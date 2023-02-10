# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import boto3
import os

def download_model():
    # Download the weights from s3 (can be changed to download weights from any cloud)
    os.makedirs("dreambooth_weights/")
    s3 = boto3.resource(service_name='s3',endpoint_url='https://cos.na-siliconvalley.myqcloud.com',region_name='na-siliconvalley', aws_access_key_id='AKIDF9oDQPjm6B0ZsxpZz9UYQzPaT6VhPLu8', aws_secret_access_key='70d6NTKwVlodJn99uPVMxYyDAryviHVW')
    bucket = s3.Bucket("dreambooth-1251401306")
    for obj in bucket.objects.filter(Prefix="dreambooth/"):
        print(obj.key);
        target = os.path.join("dreambooth_weights/", os.path.relpath(obj.key, "dreambooth/"))
        print(target);
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)
# bucket = s3.Bucket("dreambooth-1251401306")
    

if __name__ == "__main__":
    download_model()
