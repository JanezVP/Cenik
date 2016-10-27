# -*- coding: UTF-8 -*-

print "Pozdravljeni. Sem programcek za vnos cenika. Nisem najboljsi, pomagam pa."

cenik = {}

while True:
    jed = raw_input("Vnesite jed: ") + ", "
    cenik[jed] = raw_input("Vnesite ceno: ")+ " eur"

    print ("Hrana: " + jed + " Cena: " + cenik[jed])

    new = raw_input("Zelite dodati novo jed? (da/ne) ")

    if new == "ne":
        break

print "CENIK:"
print "Hrana " + "Cena"
for i in cenik:
    print (i + cenik[i])
