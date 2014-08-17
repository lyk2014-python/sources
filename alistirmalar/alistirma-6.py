# -*- coding: utf-8 -*-

meyveler = ["elma", "armut", "visne", "muz", "portakal"]

print meyveler[0] # 'elma'

print meyveler[-1] # 'portakal'

print meyveler[-2:] # ['muz', 'portakal']

print meyveler[::-1]

print len(meyveler) # 5

meyveler.append("visne")

print meyveler

print meyveler.count("visne") # 2

meyveler.insert(0, "armut")

print meyveler

print meyveler.pop(0)

print meyveler

meyveler.remove("muz")

print meyveler

del meyveler[0]

print meyveler

meyveler.sort()

print meyveler

meyveler.reverse()

print meyveler




