#Supports all file names with it's season and episode formated as:
#[s01e01], #[s1e1], [1x01], [01x01] (Not case sensitive)
#Returns season and episode of file formated as:
#('01', '01')
import re
from regexfolders import regexes
from roman_to_arabic import roman_to_arabic
def extract_season_episode(input):
    y = []
    if type(input) != str: #If the input is not a string then it is a list
        for n,i in enumerate(input):#only input that is not a string is if it includes roman numerals or has Season/Episode instead of S and E
            if not i[1].isdigit(): #if the latter number not a digit ( The prior will always be the string Season/Episode) then we know it is a roman numeral
                y.append(str(roman_to_arabic(i[1]))) #We convert it to arabic base 10
            else:
                y.append(str(i[1])) #Else it is a decimal and we append it
            input[n] = " ".join(i) 
        input = " ".join(input)
    else: #Now it is a string
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
        else: #here we are extracting the Season and episode count from the input string
              #into the format ( SeasonNumber, EpisodeNumber ) 
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
        return(y,input) #Here we return a tuple where the first element is a tuple (X, Y, Z, P) latter is the input
    else: 
        return None