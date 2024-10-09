#programme pour connaitre le prenom, l'age, et s'il est etudiant
prenom=input("Comment vous appelez-vous ?")
age=input("Quel est votre age ?")
etudiant=int(input("êtes-vous étudiant ? : 1 - Oui,  2 - Non"))
try :
    if etudiant==1 :
        print("Cette personne s'appelle " + prenom + " Elle a" + age + " et elle est étudiante")
    else :
        print("Cette personne s'appelle " + prenom + " Elle a" + age + " et elle n'est pas étudiante")
except ValueError :
    print("Vous auriez du répondre par 1 ou2 répondre par 1 ou 2")