def create_strings_from_characters(frequencies, string1, string2):
    number = 2
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for letter in string1:
        dict1[letter] = dict1.get(letter,0) + 1
        dict3[letter] = dict3.get(letter,0) + 1
    for keys in dict1:
        if len(frequencies) == 0 and len(dict1) > 0:
            number = 0
            break
        elif frequencies[keys] < dict1[keys]:
            print(f"Not enought '{keys}' in string1")
            number -= 1
            break
        elif frequencies[keys] > dict3[keys]:
            frequencies[keys] = dict3.get(letter,0) - 1
            print(frequencies)
    for letter in string2:
        dict2[letter] = dict2.get(letter,0) + 1
        dict3[letter] = dict3.get(letter,0) + 1
    print(dict3)
    for keys in dict2:
        if len(frequencies) == 0:
            break
        elif len(frequencies) > 0 and frequencies[keys] < dict2[keys]:
            print(f"Not enought '{keys}' in string2")
            number -= 1
            break
    
    return(number)
    
    
frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

create_strings_from_characters(frequencies, string1, string2)
