import time

def timeRemainder(currentTime, totalBytes, currentBytesReceive):
    timeRemainder = (currentTime*(totalBytes-currentBytesReceive))/currentBytesReceive
    return time.strftime('%Hh:%Mmin:%Ss', time.gmtime(timeRemainder))