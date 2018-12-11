regexes = {
    'usual_Series_Format' : '[sS]\d{1,2}[eE ]+\d',
    'series_and_episode_split_on_x' : '\d{1,2}x\d',
    'series_and_episode_split_on_dot' : '\[\d{1,2}\.\d{1,2}\]',
    'three_number_series/Episodes' : '([ \.\-_,]|^)\d{3}($|[ \.\-_,abc])',
    'season_in_name' : '[sS][eE][aA][sS][Oo][nN][ \.,_\-](\d|I|II|III|IV|V|VI|VII|VIII|IX|X){1,2}',
    'starts_sith_season' : '^[sS]\d{1,2}',
    'url_detector' : 'www\..+\.[A-Za-z]{2,3}\.?[A-Za-z]{1,3}'
}