# uses amazon comprehend to evaluate the sentiment of a given input
import boto3

text = input("Insert a phrase to be translated to chinese: ")

client = boto3.client('translate')
req_resp = client.translate_text(SourceLanguageCode="en", TargetLanguageCode='zh',
                                 Text=text)

print("Translated text: ", req_resp['TranslatedText'])
