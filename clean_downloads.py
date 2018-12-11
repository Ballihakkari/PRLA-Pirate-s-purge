from pathlib import Path
def main():
    # Will be user inputed: *********
    origin = "./Test Data/downloads"
    dest = "./Test Data/videos"
    # *******************************

    pathList = getFileDirList(origin)
    fileList = [i.name for i in pathList]

    return fileList


def getFileDirList(origin):
    fileExtentionWhitelist = ['.avi', '.flv', '.mp4', '.mkv', '.wmv', '.mov']
    return [i.relative_to(origin) for i in Path(origin).glob('**/*') if i.suffix in fileExtentionWhitelist]


print(main())
