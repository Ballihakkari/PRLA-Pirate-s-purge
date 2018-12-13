#obj = tuple(series_name, season, title, settings)
#NOTE movies or misc are to be marked by having season == None
from pathlib import Path
import os

def add_file_to_dest(obj, structured_folder, file_path):
    if obj[1]:  #obj is show
        directory = structured_folder / obj[0] / obj[1]
        destination = directory / obj[2]
        if not directory.is_dir():
            Path(directory).mkdir(parents=True, exist_ok=True)
        os.rename(file_path, destination)
    else:       #obj movie or misc
        #TODO
        #Sort into 
        misc_directory = structured_folder / "Misc"
        movies_directory = structured_folder / "Movies"

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

