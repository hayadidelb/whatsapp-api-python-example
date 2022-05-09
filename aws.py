import csv
import json
import pprint

import boto3
import os

AWS_CREDENTIALS_FILE = "C:/Hayadid/licenses/aws_new_user_credentials.csv"
IMAGES_FOLDER = "C:\Hayadid\images"

with open(AWS_CREDENTIALS_FILE,"r") as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = os.path.join(IMAGES_FOLDER, "violence.JPG")

client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                        aws_secret_access_key = secret_access_key,
                      region_name='us-west-2')

with open(photo,"rb") as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={"Bytes" : source_bytes},
                                MaxLabels=10)

pprint.pprint(response)

response = client.detect_moderation_labels(Image={"Bytes" : source_bytes})
#FIXME - need to seach for violence in response["ModerationLabels"][0]{"Name"} or response["ModerationLabels"][0]{"ParentName"}
pprint.pprint(response)

