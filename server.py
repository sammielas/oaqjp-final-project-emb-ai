from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    print("Input Text:", text_to_analyze)  # Debugging statement
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    
    response = emotion_detector(text_to_analyze)
    print("API Response:", response)  # Debugging statement
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    return f"For the given statement, the system response is {response}."

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)