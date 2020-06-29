import boto3

text = input("Insert a phrase whose sentiment will be evaluated: ")

client = boto3.client('comprehend')
req_resp = client.detect_sentiment(LanguageCode="en",
                                   Text="text")

print("The detected sentiment was: " + req_resp['Sentiment'])
print("\nSentiment scores:")
for sentiment_info in req_resp['SentimentScore']:
    print(sentiment_info)
from pprint import pprint

pprint(req_resp)
