# uses amazon comprehend to evaluate the sentiment of a given input
import boto3

text = input("Insert a phrase whose sentiment will be evaluated: ")

client = boto3.client('comprehend')
req_resp = client.detect_sentiment(LanguageCode="en",
                                   Text=text)

print("The detected sentiment was: " + req_resp['Sentiment'])


for sentiment, confidence_value in req_resp['SentimentScore'].items():
    print(sentiment + ": " + str(confidence_value))
