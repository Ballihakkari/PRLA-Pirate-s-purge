from pathlib import Path
from re import match, search, sub
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
def main():
    # Will be user inputed: *********
    origin = "./Test Data/downloads"
    dest = "./Test Data/videos"
    # *******************************
    fileDirList       = getFileDirList(origin)
    filePartsList     = [i.parts + (i.parts[-1],) for i in fileDirList]
    fileListNoSamples = sapleFilter(filePartsList)
    fileListNoURL     = urlStripFilename(fileListNoSamples)
    fileListNoSymbols = sybolStripFilename(fileListNoURL)
    fileListYears     = yearBrackedizer(fileListNoSymbols)
    fileListBuilt     = buildFilename(fileListYears)
    fileListSeasoned  = seasonFixer(fileListBuilt)
    fileListSpaced    = seasonSpacer(fileListSeasoned)
    fileListTitled    = titleFilename(fileListSpaced)
    fileListNoEndings = stripFilename(fileListTitled)
    
    todo = [i for i in fileListNoEndings if not search('.+S\d\dE\d\d',i[-1]) and not search(regexes['realease_year'],i[-1])]
    # return todo
    return fileListNoEndings

    # for i in fileList:
    #     filterSE(i)
    # return fileList

def getFileDirList(origin):
    fileExtentionWhitelist = ['.avi', '.flv', '.mkv', '.mp4', '.mov', '.wmv']
    return [i.relative_to(origin) for i in Path(origin).glob('**/*') if i.suffix.lower() in fileExtentionWhitelist]

def regExReplace(regExString, replacementString, pathParts):
    fileParts = pathParts[-1].rsplit('.',1)
    return pathParts[:-1] + (sub(regExString, replacementString, fileParts[0]) + '.' + fileParts[1],)

def urlStripFilename(fileDirList):
    return [regExReplace(regexes['url_detector'], '', i) for i in fileDirList]

def sapleFilter(fileDirList):
    return [i for i in fileDirList if len([j for j in i if search(regexes['sample'], j)]) == 0]


def sybolStripFilename(fileDirList):
    filtredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filtredList.append(i[:-1] + (sub('  +',' ',sub('[\.\-\(\)\[\]]',' ',fileParts[0]).strip())+'.'+fileParts[1],))
    return filtredList


def stripFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        if search('S\d{2}E\d{2}',i[-1]):
            filteredList.append(i[:-1] + (sub('(?<=S\d{2}E\d{2}) .+(?=\.)','',sub(' \(\d{4}\)','',i[-1])),))
        else:
            filteredList.append(i[:-1] + (sub('(?<=\)) .+(?=\.)','',i[-1]),))
    return filteredList


def titleFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filteredList.append(i[:-1] + (fileParts[0].title()+'.'+fileParts[-1].lower(),))
    return filteredList


def seasonFixer(fileDirLis):
    filteredList = []
    for i in fileDirLis:
        if search('[Ss]?\d{1,2}[EeXx ]*\d{1,2}(?= )',i[-1]):
            se = filterSE(i)
            if se is not None:
                filteredList.append(i[:-1] + (sub('[Ss]?\d{1,2}[EeXx ]*\d{1,2}(?= )','S'+se[0]+'E'+se[1],i[-1],1),))
            else:
                filteredList.append(i)
    return filteredList

def seasonSpacer(fileDirList):
    filteredList = [i[:-1] + (sub('(?<=[^ ])[Ss]\d{2}[Ee]\d{2}(?= )',' \g<0>', i[-1]),) for i in fileDirList]
    return [i[:-1] + (sub('(?<= )[Ss]\d{2}[Ee]\d{2}(?=[^ ])','\g<0> ', i[-1]),) for i in filteredList]


def buildFilename(fileDirList):
    # return fileDirList
    
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        m = match(regexes['num_no_space'],i[-1]) 
        if m:
            if len(m.group(0)) < 3 and search(regexes['num_no_space'],i[-3]):

                if len(i) > 3:
                    filteredList.append(i[:-1] + (i[-4]+' S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
                elif len(i) > 2 :# and search(regexes['num_no_space'],i[-3]):
                    filteredList.append(i[:-1] + ('S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
                    
            elif len(m.group(0)) == 3 and len(i) > 2:
                if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
                    filteredList.append(i[:-1] + (i[-4]+' S0'+i[-1][0]+'E'+i[-1][1:2].zfill(2),))
                else:
                    filteredList.append(i[:-1] + (i[-3]+' S0'+i[-1][0]+'E'+i[-1][1:2].zfill(2),))
            elif len(m.group(0)) == 4:
                if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
                    filteredList.append(i[:-1] + (i[-4]+' S'+i[-1][0:1].zfill(2)+'E'+i[-1][2:3].zfill(2),))
                else:
                    filteredList.append(i[:-1] + (i[-3]+' S'+i[-1][0:1].zfill(2)+'E'+i[-1][2:3].zfill(2),))
            else:
                filteredList.append(i)
        elif match(regexes['usual_series_format'],i[-1]) and len(i) > 2 :
            if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
                filteredList.append(i[:-1] + (i[-4]+' '+i[-1],))
            else:
                filteredList.append(i[:-1] + (i[-3]+' '+i[-1],))
        elif match('[Ee]?([Pp][Ii][Ss][Oo][Dd][Ee])? ?\d',fileParts[0]) and len(i) > 3:
            if search(regexes['num_no_space'],i[-3]):
                filteredList.append(i[:-1] + (i[-3]+' S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
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
count = 0
for i in main():
    print(i[-2:])
    count += 1    
    # if count == 40:
    #     count = input()
    #     count = 0
print(count)


