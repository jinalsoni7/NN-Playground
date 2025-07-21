type ImageUploadProps = {
  onImageSelect: (fileUrl: string) => void;
  onImageUpload: (fileForm: FormData) => void;
};

export default function ImageUpload({ onImageSelect, onImageUpload }: ImageUploadProps) {
  function imageValidation(fileUrl: string) {
    // validation function to check
    // 1) file size
    // 2) image file type
    return fileUrl;
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      imageValidation(imageUrl);
      onImageSelect(imageUrl);

      const formData = new FormData();
      formData.append('file', file);
      onImageUpload(formData);
    }
  };

  return (
    <label className="cursor-pointer bg-yellow-300 hover:bg-orange-300 text-black px-9 py-3 rounded-lg shadow">
      Browse
      <input type="file" accept="image/*" onChange={handleChange} className="hidden" />
    </label>
  );
}
