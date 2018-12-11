from pathlib import Path
from re import search, sub
from regexfolders import regexes
def main():
    # Will be user inputed: *********
    origin = "./Test Data/downloads"
    dest = "./Test Data/videos"
    # *******************************

    fileDirList = getFileDirList(origin)
    filePartsList = [i.parts for i in fileDirList]
    fileListNoSamples = sapleFilter(filePartsList)
    fileList = urlFilterName(fileListNoSamples)

    return fileList


def getFileDirList(origin):
    fileExtentionWhitelist = ['.avi', '.flv', '.mkv', '.mp4', '.mov', '.wmv']
    return [i.relative_to(origin) for i in Path(origin).glob('**/*') if i.suffix in fileExtentionWhitelist]


def urlFilterName(fileDirList):
    return [i if not search(regexes['url_detector'],i[-1]) else [i[:-1] + tuple(sub(regexes['url_detector'],"",i[-1]))] for i in fileDirList]
    


def sapleFilter(fileDirList):
    return [i for i in fileDirList if len([j for j in i if search("[Ss]ample", j)]) == 0]


for i in main():
    print(i)