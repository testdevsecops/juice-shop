import tarfile
tar = tarfile.open("sample.tar.gz")
tarfile.extractall()
tar.close()
