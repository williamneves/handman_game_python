'''
### JOGO DA FORCA ####
VERSÃO 1.0.0b - PT_BR
by WILLIAM NEVES
'''

import random
import time
import emoji # Importar os emojis, muito importante!
from unicodedata import normalize
from words import words_list # Lista de palavras do jogo

word = ""
number_max_tries = 0

def ttransform_accent(letter): # Função que retira o acento
  remove_accent = normalize('NFKD', letter).encode('ASCII','ignore').decode('ASCII')
  return remove_accent

def get_word_from_list(word): # Seleciona palavra aleatória da lista, e retira os acentos
  word = ttransform_accent(random.choice(words_list))
  word = normalize('NFKD', word).encode('ASCII','ignore').decode('ASCII') 
  return word.upper()

def play_game(word): # Função que regula o jogo - Veja as regras em README.md
  secret_word = "_" * len(word)
  max_number_tries = 6 # Quantidade de erros que o jogador por ter
  guessed_letters = []
  win = False
  num_letters_left = len(word)

  print(f"A palavra possui {len(word)} letras, e você possui " + str(number_max_tries) +\
           " tentativas para encontrar\n\n")
  time.sleep(0.7)

  print(" \U0001F449 PALAVRA: " + secret_word + "\n")
  time.sleep(0.1)

  if len(guessed_letters) > 0:
    print("Letras já utilizadas: ", guessed_letters)
    time.sleep(0.2)
  else:
    pass

  while max_number_tries > 0 and win == False:

    guess = ttransform_accent(input("Digite uma letra: ").upper())
    time.sleep(0.7)

    if len(guess) == 1 and guess.isalpha():

      if guess in guessed_letters:
        print("➰ Você já tentou essa letra")
        pass

      elif guess in word:
        
        guessed_letters.append(guess)
        secret_word_list = list(secret_word)
        indice = [char for char, letter in enumerate(word) if letter == guess]
        
        for index in indice:
          secret_word_list[index] = guess
          
        secret_word = "".join(secret_word_list)
        print("🎯 Parabéns", guess, "está na palavra.\n")
        
        if word == secret_word:
          win = True

      else:
        max_number_tries -= 1
        guessed_letters.append(guess)
        print(f"❌ A letra {guess} não está na palavra. Você tem {max_number_tries} tentativas restantes.\n")
    
    elif len(guess) > 1:
      print("❌ Erro, você digitou mais de uma letra.")
    
    elif not guess.isalpha() and len(guess) == 1:
      print(f"❌ Erro. Você digitou '{guess}', que é um caracter inválido.")

    else:
      print("‼ Tentativa inválida.")

    if win == True:
      print("🎉 Parabéns 🎊, você ganhou \U0001F44F!")
      time.sleep(.3)
      print("🔓 A palavra secreta era **" + word + "**\n\n")

    elif max_number_tries == 0:
      print("😰 Acabaram as tentativas e você não acertou!\n")
    
      print("🔒 A palavra secreta era ** " + word + "**\n\n")

    else:
      print(f"Restam {max_number_tries} tentativas.")
      print("")

      time.sleep(.3)

      print(" \U0001F449 PALAVRA: " + secret_word)

      if len(guessed_letters) > 0:
        print("  *Já utilizadas: (" + ",".join(guessed_letters) + ")\n")
        time.sleep(0.2)

      else:
        pass

print("\n\n**================================**\n  Seja vem Vindo ao Jogo da Forca!")
print('''
                 +---+
                 |   |
                 O   |
                /|\  |
                / \  |
              _______|
  ================================''')
print("        Versão: 1.0.0b PT-br\n            by: William_Neves\n  ================================\n")

time.sleep(1)

play = True
play_times = 0
want_play_more = True

while play:

  word = get_word_from_list(word)
  play_game(word)
  time.sleep(1)
  play_times += 1

  while want_play_more:
    s_or_n = input("Quer jogar mais? S ou N: ").upper()

    if len(s_or_n) == 1 and s_or_n.isalpha():

      if s_or_n == "S":
        print("\nOk, vamos sortear outra palavra\n\n")
        word = get_word_from_list(word)
        play_game(word)
        time.sleep(1)

      else:
        print("Até a próxima!\n")
        play = False
        want_play_more = False
        time.sleep(1)

    else:
      print("Caractere inserido inválido!")
      pass