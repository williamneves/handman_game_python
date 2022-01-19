import random
import time
import emoji
from unicodedata import normalize
from words import words_list

word = ""
number_max_tries = 6

def sem_acento(letter):
  remove_acento = normalize('NFKD', letter).encode('ASCII','ignore').decode('ASCII')
  return remove_acento

def get_word_from_list(word): # Seleciona palavra aleatória da lista, e retira os acentos
  word = sem_acento(random.choice(words_list))
  word = normalize('NFKD', word).encode('ASCII','ignore').decode('ASCII') 
  return word.upper() 

def play_game(word):
  len_secret_word = "_" * len(word)
  max_number_tries = 6
  guessed_letters = []
  win = False
  num_letters_left = len(word)
  
  print("\n\n**================================**\n  Seja vem Vindo ao Jogo da Forca!")
  print('''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
           _______|
  ============================''')
  print("          Versão  0.1.0b\n            by: GW_dev\n  ============================\n")

  time.sleep(1)
  
  print(f"A palavra possui {len(word)} letras, e você possui " + str(number_max_tries) +\
           " tentativas para encontrar\n\n")
  time.sleep(1.5)
  
  print(" \U0001F449 PALAVRA: " + len_secret_word + "\n")
  time.sleep(1)
  
  while max_number_tries > 0 and win == False:

    guess = sem_acento(input("Digite uma letra: ").upper())
    time.sleep(0.7)

    if len(guess) == 1 and guess.isalpha():

      if guess in guessed_letters:
        print("➰ Você já tentou essa letra")
        pass

      elif guess in word:
        guessed_letters.append(guess)
        len_secret_word_list = list(len_secret_word)
        indice = [char for char, letter in enumerate(word) if letter == guess]
        for index in indice:
          len_secret_word_list[index] = guess
          
        len_secret_word = "".join(len_secret_word_list)
        print("🎯 Parabéns", guess, "está na palavra.")
        

        if word == len_secret_word:
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
      print("🔓 A palavra secreta era " + word + "\n\n")

    elif max_number_tries == 0:
      print("😰 Acabaram as tentativas e você não acertou!")
    
      print("🔒 A palavra secreta era " + word + "\n\n")

    else:
      print(f"Restam {max_number_tries} tentativas.")
      print("")
      time.sleep(.3)
      print(" \U0001F449 PALAVRA: " + len_secret_word + "\n")

  # if win == True:
  #   print("Parabéns, você acertou!")
  # else:
  #   print("Acabaram as tentativas e você não acertou!")

word = get_word_from_list(word)

play_game(word)
  

  
