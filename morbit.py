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

key = ['..', '.-', './', '-.', '--', '-/', '/.', '/-', '//']
random.shuffle(key)

plaintext = input("Input plaintext: ")

morse = ""
for char in plaintext:
    if char == ' ':
        morse += '/'
    else:
        morse += morse_code[char.upper()] + '/'
if len(morse) % 2 == 1:
    morse = morse[0:-1]

ciphertext = ""
i = 0
while i < len(morse):
    ciphertext += str(key.index(morse[i:i+2]) + 1) + ' '
    i += 2

for n in random.sample(range(9), k=5):  # k = 5 numbers & corresponding morse chars given
    print("{} = {}".format(n+1, key[n]))
print(ciphertext)
