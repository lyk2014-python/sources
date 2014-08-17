sozluk = {
    "apple": "elma",
    "orange": "portakal",
    "pen": "kalem",
    "computer": "bilgisayar"
}

print sozluk

sozluk["water"] = "su"

print sozluk

del sozluk["computer"]

print sozluk

if "pen" in sozluk:
    print "pen kelimesi sozlukte var."

print sozluk.get("computer", "(yok)")

for kelime, anlami in sozluk.items():
    print "%s kelimesinin anlami: %s" % (kelime, anlami)

print sozluk.keys()
print sozluk.values()
