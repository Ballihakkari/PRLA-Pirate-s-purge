regexes = {
    # Finding Season/Episodes from title/subfolders
    'usual_series_format' : '[sS]\d{1,2}[eE ]+\d{1,2}',
    'series_and_episode_split_on_x' : '\d{1,2}x\d{1,2}',
    'series_and_episode_split_on_dot' : '\[\d{1,2}\.\d{1,2}\]',
    'three_number_series_and_episodes' : '([ \.\-_,]|^)d{3,4}($|[ \.\-_,abc])',
    'season_in_name' : '[sS][eE][aA][sS][Oo][nN][ \.,_\-](\d|I|II|III|IV|V|VI|VII|VIII|IX|X){1,2}',
    'starts_with_season' : '^[sS]\d{1,2}',
    '4digits_not_brackets' : '[^\(\d]\d{3}[^\)\d]',
    # Removing redundant URL from title
    'url_detector' : 'www\..+\.[A-Za-z]{2}\.?[A-Za-z]{1,3}',
    # Finding sample files
    'sample' : '[Ss][Aa][Mm][Pp][Ll][Ee]',
    'num_no_space' : '^[^Ss]\d+[^ ]',
    'realease_year' : '\(\d{4}\)'
}
