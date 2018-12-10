from pathlib import Path
def getFileDirList(origin):
    fileExtentionWhitelist = ['avi', 'flv', 'mp4', 'mkv', 'wmv', 'mov']
    fileList = [i for i in Path(origin).glob('**/*') if str(i).rsplit('.',1)[1] in fileExtentionWhitelist]

    return fileList

# print(getFileDirList("C:\\Users\\Egill\\Documents\\HR\\Önn 3\\3. Vikna Verkefni [Python]\\Assingments\\Group project\\Test Data\\downloads", ""))
getFileDirList("Test Data\\downloads", "")