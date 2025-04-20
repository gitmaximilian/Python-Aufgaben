# Zwei Zahlen – gerade oder ungerade
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))

if zahl1 % 2 == 0:
    print("Die erste Zahl ist gerade.")
else:
    print("Die erste Zahl ist ungerade.")

if zahl2 % 2 == 0:
    print("Die zweite Zahl ist gerade.")
else:
    print("Die zweite Zahl ist ungerade.")