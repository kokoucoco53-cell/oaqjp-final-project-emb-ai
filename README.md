# oaqjp-final-project-emb-ai

Emotion Detector final project.

## Description
This Flask application uses the Watson NLP emotion prediction service to analyze text and return scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Project structure
- `EmotionDetection/emotion_detection.py` — calls the emotion prediction service.
- `EmotionDetection/__init__.py` — exposes the package function.
- `server.py` — Flask application and `/emotionDetector` endpoint.
- `templates/index.html` — browser interface.
- `static/style.css` — page styling.
- `test_emotion_detection.py` — unit tests.

## Setup
Use Python 3.10 or newer.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run tests

```bash
python -m unittest test_emotion_detection.py
```

The tests mock the external service so they can check application behavior without depending on network availability.

## Run the web application

```bash
python server.py
```

Open `http://127.0.0.1:5000` in your browser. The live emotion analysis requires access to the IBM Skills Network Watson emotion service.

## Important
The unit tests use mocked service responses. They verify the application's handling and dominant-emotion selection, but they are not proof that the remote Watson service is currently reachable. Capture your own screenshots from the running application for assignment evidence.
