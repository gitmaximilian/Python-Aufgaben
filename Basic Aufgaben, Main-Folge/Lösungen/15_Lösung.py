# Lösung Hauptaufgabe:
w = input("Wort: ").lower()
print(sum(c in "aeiou" for c in w))