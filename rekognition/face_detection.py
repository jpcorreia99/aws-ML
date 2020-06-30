import boto3
import numpy as np
from pprint import pprint
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from get_images import *

img_bytes = get_image_from_file('portraits/group1.jpg')

client = boto3.client('rekognition')
req_resp = client.detect_faces(Image={'Bytes': img_bytes},
                               Attributes=['ALL'])  # also performs image classification

pprint(req_resp)
im = Image.open('portraits/group1.jpg')

imgWidth, imgHeight = im.size
draw = ImageDraw.Draw(im)

for faceDetail in req_resp['FaceDetails']:
    print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
          + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

    box = faceDetail['BoundingBox']
    left = imgWidth * box['Left']
    top = imgHeight * box['Top']
    width = imgWidth * box['Width']
    height = imgHeight * box['Height']

    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(width))
    print('Face Height: ' + "{0:.0f}".format(height))

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top)

    )
    draw.line(points, fill='#00d400', width=2)

    # Alternatively can draw rectangle. However you can't set line width.
    # draw.rectangle([left,top, left + width, top + height], outline='#00d400')

im.show()
