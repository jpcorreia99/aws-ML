# uses amazon comprehend to detect the language of a given input
import boto3

text = input("Insert a phrase whose laguages will be evaluated: ")

client = boto3.client('comprehend')
req_resp = client.detect_dominant_language(Text=text)

print("Detected languages:")
for language in req_resp['Languages']:
    print("Language code: ", language['LanguageCode'], ", score: ", language['Score'])
