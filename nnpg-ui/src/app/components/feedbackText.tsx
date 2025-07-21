export default function FeedbackText() {
    const myValue = "Did I get the classification right?";
    return (
        <input
            className="w-75 text-sky-700 text-xl"
            type="text"
            id="readOnlyField"
            value={myValue}
            readOnly // This makes the input read-only
        />
    );
}
