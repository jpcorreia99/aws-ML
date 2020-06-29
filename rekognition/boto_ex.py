import boto3

s3 = boto3.resource('s3')

print(s3.buckets.all())
for bucket in s3.buckets.all():  # NOTe: in .aws/config the first line must be [default]
    print(bucket)

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(instance)
