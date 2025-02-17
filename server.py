"""
Flask application for emotion detection using Watson NLP.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the emotion of the provided text using Watson NLP.

    Returns:
        str: A message containing the emotion analysis result or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is {response}."

@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
