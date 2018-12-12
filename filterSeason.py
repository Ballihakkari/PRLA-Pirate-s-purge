import re
from regexfolders import regexes
from extract_season_episode import extract_season_episode as extractSE
def filter_Season(i):
    for j in reversed(i):
        usual_format = re.search(regexes['usual_series_format'], j)
        split_on_x = re.search(regexes['series_and_episode_split_on_x'], j)
        if usual_format:
            print(extractSE(usual_format.group()))
            break
        elif split_on_x:
            print(extractSE(split_on_x.group()))
        elif re.search(regexes['series_and_episode_split_on_dot'], j):
            pass
        elif re.search(regexes['three_number_series_and_episodes'], j):
            pass
        
        
    #      or  or , or  or re.search(regexes['season_In_Name'],i[j]):
    #         wasadded = True
    #     if not wasadded:
    #         print(i)
    # wasadded = False
