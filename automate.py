class Automate:

    def __init__(self, initial, final, transitions):
        self.initial = initial
        self.final = final
        self.transitions = transitions

    def exporter_dot(self, fichier):

        groupes = {}

        # Regrouper les transitions paralleles
        for source, symbole, destination in self.transitions:

            cle = (source, destination)

            if cle not in groupes:
                groupes[cle] = []

            groupes[cle].append(symbole)

        # Ouvrir le fichier
        f = open(fichier, "w", encoding="utf-8")

        f.write("digraph AFN {\n")
        f.write("rankdir=LR;\n")
        f.write("node [shape=circle];\n")

        # Etat initial
        f.write("__start [shape=point];\n")
        f.write(f"__start -> {self.initial};\n")

        # Etat final
        f.write(f"{self.final} [shape=doublecircle];\n")

        # Ecrire les transitions
        for cle in groupes:

            source = cle[0]
            destination = cle[1]

            etiquette = ",".join(groupes[cle])

            f.write(f'{source} -> {destination} [label="{etiquette}"];\n')

        f.write("}\n")

        f.close()
class Thompson:

    # Construction d'un symbole
    def symbole(self, c, num):

        debut = num
        fin = num + 1

        transitions = [(debut, c, fin)]

        return Automate(debut, fin, transitions)

    # Construction du mot vide
    def mot_vide(self, num):

        debut = num
        fin = num + 1

        transitions = [(debut, "ε", fin)]

        return Automate(debut, fin, transitions)

    # Concatenation
    def concatener(self, a, b):

        transitions = a.transitions + b.transitions

        transitions.append((a.final, "ε", b.initial))

        return Automate(a.initial, b.final, transitions)

    # Union
    def union(self, a, b, num):

        debut = num
        fin = num + 1

        transitions = a.transitions + b.transitions

        transitions.append((debut, "ε", a.initial))
        transitions.append((debut, "ε", b.initial))
        transitions.append((a.final, "ε", fin))
        transitions.append((b.final, "ε", fin))

        return Automate(debut, fin, transitions)

    # Etoile de Kleene
    def etoile(self, a, num):

        debut = num
        fin = num + 1

        transitions = a.transitions.copy()

        transitions.append((debut, "ε", a.initial))
        transitions.append((debut, "ε", fin))
        transitions.append((a.final, "ε", a.initial))
        transitions.append((a.final, "ε", fin))

        return Automate(debut, fin, transitions)

    # Operateur plus
    def plus(self, a, num):

        debut = num
        fin = num + 1

        transitions = a.transitions.copy()

        transitions.append((debut, "ε", a.initial))
        transitions.append((a.final, "ε", a.initial))
        transitions.append((a.final, "ε", fin))

        return Automate(debut, fin, transitions)

    # Operateur optionnel
    def optionnel(self, a, num):

        debut = num
        fin = num + 1

        transitions = a.transitions.copy()

        transitions.append((debut, "ε", a.initial))
        transitions.append((debut, "ε", fin))
        transitions.append((a.final, "ε", fin))

        return Automate(debut, fin, transitions)
