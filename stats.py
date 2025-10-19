def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = {}
    for letter in text:
        l = letter.lower()
        if l in char_count:
            char_count[l] += 1
        else:
            char_count[l] = 1
    return char_count    

def get_list_dict(dictionary):
    list_of_dicts = []
    for key in dictionary:
        if key.isalpha():
            list_of_dicts.append({'char': key, 'num': dictionary[key]})
    return list_of_dicts
