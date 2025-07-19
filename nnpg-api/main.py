from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import os

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists("raw_images"):
    os.makedirs("raw_images")

if not os.path.exists("processed_images"):
    os.makedirs("processed_images")


@app.post("/")
async def process_image(file: UploadFile):
    # Read image data from UploadFile
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # save raw image
    raw_image_filename = f"raw_images/{file.filename}"
    image.save(raw_image_filename)

    # Convert to grayscale using Pillow's convert("L") method
    grayscale_image = image.convert("L")

    # Resize image to (28, 28)
    resized_image = grayscale_image.resize((28, 28))

    # Save the grayscale image
    output_filename = f"processed_images/grayscale_{file.filename}"
    resized_image.save(output_filename, "jpeg")

    return {"image": "processed"}
