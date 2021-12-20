import os, dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = file_to + "/" + relative_path

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.A-h-btq5qI_JnnfVH8dp9bnnj9lmYjx0awkT6UEVavMdMQ76vaQGL3Rt1PU31UoCLiw576_btvYRs5lfkSL-1MIl1tDzQ92TlAjNnAAwEnJ04ohpFWDchYlyXLzDR21_hT9JMak"
    transferData = TransferData(access_token)

    file_from = input("Enter source path: ")
    file_to = input("Enter destionation path: ")

    transferData.upload_file(file_from, file_to)

    print("Uploaded")

main()