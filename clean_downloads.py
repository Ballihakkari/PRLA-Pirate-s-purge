from pathlib import Path
from re import match, search, sub, findall
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
from great_user import great_user
from add_file_to_dest import add_file_to_dest
import asyncio
def main():
    # Will be user inputed: *********
    origin = "Test Data/downloads"
    dest = "Test Data/videos"

    # user_input = asyncio.run(great_user())   #Returns tuple(origin, destination, settings)
    # origin = user_input[0]     
    # dest = user_input[1]       
    # settings = user_input[2]
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
    fileListRomanized = romanNumCap(fileListTitled)
    fileListNoEndings = stripFilename(fileListRomanized)
    
    todo = [i for i in fileListNoEndings if not search(r'.+S\d\dE\d\d',i[-1]) and not search(regexes['realease_year'],i[-1])]
    return todo
    # for f in fileListNoEndings:
    #     add_file_to_dest(f, origin, dest)  
    return fileListNoEndings


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
        filtredList.append(i[:-1] + (sub('  +',' ',sub(r'[\.\-_\(\)\[\]\{\}]',' ',fileParts[0]).strip())+'.'+fileParts[1],))
    return filtredList


def stripFilename(fileDirList): # TODO: Fix... 
    # filteredList = []
    # for i in fileDirList:
    #     if search(r'S\d{2}E\d{2}',i[-1]):
    #         filteredList.append(i[:-1] + (sub(r'(?<=S\d{2}E\d{2}) .+(?=\.)','',sub(regexes['realease_year'],'',i[-1])),))
    #     else:
    #         filteredList.append(i[:-1] + (sub(r'(?<=\)) .+(?=\.)','',i[-1]),))
    # return filteredList
    filteredList = []
    for i in fileDirList:
        if search(r'S\d{2}E\d{2}(?= )',i[-1]):
            # filteredList.append(i[:-1] + (sub('(?:S\d{2}(E\d{2})+[^ ]*) .+(?=\.)','\g<0>',sub(' \(\d{4}\)','',i[-1])),)) # ToDo
            filteredList.append(i[:-1] + (sub(r'(?<=S\d{2}E\d{2}) .+(?=\.)','',sub(' \(\d{4}\)','',i[-1])),))
        elif search(r'S\d{2}E\d{2}',i[-1]):
            filteredList.append(i[:-1] + (sub(r'(?<=S\d{2}E\d{2}) .+(?=\.)','',sub(' \(\d{4}\)','',i[-1])),))
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
    # """" Old version """
    # filteredList = []
    # for i in fileDirLis:
    #     if search(r'[Ss]?\d{1,2}[EeXx ]*\d{1,2}(?= )',i[-1]):
    #         se = filterSE(i[-1])
    #         if se is not None:
    #             filteredList.append(i[:-1] + (sub('[Ss]?\d{1,2}([EeXx ]+\d{1,2}|[EeXx ]*\d{2})(?= )','S'+se[0][0]+'E'+se[0][1],i[-1],1),))
    #         else:
    #             filteredList.append(i)
    #     else:
    #         filteredList.append(i)
    # return filteredList

    """ New version """
    filteredList = []
    # count = 0
    for i in fileDirLis:
        se = filterSE(i[-1])
        try:
            if int(se[1]) > 1900:
                filteredList.append(i)
            else:
                eval('420/0') #here we devide by zero, for comedic effect
        except:
            if se:
                SeriesString = 'S'
                for epse in se[0]:
                    SeriesString+=epse+'E'
                SeriesString = SeriesString[:-1]
                i = list(i)
                print(i)
                print(se[1])
                i[-1] = sub(se[1], SeriesString, i[-1], 1)
                print(i)
                filteredList.append(tuple(i))
            else:
                filteredList.append(i)
    return filteredList


def seasonSpacer(fileDirList):
    return [i[:-1] + (sub(r'(?<=[^ ])[Ss]\d{2}[Ee]\d{2}(?= )',r' \g<0>', i[-1]),) for i in fileDirList]
    # filteredList = [i[:-1] + (sub('(?<=[^ ])[Ss]\d{2}[Ee]\d{2}(?= )',' \g<0>', i[-1]),) for i in fileDirList]
    # return [i[:-1] + (sub('(?<= )[Ss]\d{2}[Ee]\d{2}(?=[^ ])','\g<0> ', i[-1]),) for i in filteredList]


def pathSegmentSeasonSearch(pathSegment):
    return search(r'((^| )[Ss][^ ]* \d+)|((^| )\d{1,2}\.?[Ss])', pathSegment)
def pathSegmentEpisodeSearch(pathSegment):
    return search(r'((^| )[Ee].* \d+)|((^| )\d{1,2}\.?[Ee])', pathSegment)
    # return search(r'((^| )[Ee][^ ]* \d+)|((^| )\d{1,2}\.?[Ee])', pathSegment)
def __extractNumbersFromSearch__(string):
    return search(r'\d{1,2}', string.group(0)).group(0).zfill(2)

def buildFilename(fileDirList):
    filteredList = []
    for i in fileDirList:
        dirDepth = len(i)
        isMatch = match('\d{1,4}', i[-1])
        isSeasoned = search(r'[Ss]?\d{1,2}[EeXx ]+\d{1,2}(?=[ \.])', i[-1])
        
    # """ The name starts with some numbers """
        if (isMatch is not None) and (isSeasoned is None): 
            if len(isMatch.group(0)) < 3:
                if dirDepth > 3:
                    # Files locaded in a folder at least 3 steps below The ORIGIN folder
                    # without a discernable season nr. 
                    # the parent folders will be searched for a title and season nr.
                    parentHasSeason = pathSegmentSeasonSearch(i[-3])
                    if parentHasSeason:
                        seasonNr = __extractNumbersFromSearch__(parentHasSeason)
                        # print("File Handled 1: ", (i[:-1] + (i[-4] + ' S' + seasonNr + 'E' + i[-1].zfill(2),)))
                        filteredList.append(i[:-1] + (i[-4] + ' S' + seasonNr + 'E' + i[-1].zfill(2),))
                    else:
                        # Files without a discernable season nr.
                        # in the parent folder 
                        # - Are most likely movies
                        # print("Not Handled 2: ", i)
                        filteredList.append(i)
                elif dirDepth > 2:
                    # Files locaded in a folder directly below The ORIGIN folder
                    # without a discernable season nr. 
                    # the parent folder will be searched for a title and season nr.
                    parentHasSeason = pathSegmentSeasonSearch(i[-3])
                    if parentHasSeason:
                        seasonNr = __extractNumbersFromSearch__(parentHasSeason)
                        # print("File Handled 3: ", (i[:-1] + (sub(parentHasSeason.group(0), ' S' + seasonNr + 'E', i[-3]) + i[-1],) ))
                        filteredList.append(i[:-1] + (sub(parentHasSeason.group(0), ' S' + seasonNr+ 'E', i[-3]) + i[-1],))
                    else:
                        # Files without a discernable season nr.
                        # in the parent folder 
                        # - Are most likely movies
                        # print("Not Handled 4: ", i)
                        filteredList.append(i)    
                else:
                    # Files locaded directly in The ORIGIN folder
                    # without a discernable epidode and or season nr. 
                    # - Are most likely movies
                    # print("Not Handled 5: ", i)
                    filteredList.append(i)
            else:
                if dirDepth > 3: 
                    # Files missing title but with season and episode nr.
                    # print("File Handled 6: ", i[:-1] + (i[-4] + ' S' + i[-1][:1].zfill(2) + 'E' + i[-1][1:] ,))
                    filteredList.append(i[:-1] + (i[-4] + ' S' + i[-1][:1].zfill(2) + 'E' + i[-1][1:] ,))
                else:
                    # print("Not Handled 7: ", i) # Note: only one case "Dead.Poets.Society/1989.Dead.Poets.Society.avi"
                    filteredList.append(i)
        
    # """ If the name starts with a complete season """
        elif match(r'[Ss]?\d{1,2}[EeXx ]+\d{1,2}[ \.]', i[-1]):
            if dirDepth > 3:
                # Files locaded in a folder at least 3 steps below The ORIGIN folder
                # without a discernable season nr. 
                # the parent folders will be searched for a title and season nr.
                parentHasSeason = pathSegmentSeasonSearch(i[-3])
                if parentHasSeason:
                    # print("File Handled 8: ", (i[:-1] + (i[-4] + ' ' + i[-1],))) # TODO: Fix "That '70s Show/Season 6'/21 5-15.avi" by all logit it shoud be cought by case #1
                    filteredList.append(i[:-1] + (i[-4] + ' ' + i[-1],))
                else:
                    # print("File Handled 9: ", i[:-1] + (i[-4] + ' ' + i[-1],)) # Note: works on current data
                    filteredList.append(i[:-1] + (i[-4] + ' ' + i[-1],)) 

            elif dirDepth > 2:
                # Files locaded in a folder directly below The ORIGIN folder
                # the parent folder will be searched for a title and season nr.
                parentHasSeason = pathSegmentSeasonSearch(i[-3])
                if parentHasSeason:
                    # print("Filr Handled 10: ", i[:-1] + (sub(parentHasSeason.group(0),' ', i[-3]) + i[-1],))
                    filteredList.append(i[:-1] + (sub(parentHasSeason.group(0),' ', i[-3]) + i[-1],))
                else:
                    # in the parent folder 
                    print("Not Handled 11: ", i)
                    filteredList.append(i)    
            else:
                # Files locaded directly in The ORIGIN folder
                # without a definitive title
                # - Are most likely movies
                # print("Not Handled 12: ", i)
                filteredList.append(i)
        
    # """ If the name (might) contains an episode """
        elif isSeasoned is None:
            hasEpisode = pathSegmentEpisodeSearch(i[-1])
            hasSeason  = pathSegmentSeasonSearch(i[-1])
            hasNumbers = search('(?<= )\d{3,4}(?=[ \.])', i[-1])
            if dirDepth > 3:
                parentHasSeason = pathSegmentSeasonSearch(i[-3])
                grandParentHasSeason = pathSegmentSeasonSearch(i[-4])
                if hasEpisode is not None:
                    epidodeNr = __extractNumbersFromSearch__(hasEpisode)
                    if hasSeason is not None:
                        seasonNr = __extractNumbersFromSearch__(hasSeason)
                        filteredList.append(i[:-1] + (sub(hasSeason.group(0), ' S' + seasonNr + 'E' + epidodeNr, i[-1]),))
                        # print("File Handled 13: ", i[:-1] + (i[:-1] + (sub(hasSeason.group(0), ' S' + seasonNr + 'E' + epidodeNr, i[-1]),)))
                    elif parentHasSeason is not None:
                        print("Not Handled 14: ", i)
                        filteredList.append(i)
                    elif grandParentHasSeason is not None:
                        seasonNr = __extractNumbersFromSearch__(grandParentHasSeason)
                        filteredList.append(i[:-1] + (sub(grandParentHasSeason.group(0), ' S' + seasonNr, i[-4]) +  sub(hasEpisode.group(0), 'E' + epidodeNr, i[-1]),))
                        # print("File Handled 15: ", (sub(grandParentHasSeason.group(0), ' S' + seasonNr, i[-4]) +  sub(hasEpisode.group(0), 'E' + epidodeNr, i[-1]),))
                    else:
                        print("Not Handled 16: ", i)
                        filteredList.append(i)
                elif hasNumbers is not None:
                    number = hasNumbers.group(0)
                    if len(number) < 4:
                        # print("File Handled 17: ", i[:-1] + (sub(number, ('S0' + number[0] + 'E' + number[1:]), i[-1]),))
                        filteredList.append(i[:-1] + (sub(number, ('S0' + number[0] + 'E' + number[1:]), i[-1]),))
                    else:
                        # print("File Handled 18: ", i[:-1] + (sub(number, ('S' + number[:2] + 'E' + number[2:]), i[-1]),))
                        filteredList.append(i)
                else:
                    # print("Not Handled 19: ", i)
                    filteredList.append(i)    
            elif dirDepth > 2:
                # Files locaded in a folder directly below The ORIGIN folder
                # without a discernable season nr. 
                # the parent folder will be searched for a title and season nr.
                if hasNumbers is not None:
                    number = hasNumbers.group(0)
                    if len(number) < 4:
                        # print("File Handled 20: ", i[:-1] + (sub(number, ('S0' + number[0] + 'E' + number[1:]), i[-1]),))
                        filteredList.append(i[:-1] + (sub(number, ('S0' + number[0] + 'E' + number[1:]), i[-1]),))
                    else:
                        print("Not Handled 21: ", i) # Note: are simple enough to be handled by season fixer
                        filteredList.append(i)
                else:
                    parentHasSeason = pathSegmentSeasonSearch(i[-3])
                    if parentHasSeason:
                        seasonNr = __extractNumbersFromSearch__(parentHasSeason)
                        # print("File Handled 22: ", i[:-1] + (sub('(?<= )\d{2}(?=[ \.])','S' + seasonNr + 'E' + '\g<0>', i[-1]),))
                        filteredList.append(i[:-1] + (sub('(?<= )\d{2}(?=[ \.])','S' + seasonNr + 'E' + '\g<0>', i[-1]),))
                    else:
                        # Files without a discernable season nr.
                        # in the parent folder 
                        # - Are most likely movies
                        if search('\(\d{4}\)', i[-1]) is None:
                            # print("Not Handled 23: ", i)
                            pass
                        filteredList.append(i)
            else:
                # Files locaded directly in The ORIGIN folder
                # print("Not Handled 24: ", i)
                filteredList.append(i)
            
        else:
            if (search('[Ss]*\d{1,2}[EeXx]\d{1,2}', i[-1]) is None) and (search('(\d{4})', i[-1]) is None):
                # print("Not Handled 25: ", i)
                pass
            filteredList.append(i)
    return filteredList

def oldBuildFilename():
    return None
    # ***********************************************************************************************************************************************************************************
    # ***********************************************************************************************************************************************************************************
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
    # ***********************************************************************************************************************************************************************************
    # ***********************************************************************************************************************************************************************************




def yearBrackedizer(fileDirList):
    return [regExReplace('(?<= )(19|20)\d{2}',r'(\g<0>)',i) for i in fileDirList]


def romanNumCap(fileDirLis):
    return fileDirLis
    # return [regExReplace('(?<= )[IiVvXxCcLlDdMm]+(?= )', '\g<0>'.upper(), i) for i in fileDirLis]


# main()
count = 0
for i in main():
    count += 1    
    if not count % 40:
        input()


step_1 = getFileDirList("Test Data/downloads")
print("S1: ", len(step_1))
step_2 = [i.parts + (i.parts[-1],) for i in step_1]
print("S2: ", len(step_2))
step_3 = sapleFilter(step_2)
print("S3: ", len(step_3))
step_4 = urlStripFilename(step_3)
print("S4: ", len(step_4))
step_5 = sybolStripFilename(step_4)
print("S5: ", len(step_5))
step_6 = yearBrackedizer(step_5)
print("S6: ", len(step_6))
step_7 = buildFilename(step_6)
print("S7: ", len(step_7))
step_8 = seasonFixer(step_7)
print("S8: ", len(step_8))
step_9 = seasonSpacer(step_8)
print("S9: ", len(step_9))
step_10 = titleFilename(step_9)
print("S10: ", len(step_10))
step_10 = stripFilename(step_10)
print("S10: ", len(step_10))
total = {i[-1] for i in step_10}
print("Total: ", len(total))
