# Lösung Folgeaufgabe:
w = input("Wort: ").lower()
v = sum(c in "aeiou" for c in w)
k = sum(c.isalpha() and c not in "aeiou" for c in w)
print("Vokale:", v, "Konsonanten:", k)