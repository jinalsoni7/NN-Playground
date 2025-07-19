type ImageDisplayProps = {
  imageForm: FormData | null;
};

export default function ImagePredict({ imageForm }: ImageDisplayProps) {
  const handleClick = async (e: React.MouseEvent) => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_PREDICTION_API_URL}`, {
        method: 'POST',
        body: imageForm, // No need to set Content-Type header; FormData handles it
      });
      const data = await response.json();
      console.log('Upload successful:', data);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <button
      className="cursor-pointer bg-lime-300 hover:bg-green-300 text-black px-9 py-3 rounded-lg shadow"
      onClick={handleClick}
    >
      Predict
    </button>
  );
}
