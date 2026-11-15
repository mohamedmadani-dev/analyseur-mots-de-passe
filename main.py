
from generateur import generer_mdp

print("\n======================================")
print("       BIENVENUE DANS MON PROGRAMME")
print("          Analyseur de mots de passe")
print("======================================")

while True:

    print("\nQue souhaitez-vous faire ?")
    print("1 - Verifier un mot de passe")
    print("2 - Generer un mot de passe")
    print("3 - Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":

        mdp = input("\nEntrez votre mot de passe : ")

        if mdp == "":
            print("Vous n'avez pas entre de mot de passe.")
            continue

        with open("mots_courants.txt", "r") as fichier:
            liste_mdp = fichier.read().splitlines()

        if mdp.lower() in liste_mdp:
            print("\nAttention ! Ce mot de passe est tres courant.")
            print("Je vous conseille d'en choisir un autre.")
            continue

        score = 0
        conseils = []

        if len(mdp) >= 8:
            score += 1
        else:
            conseils.append("Utilisez au moins 8 caracteres.")

        if any(c.isupper() for c in mdp):
            score += 1
        else:
            conseils.append("Ajoutez une lettre majuscule.")

        if any(c.islower() for c in mdp):
            score += 1
        else:
            conseils.append("Ajoutez une lettre minuscule.")

        if any(c.isdigit() for c in mdp):
            score += 1
        else:
            conseils.append("Ajoutez au moins un chiffre.")

        caracteres = "!@#$%^&*()-_+=?"

        if any(c in caracteres for c in mdp):
            score += 1
        else:
            conseils.append("Ajoutez un caractere special.")

        print("\n----------- RESULTAT -----------")
        print("Score :", score, "/ 5")

        if score == 5:
            print("Excellent ! Votre mot de passe est solide.")
        elif score >= 3:
            print("Pas mal, mais votre mot de passe peut etre ameliore.")
        else:
            print("Votre mot de passe est trop faible.")

        if conseils:
            print("\nVoici quelques conseils :")

            for conseil in conseils:
                print("- " + conseil)

    elif choix == "2":

        nouveau_mdp = generer_mdp()

        print("\nVoici un mot de passe genere pour vous :")
        print(nouveau_mdp)

        print("\nPensez a le conserver dans un endroit securise.")

    elif choix == "3":

        print("\nMerci d'avoir utilise mon programme. A bientot !")
        break

    else:
        print("\nJe n'ai pas compris votre choix. Reessayez.")
