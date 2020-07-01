# AWS ML
Scripts developed along with the "Getting started with aws machine learning" course on Coursera. 

These illustrate the usage of different AWS machine learning services through python and s3 buckets.

## Contents

- **[Requirements](#requirements)**
- **[Rekognition](#rekognition)**
- **[Comprehend & Translate](#comprehend--translate)**
- **[SageMaker](#sagemaker)**

## Requirements 
To install the required dependencies run:
  > pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

Also install the AWS CLI. In in Manjaro run:
 > sudo pacman -S aws-cli

Finally, create IAM credentials by creating a user on the IAM tab on the aws console tab.
This will yeald a file called *new_user_credentials.csv* which will contain the credentials for the new user. 

To configure the user just write on the console:
> aws configure 

and fill the prompt with the information provided on the .csv file.

## Rekognition
Rekognition is a computer vision service offered by AWS. It is capable of handling a handful of really useful features,
such as object detection, scene classification and face detection/comparison. 

The scripts on the *rekognition* folder show basic usage of these features using the ***boto3*** library in order to 
deal with the s3 buckets.

## Comprehend & Translate
Amazon Comprehend and Translate are two services which automate Natural language processing tasks.

The scripts showcase API calls to both of these services in order to perform sentiment analisys and text translation.

## SageMaker

SageMaker is an whole complete platform for development of ml systems. It offers services which cover the whole 
development pipeline:

* Labeling
* Model development
* Hyperparameter tuning
* Deployment

The notebook *demo.py* is provided by the course and demonstrates the usage of the sagemaker services.

