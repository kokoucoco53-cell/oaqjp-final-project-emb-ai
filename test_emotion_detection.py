"""Unit tests for the Emotion Detection package."""
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def mock_response(self, dominant):
        scores = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1,
        }
        scores[dominant] = 0.9
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, post):
        post.return_value = self.mock_response("joy")
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, post):
        post.return_value = self.mock_response("anger")
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, post):
        post.return_value = self.mock_response("disgust")
        self.assertEqual(emotion_detector("I feel disgusted")["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, post):
        post.return_value = self.mock_response("sadness")
        self.assertEqual(emotion_detector("I am so sad")["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, post):
        post.return_value = self.mock_response("fear")
        self.assertEqual(emotion_detector("I am afraid")["dominant_emotion"], "fear")

    def test_empty_input(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
