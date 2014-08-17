import random
import colorama

envanter = {
    "Sticker Angular.js": 1,
    "Sticker Kodio": 5,
    "Sticker Atom Uzun": 3,
    "Sticker Atom Buyuk": 1,
    "Tshirt Kodio": 2,
    "Tshirt Coding Contest": 1,
    "Tshirt Codefront": 1,
    "Tshirt Github": 1
}

people = open("data.txt").readlines()

for item, total in envanter.items():
    print colorama.Fore.GREEN + colorama.Style.BRIGHT, item
    selected_people = random.sample(people, total)
    for person in selected_people:
        people.remove(person)
        print colorama.Fore.RED + colorama.Style.BRIGHT + "  -", person.strip()
