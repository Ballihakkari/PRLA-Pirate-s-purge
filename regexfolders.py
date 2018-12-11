regexes = {
    'usual_Series_Format' : '[sS]\d{1,2}[eE ]+\d',
    'series/Episode_Split_On_x' : '\d{1,2}x\d',
    'series/Episode_Split_On_dot' : '\[\d{1,2}\.\d{1,2}\]',
    'three_number_series/Episodes' : '([ \.\-_,]|^)\d{3}($|[ \.\-_,abc])',
    'season_In_Name' : '[sS][eE][aA][sS][Oo][nN][ \.,_\-](\d|I|II|III|IV|V|VI|VII|VIII|IX|X){1,2}',
    'StartsWithSeason' : '^[sS]\d{1,2}'
}