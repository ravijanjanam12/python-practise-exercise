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
#########################################################################################################################################
#Determine if a word or phrase is an isogram.
#
#An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
#
#Examples of isograms:
#
#    lumberjacks
#    background
#    downstream
#    six-year-old
#
#The word isograms, however, is not an isogram, because the s repeats.
###########################################################################################################################################
