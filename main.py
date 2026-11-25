from analyseur_syntaxique import AnalyseurSyntaxique

def main():

    expression = input("Donner une expression reguliere : ")

    try:
        analyseur = AnalyseurSyntaxique(expression)
        automate = analyseur.analyser()

        print("Expression valide")
        print("Etat initial :", automate.initial)
        print("Etat final :", automate.final)

        print("Transitions :")

        for transition in automate.transitions:
            print(transition)

    except (SyntaxError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()