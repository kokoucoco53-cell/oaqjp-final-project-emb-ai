"""Flask web application for the Emotion Detector."""
from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the text supplied by the browser."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
