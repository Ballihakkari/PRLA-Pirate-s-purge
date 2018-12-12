from pathlib import Path
from re import match, search, sub
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
def main():
    # Will be user inputed: *********
    origin = "./Test Data/downloads"
    dest = "./Test Data/videos"
    # *******************************
    fileDirList = getFileDirList(origin)
    filePartsList = [i.parts for i in fileDirList]
    fileListNoSamples = sapleFilter(filePartsList)
    fileListNoURL     = urlStripFilename(fileListNoSamples)
    fileListNoSymbols = sybolStripFilename(fileListNoURL)
    fileListNoEndings = fileListNoSymbols #stripFilename(fileListNoSymbols)
    fileListBuilt     = buildFilename(fileListNoEndings)
    fileListTitled = titleFilename(fileListBuilt)

    fileList = yearBrackedizer(fileListTitled)
    return fileList

    # for i in fileList:
    #     filterSE(i)
    # return fileList

def getFileDirList(origin):
    fileExtentionWhitelist = ['.avi', '.flv', '.mkv', '.mp4', '.mov', '.wmv']
    return [i.relative_to(origin) for i in Path(origin).glob('**/*') if i.suffix.lower() in fileExtentionWhitelist]


def urlStripFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        if search(regexes['url_detector'],fileParts[0]):
            filteredList.append((i[:-1] + (sub(regexes['url_detector'],"",fileParts[0])+'.'+fileParts[1],)))
        else:
            filteredList.append(i)
    return filteredList
    # return [i if not search(regexes['url_detector'],i[-1].rsplit('.',1)[0]) else (i[:-1] + (sub(regexes['url_detector'],"",i[-1].rsplit('.',1)[0])+'.'+i[-1].rsplit('.',1)[1],)) for i in fileDirList]


def sapleFilter(fileDirList):
    return [i for i in fileDirList if len([j for j in i if search("[Ss][Aa][Mm][Pp][Ll][Ee]", j)]) == 0]


def sybolStripFilename(fileDirList):
    filtredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        # filtredList.append(i[:-1] + (sub('  +',' ',sub('\W',' ',fileParts[0]).strip())+'.'+fileParts[1],))
        filtredList.append(i[:-1] + (sub('  +',' ',sub('[\.\-\(\)\[\]]',' ',fileParts[0]).strip())+'.'+fileParts[1],))
    return filtredList


def stripFilename(fileDirList):
    return [(i[:-1] + (sub('(?<=\d) .+(?=\.)','',i[-1]),)) for i in fileDirList]


def titleFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filteredList.append(i[:-1] + (fileParts[0].title()+'.'+fileParts[-1].lower(),))
    return filteredList


def buildFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        # print(fileParts[0])
        m = match('\d+',i[-1]) 
        if m:
            if len(m.group(0)) < 3:
                if len(i) > 2 and search('\d{1,2}',i[-2]):
                    filteredList.append(i[:-1] + (i[-3]+' S'+search('\d{1,2}',i[-2]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
                elif len(i) > 1 and search('\d{1,2}',i[-2]):
                    filteredList.append(i[:-1] + ('S'+search('\d{1,2}',i[-2]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
                    
            elif len(m.group(0)) == 3:
                filteredList.append(i[:-1] + ('S0'+i[-1][0]+'E'+i[-1][1:],))
            else:
                filteredList.append(i[:-1] + ('S'+i[-1][:1]+'E'+i[-1][2:],))
                # filteredList.append(i[:-1] + (sub('\d{1,2}\d{2}','S\g<0>',fileParts[0])+'.'+fileParts[1],))
                # filteredList.append(i[:-1] + ('S'+search('\d{1,2}',fileParts[0]).zfill(2)+'E'+search('\d',fileParts[0])+'.'+fileParts[1],))
        elif match('[Ee]?([Pp][Ii][Ss][Oo][Dd][Ee] )?',fileParts[0]):
            filteredList.append(i)
        else:
            filteredList.append(i)
    return filteredList


def yearBrackedizer(fileDirList):
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filteredList.append(i[:-1] + (sub('(19|20)\d{2}','(\g<0>)',fileParts[0])+'.'+fileParts[1],))
    return filteredList



# main()
# count = 0
for i in main():
    print(i)
    # count += 1    
    # if count == 40:
    #     count = input()
    #     count = 0


