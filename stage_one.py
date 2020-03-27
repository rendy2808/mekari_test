def short_letter(letter):
    text = letter
    text = text.split(" ")
    short_letter = ""

    for n in text :
        short_letter += n[0]

    print(short_letter)

    return short_letter