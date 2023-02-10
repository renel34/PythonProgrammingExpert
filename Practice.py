def create_strings_from_characters(frequencies, string1, string2):
    number = 2
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for letter in frequencies:
        dict1[letter] = frequencies[letter]
        dict2[letter] = frequencies[letter]
        #dict3[letter] = frequencies[letter]
       
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
        dict3[letter] = dict3.get(letter,0) + 1
            

    print(dict1)
    print(dict2)
    print(dict3)
    print(number)
            
    
frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

create_strings_from_characters(frequencies, string1, string2)
