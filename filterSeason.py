import re
from regexfolders import regexes
from roman_to_arabic import roman_to_arabic
from extract_season_episode import extract_season_episode as extractSE
def filter_Season(j):
        has_roman = re.findall(regexes['has_roman_numbers'], j)
        j = re.sub("episode", "e", j)
        j = re.sub("season", "s", j)
        usual_format = re.search(regexes['usual_series_format'], j)
        split_on_x = re.search(regexes['series_and_episode_split_on_x'], j)
        split_on_dot = re.search(regexes['series_and_episode_split_on_dot'], j)
        Three_number_series = re.search(regexes['three_number_series_and_episodes'], j)

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