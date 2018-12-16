#Supports all file names with it's season and episode formated as:
#[s01e01], #[s1e1], [1x01], [01x01] (Not case sensitive)
#Returns season and episode of file formated as:
#('01', '01')
import re
from regexfolders import regexes
from roman_to_arabic import roman_to_arabic
def extract_season_episode(input):
    y = []
    print(input)
    if type(input) != str:
        for n,i in enumerate(input):
            if not i[1].isdigit():
                y.append(str(roman_to_arabic(i[1])))
            else:
                y.append(str(i[1]))
            input[n] = " ".join(i)
        input = " ".join(input)
    else:
        s = input
        s = str(s).lower()
        s = re.sub(" ", "", s)
        if 'e' in s:
            y = s.split("e")
            y[0] = y[0].replace("s", "")
        elif 'x' in s:
            y = s.split("x")
        elif re.search(regexes['series_and_episode_split_on_dot'], s):
            y = s[1:-1].split('.')
        else:
            if re.search(r'\d{4}', s):
                x = re.search(r'\d{4}',s).group()
                y.append(x[0:2])
                y.append(x[2:])
            elif len(s) == 3:
                y.append(s[0])
                y.append(s[1:])
            elif len(s) == 4:
                if s[0].isdigit():
                    y.append(s[0])
                    y.append(s[1:-1])
                else:
                    y.append(s[1])
                    y.append(s[2:])
            else:
                y.append(s[1])
                y.append(s[2:-1])
    for i in range(len(y)):
        if len(y[i]) == 1:
            y[i] = '0' + y[i]
    if len(y) >= 2:
        return(y,input)
    else: 
        return None