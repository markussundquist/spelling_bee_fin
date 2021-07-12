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