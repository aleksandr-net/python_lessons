#!/usr/bin/python3.5

# Odnostrochniy commentariy

"""
Mnogostrochniy
commentariy
"""

is_student = True
name = input('Insert name: ')

print('Hello, ', name, '!')

# Chto takoe tip dannyh?

# Skalyarnie tipy dannyh:

# bool - logicheskie (True, False)

# int - celochislennie
i1 = 666 # desyatirichnaya
i2 = 0x59F # shestnadcatirichnaya sistema schosleniya
i3 = 0b11 # dvoichnaya SS
i4 = 0o255 # vosmerichnaya

# float - s plavauschey tochkoy (drobnie)
f1 = 1.23
f2 = 12e-3 # 12 * 10^-3
f3 = 12e3 # 12 * 10^3

# str - strokovoy
s1 = 'Some string' # Predpochtitelniy sposob
s2 = "Some \" string" # Stroka s ekranirovaniem
s3 = r'Raw string' # Syrie stroki
s4 = u'Hello' # Unicodnaya stroka (dlya sovmestimosti s python2)
s5 = b'Baytovaya stroka'
s6 = '''Mnogostrochnaya
stroka
raz
'''
s7 = """Mnogostrochnaya
stroka
dva
"""

# Kompleksnye chisla - complex
c1 = 3.14j


# Strukturirovannye peremennye (slojnye)
# tuple, list, set, dict, object

# Korteji - tuple
t1 = (1,) # kortej iz odnogo elementa - zapyataya obyazatelna!
t2 = (True, 61, 1.2, 'String', (1, 2, 3)) # MNOGO ZNACHENIT RAZNOGO TIPA

# Spiski - list
lst1 = [[1], [2], 3, False, (1,)]

# Mnojestva - set
s1 = {1, 2, 3, 'prprpr', 3, 3, 3}
s2 = set() # pustoe mnojestvo
s3 = s1 - {1, 2}

print(t2[1], lst1[2], lst1[0][0]) # Obraschenie k elementam strukturirovannyh peremennyh
print(s3)

# Slovari - dict
d = {
    'id': 1,
    'name': 'Sasha',
    'is_student': True,
    'skills': ('python', 'linux')
}

# Specialnye tipy dannyh
# None - pustota

a = None

