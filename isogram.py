def is_isogram(string):
    letters_list=[]
    for letter in string:
        if letter == '-' or letter== ' ':
            pass
        else:
            letters_list.append(letter.lower())
    no_of_letters_in_str=len(letters_list)
    no_of_letters_in_set=len(set(letters_list))
    if no_of_letters_in_str == no_of_letters_in_set:
        return True
    else:
        return False
