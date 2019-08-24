def is_pangram(sentence):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sentencearray=[]
    rarr=[]
    for word in sentence.split():
        for letter in word:
                    sentencearray.append(letter.lower())
    for letter in alpha:
        if letter in sentencearray:
            rarr.append('True')
        else:
            rarr.append('False')
    if "False" in rarr:
        return False
    else:
        return True
    


