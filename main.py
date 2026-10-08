TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


users = {
    "bob": "123",     
    "ann": "pass123", 
    "mike": "password123",
    "liz": "pass123"
}

username = input("username:")
password = input("password:")

if username in users and users[username] == password:
    print("---------------------------------------")
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed")
    print("---------------------------------------")

else:
    print("unregistered user, terminating the program..")
    quit()

selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not selection.isdigit():
    print("Invalid input,  terminating the program..")
    quit()
selection = int(selection)
if selection < 1 or selection > len(TEXTS):
    print("Number not in range, terminating the program.. ")
    quit()

#Uživatel vybere číslo, ale v Pythonu se indexuje od 0 (index 0 = 1. text). Proto musíme odečíst:
index_textu = selection - 1
text = TEXTS[index_textu]
print("---------------------------------------")
words = text.split()
titlecase = 0
uppercase = 0
lowercase = 0
numbers = 0
numbers_sum = 0

for word in words:
    clean_word = word.strip(",.")
    if clean_word.istitle():
        titlecase += 1 
        #zkácený zápis pro: uppercase = uppercase + 1
    elif clean_word.isupper() and clean_word.isalpha():
        uppercase += 1
    elif clean_word.islower():
        lowercase += 1
    elif clean_word.isdigit():
        numbers += 1
        numbers_sum += int(clean_word)


print(f"There are {len(words)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numbers} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")
print("---------------------------------------")

word_lenghts = {}
for word in words:
    clean_word = word.strip(",.")
    lenght = len(clean_word)
    if lenght not in word_lenghts:
        word_lenghts[lenght] = 1
    else:
        word_lenghts[lenght] += 1
print("---------------------------------------")
print("LEN|  OCCURRENCES  |NR.")
print("---------------------------------------")

for lenght in sorted(word_lenghts):
    count = word_lenghts[lenght]
    stars = count * "*"
    print(F"{lenght:>3}|{stars:<15}|{count}")
