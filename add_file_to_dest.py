from pathlib import Path

def add_file_to_dest(obj, structured_file):
    directory = structured_file / obj[0] / obj[1]

    if not directory.is_dir():
        Path(directory).mkdir(parents=True, exist_ok=True)
        #print("Is not dir")
        #  file?
    else:
        Path(directory).mkdir(parents=True, exist_ok=True)
        #print("Is dir")
        #add file?


# obj0 = ("Samuri Jack", "Season 5")
# obj1 = {'show name': "Teen Titans", 'season nr': "Season 01"} #Invalid now, use tuples not dicts
# obj2 = {'show name': "Teen Titans", 'season nr': "Season 02"} #Invalid now, use tuples not dicts
# obj3 = {'show name': "Teen Titans", 'season nr': "Season 03"} #Invalid now, use tuples not dicts
# obj4 = {'show name': "Teen Titans", 'season nr': "Season 04"} #Invalid now, use tuples not dicts
# obj5 = {'show name': "Teen Titans", 'season nr': "Season 05"} #Invalid now, use tuples not dicts

# structured_file = Path(r"C:\Users\Sæmundur\Desktop\Python_hopverkefni_tests") #arbitrary local file
# add_file_to_dest(obj0, structured_file)
# add_file_to_dest(obj1, structured_file)
# add_file_to_dest(obj2, structured_file)
# add_file_to_dest(obj3, structured_file)
# add_file_to_dest(obj4, structured_file)
# add_file_to_dest(obj5, structured_file)
