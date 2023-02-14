def create_strings_from_characters(frequencies, string1, string2):
    number = 2
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for letter in frequencies:
        dict1[letter] = frequencies[letter]
        dict2[letter] = frequencies[letter]
        dict3[letter] = frequencies[letter]
       
    for letter in string1:
        dict1[letter] = dict1.get(letter,0) - 1
        if dict1[letter] < 0:
            number -= 1
            break

    for letter in string2:
        dict2[letter] = dict2.get(letter,0) - 1
        if dict2[letter] < 0:
            number -= 1   
            break
    
    for letter in string1 + string2:
        dict3[letter] = dict3.get(letter,0) - 1
        if dict3[letter] < 0 and number == 2:
            number -= 1

    print(number)
            
    
frequencies = {"a": 1}
string1 = ""
string2 = ""

create_strings_from_characters(frequencies, string1, string2)
