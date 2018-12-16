def roman_to_arabic(roman_number):
    roman_val = {'I' : 1, #Dictionary where they key is the roman number
                 'V' : 5, #And the value is the corresponding value in the arabic base 10 system
                 'X' : 10,
                 'L' : 50,
                 'C' : 100,
                 'D' : 500,
                 'M' : 1000}
    sumofall = 0
    for n,i in enumerate(roman_number):
        try:
            if roman_val[i] < roman_val[roman_number[n+1]]: #if the next number is larger than the current number we subract the current number from the sum
                sumofall -= roman_val[i]
            else:                                           #else we add it to the sum
                sumofall += roman_val[i]
        except IndexError:#This happens when we compare the last number of the list to the current number 
            sumofall += roman_val[i] 
    return sumofall