import tarfile

with tarfile.open("archive.tar", "r") as tar:
    tar.extractall()

with open("archive.tar", "r") as tar:
    for member in tar.getmembers():
        tar.extract(member)
