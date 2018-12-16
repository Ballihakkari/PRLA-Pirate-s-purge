import re, os
from pathlib import Path

def name_guarantee(name, file_location):
    i = 1
    temp_name = name
    while os.path.exists(temp_name):
        i += 1
        temp_name = str(name)
        idx = temp_name.index('.')
        temp_name = Path(temp_name[:idx] + str("(" + str(i) + ")") + temp_name[idx:])

    try:
        os.rename(file_location, temp_name)
    except:
        print("ERROR: Unable to move file: " + str(file_location))    
        print("Path likly too long")    

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
        if str(series) == ".": #Unable to extract series name
            misc_dir = destination / Path("Miscellaneous")
            if not misc_dir.is_dir():
                Path(misc_dir).mkdir(parents=True, exist_ok=True)
            name_guarantee(misc_dir /file_name, file_location)
        else:
            tv_dir = destination / Path("TV Shows") / series / season
            if not tv_dir.is_dir():
                Path(tv_dir).mkdir(parents=True, exist_ok=True)
            name_guarantee(tv_dir / file_name, file_location)
    elif movie_regex.search(file_name):
        movies_dir = destination / Path("Movies")
        if not movies_dir.is_dir():
            Path(movies_dir).mkdir(parents=True, exist_ok=True)
        name_guarantee(movies_dir / file_name, file_location)
    else:
        misc_dir = destination / Path("Miscellaneous")
        if not misc_dir.is_dir():
            Path(misc_dir).mkdir(parents=True, exist_ok=True)
        name_guarantee(misc_dir / file_name, file_location)
    return None