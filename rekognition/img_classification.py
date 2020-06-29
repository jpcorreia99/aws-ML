import boto3
from get_images import *




print('ok')
img_bytes = get_image_from_file('images/seoul.jpg')


client = boto3.client('rekognition')
req_resp = client.detect_labels(Image={'Bytes': img_bytes },
                                MinConfidence=70)

from pprint import pprint
pprint(req_resp)

print('Labels')
for label in req_resp['Labels']:
    print("Label: "+label['Name']+", confidence: "+str(label['Confidence']))