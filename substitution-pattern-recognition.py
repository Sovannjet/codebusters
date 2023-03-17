import random

patterns = ["011", "0102", "01 02", "010...", "...001", "0123413",
            "01232", "0120", "01231", "012031", "0122300", "0122334", "0110"]
answers = [("all", "too"), ("away", "even", "ever"), ("it is", "is it"), "eve", "lly", "science",
           ("there", "where", "these"), ("that", "high", "dead"), "which", "people", "success", "succeed", "oo"]

while True:
    i = random.randrange(len(patterns))
    pattern = patterns[i]
    answer = answers[i]
    num_unique_letters = max([int(n) for n in list(pattern.replace('.', '').replace(' ', ''))])
    replacements = random.sample([chr(i) for i in range(65, 91)], k=num_unique_letters+1)
    ciphertext = pattern
    for i in range(num_unique_letters + 1):
        ciphertext = ciphertext.replace(str(i), replacements[i])
    print(ciphertext)
    response = input()

    while response not in ("quit", "end game", "give up", "don't know"):
        if type(answer) is str:
            if answer not in response:
                response = input()
            else:
                break
        elif type(answer) is tuple:
            if True not in [ans in response for ans in answer]:
                response = input()
            else:
                print("Possible answers: " + str(answer))
                break
    else:
        if response == "give up" or response == "don't know":
            print(answer)
        else:  # response == "quit" or response == "end game"
            break
