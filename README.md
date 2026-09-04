# Final Project: AI-Based Web Application Development and Deployment

This repository contains the completed IBM Skills Network final project: a
Flask web application that uses the Watson NLP Emotion Predict service to
analyze text, return five emotion scores, and identify the dominant emotion.

## Run the project

```bash
pip install requests flask pylint
python3 server.py
```

Open `http://127.0.0.1:5000`, enter a sentence, and select **Run Sentiment
Analysis**.

## Test and analyze the code

```bash
python3 -m unittest test_emotion_detection.py -v
pylint server.py
```
