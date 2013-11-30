import hashlib

def getSha1(filePath):
    return hashlib.sha1(open(filePath).read()).hexdigest()
    
def sha1Equals(sha1, filePath):
    return sha1 == getSha1(filePath)