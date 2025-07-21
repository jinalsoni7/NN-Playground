export default function FeedbackButtons() {
    return (
        <div className="space-x-4">
            <button className="cursor-pointer bg-lime-300 hover:bg-lime-700 text-black px-9 py-3 rounded-lg shadow">
                Yes
            </button>
            <button className="cursor-pointer bg-red-300 hover:bg-red-700 text-black px-9 py-3 rounded-lg shadow">
                No
            </button>
        </div>
    )
}
