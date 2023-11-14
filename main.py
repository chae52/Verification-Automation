import boto3
from botocore.exceptions import NoCredentialsError

# AWS 계정 및 S3 정보 설정
aws_access_key = 'YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'YOUR_AWS_SECRET_KEY'
bucket_name = 'YOUR_S3_BUCKET_NAME'

# S3 클라이언트 생성
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# DB에서 이미지 URL을 가져오는 코드
image_urls = get_image_urls_from_db()

# 이미지를 S3에 업로드
for url in image_urls:
    response = requests.get(url)
    if response.status_code == 200:
        # 이미지를 S3 버킷에 업로드
        s3.upload_fileobj(response.content, bucket_name, f'{hash(url)}.jpg')
    else:
        print(f"Failed to download image from {url}")
