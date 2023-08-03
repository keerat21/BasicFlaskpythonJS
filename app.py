import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import the CORS extension

from textblob import TextBlob


app = Flask(__name__)
CORS(app, origins="http://localhost:8081")
 # Initialize CORS with your Flask app

# Set up the logging configuration
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    print("Received data:", data)  # Add this logging statement
    print("number", len(data))  # size
    text = data[text][1]

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
