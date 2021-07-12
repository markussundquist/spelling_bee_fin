from random import choice

def terrible_optimizer():
    #Leikkaa latausaikoja (karusti) valitsemalla kirjaimet valmiista listasta. Bonuksena on se, että latausajat lyhenevät, mitä enemmän pelia pelaa (lisää myöhemmin).
    linefile = open("kirjainyhdistelmät.txt", "r")
    allText= linefile.read()
    game_lines = list(map(str, allText.split()))
    game_letters = choice(game_lines)
    mandatory_letter = game_letters[0]
    print(f'Kirjaimesi ovat \'{game_letters}\' ja näistä pakollinen kirjain on {mandatory_letter}.')
    return game_letters, mandatory_letter, False

def write_letters_to_file(game_letters): #lisää kirjaimet tekstitiedostoon, jotta latausajat vähentyisivät
    append_file = open("kirjainyhdistelmät.txt", "a+")
    game_letters_sorted = sorted(game_letters[1:])      #Nämä järjestävät kirjaimet aakkosjärjestykseen pakollista kirjainta lukuunottamatta
    game_letters_sorted.insert(0, game_letters[0])      #tarkoituksena on vähentää kahdesti esiintyviä numeroita
    game_letters_joined = ''.join(game_letters_sorted)
    game_letters_joined = game_letters_joined + "\n"
    if game_letters_joined not in append_file:
        append_file.write(game_letters_joined)
    append_file.close()

def loading_cut_off():
    i = 0
    count_rows = open("kirjainyhdistelmät.txt", "r")
    for row in count_rows:
        i += 1
    return (i/80)

if __name__ == '__main__':
    print(loading_cut_off())