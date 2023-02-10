# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import boto3
import os

def download_model():
    # Download the weights from s3 (can be changed to download weights from any cloud)
    os.makedirs("dreambooth_weights/")
    s3 = boto3.resource(service_name='s3',endpoint_url='https://ssssrr.oss-cn-shenzhen.aliyuncs.com',region_name='oss-cn-shenzhen', aws_access_key_id='LTAI5tRwn1RzJSUQgjeYEeqR', aws_secret_access_key='2NyzQeEWu9GmFIVnDlGDnHAZ6sy4WT')
    bucket = s3.Bucket("ssssrr")
    for obj in bucket.objects.filter(Prefix="dreambooth"):
        print(obj.key);
        print('\n');
        target = os.path.join("dreambooth_weights/", os.path.relpath(obj.key, "dreambooth/"))
        
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)

if __name__ == "__main__":
    download_model()
