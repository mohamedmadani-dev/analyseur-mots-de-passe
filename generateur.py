from random import choice
import string

def generer_mdp():

    caracteres = string.ascii_letters + string.digits + "!@#$%&*?"

    while True:
        mdp = ""

        for i in range(12):
            mdp += choice(caracteres)

        if (any(c.isupper() for c in mdp)
            and any(c.islower() for c in mdp)
            and any(c.isdigit() for c in mdp)
            and any(c in "!@#$%&*?" for c in mdp)):

            return mdp
