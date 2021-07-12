def scoring(guess):
    #4 kirjainta = 1p
    #5 kirjainta = 4p
    #6 kirjainta = 6p
    #7 kirjainta = 7p
    #8 kirjaimen pangram = 15p
    #9 kirjaimen pangram = 16p eli pangram 7p bonus
    if len(guess) == 4:
        return 1
    elif len(guess) == 5:
        return 4
    else:
        return len(guess)

def max_score(wordlist):
    maximum = 0
    for word in wordlist:
        maximum += scoring(word)
    return maximum