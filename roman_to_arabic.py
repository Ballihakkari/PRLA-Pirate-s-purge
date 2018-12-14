def roman_to_arabic(roman_number):
    roman_val = {'I' : 1, #Dictionary where they key is the roman number
                 'V' : 5, #And the value is the corresponding value in the arabic base 10 system
                 'X' : 10,
                 'L' : 50,
                 'C' : 100,
                 'D' : 500,
                 'M' : 1000}
    sumofall = 0
    sumofdoubles = 0
    for n,i in enumerate(roman_number):
        try:
            if roman_val[i] < roman_val[roman_number[n+1]]:
                sumofall -= roman_val[i]
                sumofdoubles
            else:
                sumofall += roman_val[i]
        except IndexError:
            sumofall += roman_val[i]
    return sumofall