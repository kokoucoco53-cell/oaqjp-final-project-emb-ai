"""Call the Watson NLP emotion prediction service."""
import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the required empty result when input or service response is invalid."""
    result = {emotion: None for emotion in EMOTION_KEYS}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze):
    """Return scores for five emotions and the dominant emotion."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    try:
        response = requests.post(
            EMOTION_URL,
            headers=HEADERS,
            json={"raw_document": {"text": text_to_analyze}},
            timeout=30,
        )
    except requests.RequestException:
        return _empty_result()

    if response.status_code == 400:
        return _empty_result()
    if response.status_code != 200:
        return _empty_result()

    try:
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        scores = {key: emotions.get(key) for key in EMOTION_KEYS}
        if any(value is None for value in scores.values()):
            return _empty_result()
        scores["dominant_emotion"] = max(EMOTION_KEYS, key=scores.get)
        return scores
    except (KeyError, IndexError, TypeError, ValueError):
        return _empty_result()
