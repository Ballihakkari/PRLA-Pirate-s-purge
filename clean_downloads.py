from pathlib import Path
from re import match, search, sub
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
from great_user import great_user
from add_file_to_dest import add_file_to_dest
import asyncio
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
    
    todo = [i for i in fileListNoEndings if not search(r'.+S\d\dE\d\d',i[-1]) and not search(regexes['realease_year'],i[-1])]
    # return todo
    for f in fileListNoEndings:
        add_file_to_dest(f, origin, dest)  
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
    # return [i[:-1] + (regExReplace(regexes['url_detector'], '', i),) for i in fileDirList]


def sapleFilter(fileDirList):
    return [i for i in fileDirList if len([j for j in i if search(regexes['sample'], j)]) == 0]


def sybolStripFilename(fileDirList):
    filtredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filtredList.append(i[:-1] + (sub('  +',' ',sub(r'[\.\-\(\)\[\]]',' ',fileParts[0]).strip())+'.'+fileParts[1],))
    return filtredList


def stripFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        if search(r'S\d{2}E\d{2}',i[-1]):
            # filteredList.append(i[:-1] + (sub('(?:S\d{2}E\d{2}[^ ]*) .+(?=\.)','\g<0>',sub(' \(\d{4}\)','',i[-1])),)) # ToDo
            filteredList.append(i[:-1] + (sub(r'(?<=S\d{2}E\d{2}) .+(?=\.)','',sub(regexes['realease_year'],'',i[-1])),))
        else:
            filteredList.append(i[:-1] + (sub(r'(?<=\)) .+(?=\.)','',i[-1]),))
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
        if search(r'[Ss]?\d{1,2}[EeXx ]*\d{1,2}(?= )',i[-1]):
            se = filterSE(i)
            if se is not None:
                print(i, se)
                filteredList.append(i[:-1] + (sub('[Ss]?\d{1,2}[EeXx ]*\d{1,2}(?= )','S'+se[0]+'E'+se[1],i[-1],1),))
            else:
                filteredList.append(i)
        else:
            filteredList.append(i)
    return filteredList

def seasonSpacer(fileDirList):
    return [i[:-1] + (sub(r'(?<=[^ ])[Ss]\d{2}[Ee]\d{2}(?= )',r' \g<0>', i[-1]),) for i in fileDirList]
    # filteredList = [i[:-1] + (sub('(?<=[^ ])[Ss]\d{2}[Ee]\d{2}(?= )',' \g<0>', i[-1]),) for i in fileDirList]
    # return [i[:-1] + (sub('(?<= )[Ss]\d{2}[Ee]\d{2}(?=[^ ])','\g<0> ', i[-1]),) for i in filteredList]

#*************************************************************************************************************************
#*************************************************************************************************************************
def buildFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        # print(i)
        fileParts = i[-1].rsplit('.',1)
        fileDirDepth = len(i)
        isMatch = match(regexes['num_no_space'], i[-1])
        isSeasoned = search(r'[Ss]?\d{2}[EeXx ]+\d{2}', i[-1])
        if isMatch and not isSeasoned: 
            # print(i, isMatch.group()) 
            if len(match(r'\d+',isMatch.group(0)).group(0)) < 3:
                parentIsSeason = match(r'([Ss].* ?\d+)|(\d{1,2}\.? ?[Ss])',i[-3])
                # parentIsSeason = (match('[Ss].* ?\d',i[-3]) is not None or match('\d{1,2}\.? ?[Ss]',i[-3]) is not None)
                if fileDirDepth > 3:
                    seasonNr = search(r'\d{1,2}',parentIsSeason.group(0))
                    if parentIsSeason is not None and seasonNr:
                    # if seasonNr:
                        filteredList.append(i[:-1] + (i[-4] + ' S' + seasonNr.group(0).zfill(2) + 'E' + fileParts[0].zfill(2)+'.'+fileParts[1],))
                        # print("New Filename: ", i[:-1] + (i[-4] + ' S' + seasonNr.group(0).zfill(2) + 'E' + fileParts[0].zfill(2)+'.'+fileParts[1],), "\tparentIsSeason: ", parentIsSeason, "\tseasonNr: ", seasonNr)
                    else:
                        print("Not Handled: ", i, "\tparentIsSeason: ", parentIsSeason, "\tseasonNr: ", seasonNr)
                        filteredList.append(i)
            else:
                if fileDirDepth > 3: 
                    filteredList.append(i[:-1] + (i[-4] + ' S' + i[-1][:1].zfill(2) + 'E' + i[-1][1:] ,))
                    # filteredList.append(i[:-1] + (i[-4] + i[-1],))
                    # print("New Filename 2: ", i[:-1] + (i[-4] + ' S' + i[-1][:1].zfill(2) + 'E' + i[-1][1:] ,))
                else:
                    print("Not Handled 2: ", i)
                    filteredList.append(i)
        else:
            # print(i)
            filteredList.append(i)
    # return fileDirList
    return filteredList

    
   



#*************************************************************************************************************************
#*************************************************************************************************************************

#  filteredList = []
#     for i in fileDirList:
#         fileParts = i[-1].rsplit('.',1)
#         m = match(regexes['num_no_space'],i[-1]) 
#         if m:
#             if len(m.group(0)) < 3 and search(regexes['num_no_space'],i[-3]):

#                 if len(i) > 3:
#                     filteredList.append(i[:-1] + (i[-4]+' S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
#                 elif len(i) > 2 :# and search(regexes['num_no_space'],i[-3]):
#                     filteredList.append(i[:-1] + ('S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
#                 else:
#                     filteredList.append(i)
                    
#             elif len(m.group(0)) == 3 and len(i) > 2:
#                 if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
#                     filteredList.append(i[:-1] + (i[-4]+' S0'+i[-1][0]+'E'+i[-1][1:2].zfill(2),))
#                 else:
#                     filteredList.append(i[:-1] + (i[-3]+' S0'+i[-1][0]+'E'+i[-1][1:2].zfill(2),))
#             elif len(m.group(0)) == 4:
#                 if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
#                     filteredList.append(i[:-1] + (i[-4]+' S'+i[-1][0:1].zfill(2)+'E'+i[-1][2:3].zfill(2),))
#                 else:
#                     filteredList.append(i[:-1] + (i[-3]+' S'+i[-1][0:1].zfill(2)+'E'+i[-1][2:3].zfill(2),))
#             else:
#                 filteredList.append(i)
#         elif match(regexes['usual_series_format'],i[-1]) and len(i) > 2 :
#             if (match('[Ss].+ ?\d',i[-3]) or match('\d{1,2}\.? ?[Ss]',i[-3])) and len(i) > 3:
#                 filteredList.append(i[:-1] + (i[-4]+' '+i[-1],))
#             else:
#                 filteredList.append(i[:-1] + (i[-3]+' '+i[-1],))
#         elif match('[Ee]?([Pp][Ii][Ss][Oo][Dd][Ee])? ?\d',fileParts[0]) and len(i) > 3:
#             if search(regexes['num_no_space'],i[-3]):
#                 filteredList.append(i[:-1] + (i[-3]+' S'+search(regexes['num_no_space'],i[-3]).group(0).zfill(2)+'E'+fileParts[0].zfill(2)+'.'+fileParts[1],))
#         else:
#             filteredList.append(i)
#     return filteredList

def yearBrackedizer(fileDirList):
    # return [regSub]
    filteredList = []
    for i in fileDirList:
        fileParts = i[-1].rsplit('.',1)
        filteredList.append(i[:-1] + (sub(r'(19|20)\d{2}',r'(\g<0>)',fileParts[0])+'.'+fileParts[1],))

    return filteredList



# main()
count = 0
for i in main():
    print(i)
    count += 1    
    # if count == 40:
    #     count = input()
    #     count = 0
print(count)


# step_1 = getFileDirList("Test Data/downloads")
# print("S1: ", len(step_1))
# step_2 = [i.parts + (i.parts[-1],) for i in step_1]
# print("S2: ", len(step_2))
# step_3 = sapleFilter(step_2)
# print("S3: ", len(step_3))
# step_4 = urlStripFilename(step_3)
# print("S4: ", len(step_4))
# step_5 = sybolStripFilename(step_4)
# print("S5: ", len(step_5))
# step_6 = yearBrackedizer(step_5)
# print("S6: ", len(step_6))
# step_7 = buildFilename(step_6)
# print("S7: ", len(step_7))
# step_8 = seasonFixer(step_7)
# print("S8: ", len(step_8))
# step_9 = seasonSpacer(step_8)
# print("S9: ", len(step_9))
# step_10 = titleFilename(step_9)
# print("S10: ", len(step_10))
# step_10 = stripFilename(step_10)
# print("S10: ", len(step_10))
# total = {i[-1] for i in step_10}
# print("Total: ", len(total))