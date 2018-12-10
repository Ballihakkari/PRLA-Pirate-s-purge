#Supports all file names with it's season and episode formated as:
#[s01e01], #[s1e1], [1x01], [01x01] (Not case sensitive)
#Returns season and episode of file formated as:
#('01', '01')
import re
def extract_season_episode(s):
    x = re.search(r'[sS]?\d{1,2}[eEx]\d{1,2}', s)
    if x:
        x = x.group(0).upper()
        if 'X' in x:
            y = x.split("X")
        else:
            y = x.split("E")
        y[0] = y[0].replace("S", "")
        if len(y[0]) == 1:
            y[0] = '0' + y[0]
        
        if len(y[1]) == 1:
            y[1] = '0' + y[1]
        
        return tuple(y)

# s = """Brooklyn.Nine-Nine.S03E04.INTERNAL.XviD-AFG.avi
# Buffy S01E01 - Welcome to the Hellmouth.avi
# Burlesque.Isltexti.2010(DvDrip)X264 - Skari11.mkv
# Come Dine with Me s28e52 Zac.avi
# Come Dine with Me s28e24 Jan Leeming.avi
# Come Dine With Me S25E115.avi
# Community.S01E14.HDTV.XviD-2HD.avi
# derren.brown.the.experiments.s01e03.ws.pdtv.xvid-c4tv.avi
# Once.Upon.a.Time..S04E03.HDTV.x264-ChameE.mkv
# downton_abbey.3x08.hdtv_x264-fov.mp4
# dexter.609.hdtv-lol.avi
# Hells.Kitchen.US.S10E01.PDTV.x264-LOL.mp4
# house.805.hdtv-lol.avi
# Its.Always.Sunny.in.Philadelphia.S07E07.HDTV.XviD-ASAP.avi
# It's Always Sunny In Philadelphia - 106 - The Gang Finds a Dead Guy.avi
# Brooklyn 99 S02E01 HDTV.XviD-AFG.avi
# 90210 s1e33 - KrummiferAðVeiða
# S06E23-24 - Shutout In Seattle.avi
# 24 Backstage Pass.avi
# the-happening-1983-s3e9"""
# s = s.split('\n')
# for i in s:
#     print(extract_season_episode(i))