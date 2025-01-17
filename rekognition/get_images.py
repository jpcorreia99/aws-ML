import requests

def get_image_from_url(imgurl):
    resp = requests.get(imgurl)
    imgbytes = resp.content
    return imgbytes


def get_image_from_file(filename):
    """Based on
       https://docs.aws.amazon.com/rekognition/latest/dg/example4.html,
       last access 26/06/202020"""
    with open(filename, 'rb') as imgfile:
        return imgfile.read()