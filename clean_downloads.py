from pathlib import Path
from re import search, sub
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
def main():
    # Will be user inputed: *********
    origin = "./Test Data/downloads"
    dest = "./Test Data/videos"
    # *******************************

    fileDirList = getFileDirList(origin)
    filePartsList = [i.parts for i in fileDirList]
    fileList = sapleFilter(filePartsList)
    #fileList = urlFilterName(fileListNoSamples)
    for i in fileList:
        filterSE(i)
    return fileList


def getFileDirList(origin):
    fileExtentionWhitelist = ['.avi', '.flv', '.mkv', '.mp4', '.mov', '.wmv']
    return [i.relative_to(origin) for i in Path(origin).glob('**/*') if i.suffix in fileExtentionWhitelist]


def urlFilterName(fileDirList):
    return [i if not search(regexes['url_detector'],i[-1]) else [i[:-1] + tuple(sub(regexes['url_detector'],"",i[-1]))] for i in fileDirList]
    


def sapleFilter(fileDirList):
    return [i for i in fileDirList if len([j for j in i if search("[Ss]ample", j)]) == 0]


main()