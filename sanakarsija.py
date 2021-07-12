file1 = open("kaikkisanat.txt", "r")
file2 = open("kaikkisanatkarsittu.txt", "w")



print("Poistetaan kaikki sanat, joissa on enemmän kuin 7 kirjainta...")
for word in file1:
    if len(word) > 3:
        if len(set(word[:-1])) < 8:
            file2.write(word)

print("Kaikki valmista")
