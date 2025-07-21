'use client';

import { useState } from 'react';
import Title from "@/app/components/title";
import ImageUpload from "@/app/components/imageUpload";
import ImageDisplay from '@/app/components/imageDisplay';
import ImagePredict from '@/app/components/imagePredict';
import PredictionText from '@/app/components/predictionText';
import FeedbackText from '@/app/components/feedbackText';
import FeedbackButtons from '@/app/components/feedbackButtons';

export default function Home() {
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [imageForm, setImageForm] = useState<FormData | null>(null);
  const [predictionText, setPredictionText] = useState<string>("0 or not 0");
  return (
    <main className='h-screen w-screen overflow-hidden grid grid-cols-2 grid-rows-31 gap-15'>
      <Title text="Binary Classification for Handwritten Digits" />

      <div className="col-span-1 row-span-13">
        <div className="flex justify-center py-30">
          <ImageUpload onImageSelect={setImageUrl} onImageUpload={setImageForm} />
        </div>
      </div>

      <div className="col-span-1 row-span-13">
        <div className="flex justify-center py-30">
          <ImageDisplay imageUrl={imageUrl} />
        </div>
      </div>

      <div className="col-span-1 row-span-5">
        <div className="flex justify-center">
          <ImagePredict imageForm={imageForm} onImagePredict={setPredictionText}/>
        </div>
      </div>

      <div className="col-span-1 row-span-5">
        <div className="flex justify-center">
          <PredictionText predictionText={predictionText}/>
        </div>
      </div>

      <div className="col-span-1 row-span-5">
        <div className="flex justify-center">
          <FeedbackText />
        </div>
      </div>

      <div className="col-span-1 row-span-5">
        <div className="flex justify-center">
          <FeedbackButtons />
        </div>
      </div>
    </main>
  );
}
