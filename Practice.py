def create_strings_from_characters(frequencies, string1, string2):
    number = 2
    dict1 = {}
    dict2 = {}
    for letter in string1:
        dict1[letter] = dict1.get(letter,0) + 1
    for letter in string2:
        dict2[letter] = dict2.get(letter,0) + 1
    


    
    
frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

create_strings_from_characters(frequencies, string1, string2)
