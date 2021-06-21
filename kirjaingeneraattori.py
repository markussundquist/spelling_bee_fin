from random import shuffle

Generator = False

accepted_words = ["kyllä", "jeba", "jep", "kyllä", "yes", "y", "k", "kyl"]
accepted_exits = ['e', 'ei', 'en', 'en mä', 'n', 'no']
alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyzäö']
correct_words = []
append_file = open("kirjainyhdistelmät.txt", "a+")

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



    with open("kaikkisanatkarsittu.txt", "r") as file:
        for line in file:
            wordlist.append(str(line).lower()[:-1])

    for word in wordlist:
        if mandatory in word:
            if len(word) > 3:
                if any(x in invalid_letters for x in word) == False: #Karsii sanat, jotka sisältävät muita kuin hyväksyttyjä kirjaimia
                    accepted.append(word)
    
    return accepted

def ispangram(letters, game_words):

    pangram_count = 0
    for word in game_words:
        if set(letters) - set(word) == set(): ##jos sana käyttää kaikki kirjaimet, tuloksena on tyhjä set()
            pangram_count += 1

    return pangram_count

print("-- Tämä ohjelma kerää hyväksyttyjä kirjainyhdistelmiä. \n-- Ohjelman tarkoituksena on vähentää latausaikoja.\n-- Paina ^C poistuaksesi generaattorista")
Query = True
while Query == True:
    start = input("\n\nKirjoita \"y\" aloittaaksesi: ")

    if start.lower() == "y":
        Query = False

Generator = True
i = 0
while Generator == True:

    game_letters = select_letters()
    mandatory_letter = set_mandatory(game_letters)
    game_words = create_words(game_letters, mandatory_letter)

    if len(game_words) > 12 and ispangram(game_letters, game_words) > 0 :
        game_letters_sorted = sorted(game_letters[1:])      #Nämä järjestävät kirjaimet aakkosjärjestykseen pakollista kirjainta lukuunottamatta
        game_letters_sorted.insert(0, game_letters[0])      #tarkoituksena on vähentää kahdesti esiintyviä numeroita
        game_letters_joined = ''.join(game_letters_sorted)
        game_letters_joined = game_letters_joined + "\n"
        if game_letters_joined not in append_file:
            print(f'Kirjaimet \'{game_letters}\', joista pakollinen {mandatory_letter} merkattu muistioon.')
            append_file.write(game_letters_joined)
            i += 1
    else:
        i += 1
        print(f"{i} kierrosta tehty.")
#            append_file.close()
#            append_file = open("kirjainyhdistelmät.txt", "a+")
