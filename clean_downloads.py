from pathlib import Path
from re import match, search, sub, findall
from regexfolders import regexes
from filterSeason import filter_Season as filterSE
# from great_user import great_user
from add_file_to_dest import add_file_to_dest
import asyncio, sys, argparse, os
from filter_functions import *

def main():
    origin = "C:\\Users\\Sæmundur\\Desktop\\downloads"
    dest = "C:\\Users\\Sæmundur\\Desktop\\dest"
    # if len(sys.argv) > 2 and  os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
    #     origin = sys.argv[1]
    #     dest = sys.argv[2]
    #     print(origin + "\n" + dest)
    # else:        
    #     user_input = asyncio.run(great_user())   #Returns tuple(origin, destination, settings)
    #     origin = user_input[0]     
    #     dest = user_input[1]       
    #     # settings = user_input[2]

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
    
    for f in fileListNoEndings:
        add_file_to_dest(f, origin, dest)  
    
    # todo = [i for i in fileListNoEndings if not search(r'.+S\d\dE\d\d',i[-1]) and not search(regexes['realease_year'],i[-1])]
    # return todo
    # return fileListNoEndings


# main()
# count = 0
# for i in main():
#     print(i)
#     # print(filterSE(i[-1]))
#     count += 1    
#     if not count % 40:
#         input()
# print(count)

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