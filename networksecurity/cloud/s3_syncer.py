import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)
        print(f"Synced {folder} to {aws_bucket_url}")

    def sync_folder_from_s3(self, aws_bucket_url, folder):
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        os.system(command)
        print(f"Synced {aws_bucket_url} to {folder}")