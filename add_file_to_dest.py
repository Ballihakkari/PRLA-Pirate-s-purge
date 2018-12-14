import re
from pathlib import Path
import os

def name_guarantee(name):
    i = 1
    temp_name = name
    while os.path.exists(temp_name):
        i += 1
        temp_name = name
        temp_name / Path("(" + str(i) + ")")
    return temp_name
        

#file_info(path_part1/path_part2/path_part3/path_part4/.../new_name)
def add_file_to_dest(file_info, origin, destination):
    file_location = Path(origin)
    file_name = file_info[-1]
    for n in range(len(file_info) - 1):  #-1 since the last index is new file name
        file_location = file_location / Path(file_info[n])
    
    show_regex = re.compile(r'(S\d{2}E\d{2})')
    movie_regex = re.compile(r'\(\d{4}\)')
    
    if show_regex.search(file_name):
        series = Path((str((re.search(r'[^(S\d{2}E\d{2})]*', file_name).group(0))).strip()))
        season = Path(("Season " + str(re.search(r'(?<=S)(\d{2})', file_name).group(0))).strip())
        target_dir = destination / Path("TV Shows") / series / season
        if not target_dir.is_dir():
            Path(target_dir).mkdir(parents=True, exist_ok=True)
        #TODO laga error "FileExistsError: [WinError 183] Cannot create a file when that file already exists:"
        file_name = name_guarantee(file_name)
        os.rename(file_location, target_dir / file_name)

    elif movie_regex.search(file_name):
        movies_dir = destination / Path("Movies")
        if not movies_dir.is_dir():
            Path(movies_dir).mkdir(parents=True, exist_ok=True)
        file_name = name_guarantee(file_name)
        os.rename(file_location, movies_dir / file_name)

    else:
        misc_dir = destination / Path("Miscellaneous")
        if not misc_dir.is_dir():
            Path(misc_dir).mkdir(parents=True, exist_ok=True)
        file_name = name_guarantee(file_name)
        os.rename(file_location, misc_dir / file_name)
    return None

#Demo 
#NOTE: uses local files, will need to be altered before using. Must also make files that you want moved e.g SamuraiJack_BADTEXT_s4_e6.txt

# obj1 = ("Samurai Jack", "Season 1", "Samurai Jack Season 1 Episode 1 The Beginning")
# obj2 = ("Samurai Jack", "Season 2", "Samurai Jack Season 2 Episode 1 Aku Strikes Back")
# obj3 = ("Samurai Jack", "Season 3", "Samurai Jack Season 3 Episode 1 Who's Sword is it Anyways?")
# obj4 = ("Samurai Jack", "Season 4", "Samurai Jack Season 4 Episode 1 They're not Pajamas!")
# obj5 = ("Samurai Jack", "Season 5", "Samurai Jack Season 5 Episode 1 This is The Beginning of The End")

# file_path1 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s4_e6.txt")
# file_path2 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s1_e1.txt")
# file_path3 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s2_e1.txt")
# file_path4 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s3_e1.txt")
# file_path5 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s4_e1.txt")
# file_path6 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s5_e1.txt")
# file_path7 = Path(r"C:\Users\Sæmundur\Desktop\Pirate-s-purge\SamuraiJack_BADTEXT_s2_e6.txt")

# structured_folder = Path(r"C:\Users\Sæmundur\Desktop\Python_hopverkefni_tests") #Placeholder for destination path


# add_file_to_dest(obj4, structured_folder, file_path1,)
# add_file_to_dest(obj1, structured_folder, file_path2,)
# add_file_to_dest(obj2, structured_folder, file_path3,)
# add_file_to_dest(obj3, structured_folder, file_path4,)
# add_file_to_dest(obj4, structured_folder, file_path5,)
# add_file_to_dest(obj5, structured_folder, file_path6,)
# add_file_to_dest(obj2, structured_folder, file_path7,)

