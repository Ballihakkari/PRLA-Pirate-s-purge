import re
from regex_folders import regexes
from roman_to_arabic import roman_to_arabic
from extract_season_episode import extract_season_episode as extractSE
def filter_season(j):
    has_roman = re.findall(regexes['has_roman_numbers'], j)
    #Has roman returns a list of stringsif matched
    #All others return a string
    usual_format = re.search(regexes['usual_series_format'], j) 
    split_on_x = re.search(regexes['series_and_episode_split_on_x'], j)
    split_on_dot = re.search(regexes['series_and_episode_split_on_dot'], j)
    Three_number_series = re.search(regexes['three_number_series_and_episodes'], j)
    #We might match more than one but we go into the if statements in order of importance/likelihood of correct match
    if usual_format:
        return extractSE(usual_format.group())
    elif split_on_x:
        return extractSE(split_on_x.group())
    elif split_on_dot:
        return extractSE(split_on_dot.group())
    elif Three_number_series:
        return extractSE(Three_number_series.group())
    elif has_roman:
        return extractSE(has_roman)
    return None #If nothing was matched we return None