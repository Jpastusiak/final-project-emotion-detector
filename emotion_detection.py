import requests  # Import the requests library to handle HTTP requests
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
   # URL of the sentiment analysis service
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   # Create a dictionary with the text to be analyzed
   myobj = { "raw_document": { "text": text_to_analyse } }
   # Set the headers required for the API request
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
   # Send a POST request to the API with the text and headers
   response = requests.post(url, json = myobj, headers=header)

   # Parse the JSON response
   formatted_response = response.json()

   # Try to safely extract emotion data
   try:
      emotions = formatted_response['emotionPredictions'][0]['emotion']
      anger_score = emotions['anger']
      disgust_score = emotions['disgust']
      fear_score = emotions['fear']
      joy_score = emotions['joy']
      sadness_score = emotions['sadness']
      dominant_emotion = max(emotions, key=emotions.get)
   except (KeyError, IndexError) as e:
      return {"error": f"Unexpected response format: {e}"}

   return {
      'anger': anger_score,
      'disgust': disgust_score,
      'fear': fear_score,
      'joy': joy_score,
      'dominant_emotion': dominant_emotion
   }