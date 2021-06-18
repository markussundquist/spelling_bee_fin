from random import shuffle, choice

playing = False
counter = True
query = True
accepted_words = ["kyllä", "jeba", "jep", "kyllä", "yes", "y", "k", "kyl"]
accepted_exits = ['e', 'ei', 'en', 'en mä', 'n', 'no']
alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyzäö']
correct_words = []
score, good_start, moving_up, good, solid, nice, great, amazing, genius, queen_bee = 0, 0, 0, 0, 0, 0, 0 ,0 , 0, 0

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

def ispangram(letters, game_words):

    pangram_count = 0
    if len(game_words) > 1:
        for word in game_words:
            if set(letters) - set(word) == set(): ##jos sana käyttää kaikki kirjaimet, tuloksena on tyhjä set(). Tarkastaa pangramit pelilautaa rakentaessa.
                pangram_count += 1
    return pangram_count

def pangram_check(letters, guess):
    if set(letters) - set(guess) == set(): ##Tämä tarkistaa vastauksen pangramin varalta
        return 7
    else:
        return 0

def terrible_optimizer():
    #Leikkaa latausaikoja (karusti) valitsemalla kirjaimet valmiista listasta. Bonuksena on se, että latausajat lyhenevät, mitä enemmän pelia pelaa (lisää myöhemmin).
    linefile = open("kirjainyhdistelmät.txt", "r")
    allText= linefile.read()
    game_lines = list(map(str, allText.split()))
    game_letters = choice(game_lines)
    mandatory_letter = game_letters[0]
    print(f'Kirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.')
    return game_letters, mandatory_letter, False

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

def write_letters_to_file(game_letters): #lisää kirjaimet tekstitiedostoon, jotta latausajat vähentyisivät
    append_file = open("kirjainyhdistelmät.txt", "a+")
    game_letters_joined = ''.join(game_letters)
    game_letters_joined = game_letters_joined + "\n"
    if game_letters_joined not in append_file:
        append_file.write(game_letters_joined)
    append_file.close()

def create_rankings(scoring): #Luo sijoittumiselle eri nimet
    if scoring % 2 != 0:
        queen_bee = (scoring-1)
    else:
        queen_bee = scoring
    return (queen_bee/50), (queen_bee*0.075), (queen_bee*0.1),  (queen_bee*0.2), (queen_bee*0.3), (queen_bee*0.4), (queen_bee*0.5), (queen_bee*0.75), queen_bee  

    








########################################################################################################
while query == True:

    start_game = input("Tervetuloa pelaamaan \"spelling bee\" -peliä! Haluatko aloittaa pelin? ")

    if start_game.lower() in accepted_words:
        playing = True
        break
    elif start_game.lower() in accepted_exits:
        break
    else:
        print("En ymmärtänyt vastausta. Vastaa muodossa kyllä tai ei.")

#Kerää pelilaudan
print("Kerätään sanoja. Tässä saattaa kestää hetki!")
i = 0 ## Tämän tarkoituksena on vähentää latausaikoja. Jos i ylittää 200:n arvon, peli valitsee kirjaimet valmiista listasta.
while playing == True:

    #valitsee aakkosista satunnaisesti 7 kirjainta ja niistä pakollisen kirjaimen
    while counter == True:

        game_letters = select_letters()
        print(f'{i}/100%')
        mandatory_letter = set_mandatory(game_letters)
        game_words = create_words(game_letters, mandatory_letter)
        i += 1

        if len(game_words) > 12 and ispangram(game_letters, game_words) > 0: #pitää huolen, että arvattavia sanoja on vähintään 10 ja sisältää vähintään yhden pangramin
            print(f'Kirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.\nMaksimipistemäärä on {max_score(game_words)}p.')
            write_letters_to_file(game_letters)
            counter = False

        elif i > 100: #latausaika liian suuri
            game_letters, mandatory_letter, counter = terrible_optimizer()
            game_words = create_words(game_letters, mandatory_letter)
            print(f'Maksimipistemäärä on {max_score(game_words)}p.')


##Pelin alku
    guess = input("Kirjoita tähän vastauksesi: ").lower()

    if guess == "exit_game":
        break
    elif guess == "enable_cheats":
        print(game_words)
    elif guess == "display_score":
        print(score)
    elif guess == "arvatut_sanat":
        print(correct_words)
    elif guess in correct_words:
        print("Olet jo arvannut tämän sanan!")
    elif mandatory_letter not in guess:
        print("Jokaisessa sanassa on oltava pakollinen kirjain!")
    elif len(guess) < 4:
        print("Vastauksien täytyy olla vähintään 4:n kirjaimen pituisia!")
    elif guess in game_words:
        score += (scoring(guess) + pangram_check(game_letters, guess))
        if pangram_check(game_letters, guess) == 7:
            print("PANGRAM!!!!!")
        print(f"Vastaus \"{guess}\" on oikein. Vastauksesi oli {scoring(guess)+pangram_check(game_letters, guess)}:n pisteen arvoinen, jolloin sinulla on yhteensä {score}/{max_score(game_words)} pistettä!")
        correct_words.append(guess)
    else:
        print(f"Vastaus {guess} on väärin")

    print(f'\nKirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.')

print("Kiitos, kun pelasit")