type PredictionDisplayProps = {
  predictionText: string;
};

export default function PredictionText({ predictionText }: PredictionDisplayProps) {
    const myValue = "0 or not 0";
    return (
        <input
            className="text-sky-700 text-xl"
            type="text"
            id="readOnlyField"
            value={predictionText}
            readOnly // This makes the input read-only
        />
    );
}
