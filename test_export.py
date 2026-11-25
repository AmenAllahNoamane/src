from automate import Automate

transitions = [
    (0, "a", 1),
    (0, "b", 1),
    (1, "ε", 2)
]

automate = Automate(0, 2, transitions)

automate.exporter_dot("test_export.dot")

print("Export termine")