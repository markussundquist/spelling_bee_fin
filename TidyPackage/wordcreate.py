from random import shuffle

alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyzäö']

def select_letters():

    shuffle(alphabet)
    return alphabet[:7]


def set_mandatory(word): ##Selects the first letter as mandatory from the 7 letters

    return word[0]

def create_words(letters, mandatory):

    #kerää sanat osoitteesta https://github.com/hugovk/everyfinnishword
    wordlist = []
    accepted = []
    invalid_letters = [x for x in alphabet if x not in letters]
    invalid_markings = "-"
    invalid_letters.append(invalid_markings)
    with open("kaikkisanat.txt", "r") as file:
        for line in file:
            wordlist.append(str(line).lower()[:-1])

    for word in wordlist:
        if mandatory in word:
            if len(word) > 3:
                if any(x in invalid_letters for x in word) == False: #Karsii sanat, jotka sisältävät muita kuin hyväksyttyjä kirjaimia
                    accepted.append(word)
    
    return accepted

