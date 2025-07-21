type ImageDisplayProps = {
  imageUrl: string | null;
};

export default function ImageDisplay({ imageUrl }: ImageDisplayProps) {
  return (
    <div className="w-100 h-100">
      {imageUrl ? (
        <img src={imageUrl} alt="Uploaded" className="h-70 w-90 object-contain" />
      ) : (
        <span className="text-sky-700 text-xl">No image selected</span>
      )}
    </div>
  );
}
