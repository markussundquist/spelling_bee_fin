from TidyPackage.wordcreate import select_letters, set_mandatory, create_words
from TidyPackage.pangram import ispangram, pangram_check
from TidyPackage.scoring import scoring, max_score
from TidyPackage.filewrite import terrible_optimizer, write_letters_to_file, loading_cut_off


playing = False
counter = True
query = True
accepted_words = ["kyllä", "jeba", "jep", "kyllä", "yes", "y", "k", "kyl"]
accepted_exits = ['e', 'ei', 'en', 'en mä', 'n', 'no']
correct_words = []
score = 0



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
i = 0 ## Tämän tarkoituksena on vähentää latausaikoja. Jos i ylittää 200:n arvon, peli valitsee kirjaimet valmiista listasta.
cut_off = loading_cut_off()
while playing == True:

    #valitsee aakkosista satunnaisesti 7 kirjainta ja niistä pakollisen kirjaimen
    while counter == True:

        game_letters = select_letters()
        print("\n"*200)
        print(f'{i}/100% Kerätään sanoja. Tässä saattaa kestää hetki!')
        mandatory_letter = set_mandatory(game_letters)
        game_words = create_words(game_letters, mandatory_letter)
        i += 1

        if len(game_words) > 12 and ispangram(game_letters, game_words) > 0: #pitää huolen, että arvattavia sanoja on vähintään 10 ja sisältää vähintään yhden pangramin
            print(f'Kirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.\nMaksimipistemäärä on {max_score(game_words)}p.')
            write_letters_to_file(game_letters)
            counter = False

        elif i > (200 - cut_off): #latausaika liian suuri
            game_letters, mandatory_letter, counter = terrible_optimizer()
            game_words = create_words(game_letters, mandatory_letter)
            print(f'Maksimipistemäärä on {max_score(game_words)}p.')
    

##Pelin alku
    guess = input("Kirjoita tähän vastauksesi: ").lower()
    print("\n"*200)

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
        print(f"Vastaus \"{guess}\" on väärin")


    print(f'\nKirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.')

print("Kiitos, kun pelasit")