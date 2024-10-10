def inverser_mots(phrase):
    mots = phrase.split()
    mots_inverses = mots[::-1]
    phrase_inversee = ' '.join(mots_inverses)
    return phrase_inversee
phrase_originale =input("Saisir une phrase : ")
phrase_inversee = inverser_mots(phrase_originale)
print(phrase_inversee)