import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

from textblob import TextBlob

app = Flask(__name__)

# Initialize CORS with options
cors = CORS(app, resources={r"/process": {"origins": "http://localhost:8081"}})

# Set up the logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    print("Received data:", data)
    text = data['text']  # Correct the way you access the text data

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    # Determine sentiment label based on the score
    if sentiment_score > 0:
        sentiment_label = 'Positive'
    elif sentiment_score < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Return the sentiment result along with the processed text
    result = {
        'processed_text': text,
        'sentiment': {
            'label': sentiment_label,
            'score': sentiment_score
        }
    }

    # Log the result
    logging.debug(f"Processed text: {result}")

    # Return the response with 'utf-8' charset specified
    response = jsonify({'result': result})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Cache-Control'] = 'no-cache'
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
