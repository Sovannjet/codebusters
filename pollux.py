import random

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": ".--.",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

key = [random.choice(('.', '-', '/')) for n in range(10)]
dot_nums = []
dash_nums = []
space_nums = []
for n in range(10):
    morse_char = key[n]
    if morse_char == '.':
        dot_nums.append(n)
    elif morse_char == '-':
        dash_nums.append(n)
    else:
        space_nums.append(n)

plaintext = input("Input plaintext: ")

morse = ""
for char in plaintext:
    if char == ' ':
        morse += '/'
    else:
        morse += morse_code[char.upper()] + '/'
morse = morse[0:-1]

ciphertext = ""
for char in morse:
    if char == '.':
        ciphertext += str(random.choice(dot_nums))
    elif char == '-':
        ciphertext += str(random.choice(dash_nums))
    elif char == '/':
        ciphertext += str(random.choice(space_nums))
    else:
        print("error")

for n in random.sample(range(10), k=5):  # k = 5 numbers & corresponding morse chars given
    print("{} = {}".format(n, key[n]))
print(ciphertext)
