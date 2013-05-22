"""
Download file from s3.
"""
import sys
from boto.s3.connection import S3Connection


aws_access_key_id = sys.argv[1]
aws_secret_access_key = sys.argv[2]
bucket_name = sys.argv[3]
key_name = sys.argv[4]
local_file_name = sys.argv[5]

c = S3Connection(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
bucket = c.get_bucket(bucket_name=bucket_name)
key = bucket.lookup(key_name)
local_file = open(local_file_name, 'wb')
key.get_contents_to_file(local_file)