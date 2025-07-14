type ImageUploadProps = {
  onImageSelect: (fileUrl: string) => void;
};

export default function ImageUpload({ onImageSelect }: ImageUploadProps) {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      onImageSelect(imageUrl);
    }
  };

  return (
    <label className="cursor-pointer bg-yellow-300 hover:bg-amber-300 text-black px-9 py-3 rounded-lg shadow">
        Browse
      <input type="file" accept="image/*" onChange={handleChange} className="hidden" />
    </label>
  );
}
