# python 3.9

from requests import *
import sys
from email.utils import formatdate
from base64 import b64encode
import hmac
from hashlib import sha1
import mimetypes

# some necessary config
AccessKeyId = "..."         # fine in "my credentials", "access key". if you dont have, you can create one
AccessKeySecret = "..."     # same for AccessKeyId
BucketName = "..."          # the OBS bucket name, you can find in your console
UploadPath = "..."          # the OBS path that you want to save
Endpoint = "..."            # Endpoint, in your console

def upload(file_name, content, file_type):
    Date = formatdate(timeval=None, localtime=False, usegmt=True)
    header = {"Content-Type": file_type,
              "Date": Date}

    # path check
    Object = UploadPath
    if not Object.startswith("/"): Object = "/" + Object
    if not Object.endswith("/"): Object += "/"
    Object += file_name

    str2sign = f"PUT\n\n{header['Content-Type']}\n{header['Date']}\n/{BucketName}{Object}"
    MAC = b64encode(hmac.new(AccessKeySecret.encode("u8"), str2sign.encode('u8'), sha1).digest()).decode('u8')
    header["Authorization"] = f"OBS {AccessKeyId}:{MAC}"

    try:
        res = put(f"https://{BucketName}.{Endpoint}{Object}", headers=header, data=content)
    except Exception as e:
        print(f"[ERROR] Upload {file_name} error")
        print(e)
        exit(1)

    if res.status_code == 200:
        return f"https://{BucketName}.{Endpoint}{Object}"
    else:
        print(f"[ERROR] {res.status_code} Fail")
        exit(1)


if __name__=="__main__" :

    # Please use absolute path for files.

    files = sys.argv[1:]
    if files == []:
        print("[ERROR] No provided file path")
        exit(1)

    response_url = []
    for file in files:

        try:
            content = open(file, "rb").read()
        except:
            print(f"[ERROR] The {file} that provide doesn't exist")
            exit(1)

        if '/' not in file:
            file_name = file.split("\\")[-1]
        else :
            file_name = file.split("/")[-1]

        type = mimetypes.guess_type(file)[0]

        if type is None:
            type = "application/octet-stream"

        response_url.append(upload(file_name, content, type))

    print("Upload Success:")
    for url in response_url:
        print(url)






