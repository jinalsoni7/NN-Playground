export default function PredictionText() {
    const myValue = "0 or not 0";
    return (
        <input
            className="text-sky-700 text-xl"
            type="text"
            id="readOnlyField"
            value={myValue}
            readOnly // This makes the input read-only
        />
    );
}
