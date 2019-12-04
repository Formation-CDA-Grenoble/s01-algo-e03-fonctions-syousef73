def double(number):
    # Début de ton code
    double = 2*number
    # Fin de ton code
    return double


# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -6),
)

for test in tests:
    print(f"L'appel  double({test[0]})  renvoie: {double(test[0])} (résultat attendu: {test[1]})")
