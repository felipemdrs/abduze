import hashlib

def getSha1(filePath):
    file = open(filePath, "rb")
    sha1hash = hashlib.sha1()
    while True:
        buffer = file.read(0x100000)
        if not buffer:
            break
        sha1hash.update(buffer)
    file.close()
    return sha1hash.hexdigest()

def sha1Equals(sha1, filePath):
    return sha1 == getSha1(filePath)