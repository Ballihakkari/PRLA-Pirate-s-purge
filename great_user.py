#Greats user, asks user to select files and settings
#Returns tuple(origin, destination, settings)
from tkinter.filedialog import askdirectory
from pathlib import Path
import os, time, sys, asyncio

#async function to use have the script wait for askdirectory() 
async def wait_for_askdirectory():
    #TODO flush input
        #Ok kannski létt bail á þetta
        #Þetta er gg OS spasific
    #TODO lostna við vírusar gluggan
        #Turns out þetta er líka flókið
        #Skoða þetta seinna(ef ég nenni)
    return askdirectory()

def new_screen(origin, destination):
    os.system('cls' if os.name == 'nt' else 'clear')
    if origin:
        print("Selected the origin folder your files:\t[" + origin + "]")
    if destination:
        print("Selected destination of your files:\t[" + destination + "]")
    print("\n\n")

async def great_user():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ready to clean up your folder?")
    input("Press enter to continue...")
    
    cont = True             #Must ask for destination and origin folder once
    destination_cont = ""   # != "y", therefore will be asked at least once
    origin_cont = ""        # != "y", therefore will be asked at least once
    settings_cont = "y"     #Settings will not be automatically opened
    origin = ""             #Path to origin folder
    destination = ""        #Path to destination folder
    settings = ""           #Settings chosen
    while cont:

        #Asks user for origin folder
        while origin_cont.lower() != 'y': 
            new_screen(origin, destination)
            print("Select the folder you wish to clean up\nAfter that, press enter to continue")
            origin = await wait_for_askdirectory()
            print("\nIs this your downloads folder?\t[" + origin + "]")
            origin_cont = input("If this is your folder enter 'y': ")
        new_screen(origin, destination)

        #Asks user for destination folder
        while destination_cont.lower() != 'y':
            new_screen(origin, destination)
            print("Select the destination of your files\nAfter that, press enter to continue")
            destination = await  wait_for_askdirectory()
            print("\nIs this your destination folder?\t[" + destination + "]")
            destination_cont = input("If this is your folder enter 'y': ")

        #Overview and confermation before exicution
        print("\n\n\n\n\nTo change the origin folder of your files enter 'o'")
        print("To change the destination folder of your files enter 'd'")
        print("To change settings enter 's'")
        exicute = input("To exicute the script input anything else: ")
        
        #Determine if user wants to alter folders or settings before exicution
        if exicute.lower() == 'o':
            origin_cont = ""
        elif exicute.lower() == 'd':
            destination_cont = ""
        else:
            cont = False
            
    os.system('cls' if os.name == 'nt' else 'clear')
    return(origin, destination, settings)

#print(asyncio.run(great_user()))