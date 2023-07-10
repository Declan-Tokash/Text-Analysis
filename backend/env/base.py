from flask import Flask, request, jsonify
from nlp import sentiment_analysis, entity_recognition, translate, summary_build

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@api.route('/process-data', methods=['POST'])
def process_data():
    data = request.json  # Access the incoming JSON data from the frontend
    processed_data = '' # Perform your desired function on the data
    if data[0] == 'Summarize':
        processed_data = summary_build(data[1])
    elif data[0] == 'Translate':
        processed_data = translate(data[1])
    elif data[0] == 'Sentiment Analysis':
        processed_data = sentiment_analysis(data[1])
    elif data[0] == 'Entity Recognition':
        processed_data = entity_recognition(data[1])
        
    return jsonify({'result': processed_data}) 

