import random
import time

morse = {
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
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
    # "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    # "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"
}

corrects = [0] * 26
seens = [0] * 26
timeses = [[] for x in range(26)]


def play():
    global corrects
    global seens

    pair = random.choice(list(morse.items()))
    i = random.randint(0, 1)
    prompt = pair[i]
    answer = pair[i - 1]

    print(prompt)
    t0 = time.time()
    response = input()

    # increment corrects
    if response.upper() == answer:
        t = time.time()
        if '.' in prompt or '-' in prompt:
            corrects[ord(answer) - 65] += 1
            timeses[ord(answer) - 65].append(t - t0)
        else:
            corrects[ord(prompt) - 65] += 1
            timeses[ord(prompt) - 65].append(t - t0)

    while response.upper() != answer:
        if response == "give up" or response == "don't know":
            print("answer was " + pair[i - 1])
            break
        elif response == "quit" or response == "end game":
            print("{}\t{}\t{}\t{}\t{}".format("Letter", "Correct", "Seen", "Accuracy", "Avg. Time"))
            for n in range(26):
                correct = corrects[n]
                seen = seens[n]
                acc = "-\t"
                avg = "-\t"
                times = timeses[n]
                if seen != 0:
                    acc = "{:.2%}".format(correct / seen)
                if len(times) != 0:
                    avg = "{:.3f}".format(sum(times) / len(times))
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(chr(n + 65), correct, seen, acc, avg))
            return
        else:
            print("incorrect")
            response = input()

    # increment seens
    if '.' in prompt or '-' in prompt:
        seens[ord(answer) - 65] += 1
    else:
        seens[ord(prompt) - 65] += 1

    play()


play()
