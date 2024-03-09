import os;
from google.cloud import storage;

#Validate google applications into OS environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/guga6/OneDrive/Documentos/studies/python-course/cloud-storage/unimarket.json';

#Instance the client storage management -> storage.Client()
client_storage = storage.Client();

#Create cloud buckets -> Bucket Name && Bucket Location
""" bucket_name = 'market_items';
bucket = client_storage.bucket(bucket_name);
bucket = client_storage.create_bucket(bucket, location="US"); """

#Access specific bucket -> storage.get_bucket()

#Upload files to a bucket
#1º -> Get bucket;
#2º -> Set a blob for the gotten bucket;
#3º -> Use the setted blob for uploading a file;
""" def uploadFile(bucket_name, blob_name, file_path) :
  try :
    bucket = client_storage.get_bucket(bucket_name);
    bucket_blob = bucket.blob(blob_name);
    bucket_blob.upload_from_filename(file_path);
    
    print("Upload successfully done.")
    return True;
  except Exception as e:
    print(e);

    return False;

uploadFile("market_items", "unicorn-picture", "C:/Users/guga6/OneDrive/Documentos/studies/python-course/cloud-storage/unicorn-emoji-image.png"); """

#Download files from a bucket
#1º -> Get a specific bucket
#2º -> Declare an existent blob inside the gotten bucket
#3º -> Download file from the declared blob

def dowloadFile(bucket_name, blob_name) :
  try :
    bucket = client_storage.get_bucket(bucket_name);
    blob = bucket.blob(blob_name);
    with open(os.path.join(os.getcwd(), blob_name + ".png"), "wb") as destiny_path :
      client_storage.download_blob_to_file(blob, destiny_path);

    print("Dowload was done successfully.");

    return True;
  except Exception as e:
    print(e);

    return False;

dowloadFile("market_items", "unicorn-picture");
