# Größere Zahl finden oder Gleichheit prüfen
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))

if zahl1 > zahl2:
    print("Die größere Zahl ist:", zahl1)
elif zahl2 > zahl1:
    print("Die größere Zahl ist:", zahl2)
else:
    print("Beide Zahlen sind gleich.")