print("Bem Vindo ao jogo da Força")

secret_word = ["R", "I", "O"]
guessed_char = []

for char in range(0, len(secret_word)):
    guessed_char.append("_")

check = False

while check == False:
    attempt = str(input("Digite apenas 1 letra: "))

    for char in range(0, len(secret_word)):
        if attempt == secret_word[char]:
            guessed_char[char] = attempt

        print(guessed_char[char])

    check = True

    for hi_char in range(0, len(guessed_char)):
        if guessed_char[hi_char] == "_":
            check = False

