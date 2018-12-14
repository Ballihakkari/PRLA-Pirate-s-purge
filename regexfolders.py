regexes = {
    # Finding Season/Episodes from title/subfolders
    'usual_series_format' : '[sS]\d{1,2}[eE ]+\d{1,2}',
    'series_and_episode_split_on_x' : '\d{1,2}x\d{1,2}',
    'series_and_episode_split_on_dot' : '\[\d{1,2}\.\d{1,2}\]',
    'three_number_series_and_episodes' : '([ \.\-_,]|^)\d{3,4}($|[ \.\-_,abc])',
    'has_roman_numbers' : '([sS][eE][aA][sS][Oo][nN]|[eE][pP][iI][sS][oO][dD][eE])[ \.,_\-]?[IVXCLDM]+',
    'roman_num' : '[IVXCLDM]'
    'starts_with_season' : '^[sS]\d{1,2}',
    # Removing redundant URL from title
    'url_detector' : 'www\..+\.[A-Za-z]{2}\.?[A-Za-z]{1,3}',
    # Finding sample files
    'sample' : '[Ss][Aa][Mm][Pp][Ll][Ee]',
    'num_no_space' : '^[^Ss]\d+[^ ]',
    'realease_year' : '\(\d{4}\)'
}
