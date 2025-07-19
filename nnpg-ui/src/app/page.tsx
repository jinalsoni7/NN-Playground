'use client';

import { useState } from 'react';
import Title from "@/app/components/title";
import ImageUpload from "@/app/components/imageUpload";
import ImageDisplay from '@/app/components/imageDisplay';
import ImagePredict from '@/app/components/imagePredict';
import PredictionText from '@/app/components/predictionText';

export default function Home() {
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [imageForm, setImageForm] = useState<FormData | null>(null);
  return (
    <main className='grid grid-cols-2 grid-rows-13'>
      <Title text="Binary Classification for Handwritten Digits" />

      <div className="col-span-1 row-span-7">
        <div className="flex justify-center py-30">
          <ImageUpload onImageSelect={setImageUrl} onImageUpload={setImageForm} />
        </div>
      </div>

      <div className="col-span-1 row-span-7">
        <div className="flex justify-center py-30">
          <ImageDisplay imageUrl={imageUrl} />
        </div>
      </div>

      <div className="col-span-1 row-span-4">
        <div className="flex justify-center">
          <ImagePredict imageForm={imageForm}/>
        </div>
      </div>

      <div className="col-span-1 row-span-4">
        <div className="flex justify-center">
          <PredictionText />
        </div>
      </div>

    </main>
  );
}
