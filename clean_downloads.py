from pathlib import Path
from re import match, search, sub, findall
from regex_folders import regexes
from filter_season import filter_season as filterSE
from great_user import great_user
from add_file_to_dest import add_file_to_dest
from filter_functions import *
import asyncio, sys, argparse, os

def main():
    origin = ""
    dest = ""
    #If user inputs two valid paths as arguments
    if len(sys.argv) > 2 and  os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        origin = sys.argv[1]
        dest = sys.argv[2]
        print(origin + "\n" + dest)
    #If user runs normally files are chosen through UI
    else:        
        user_input = asyncio.run(great_user())   #Returns tuple(origin, destination, settings)
        origin = user_input[0]     
        dest = user_input[1]       

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
main()