"""Unit tests for the EmotionDetection package."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify the dominant emotion for representative statements."""

    def test_dominant_emotions(self):
        """Check the expected dominant emotion for each sample."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
