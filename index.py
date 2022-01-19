import random
from unicodedata import normalize
from words import words_list
word = ""
number_max_tries = 6

def get_word_from_list(word): # Seleciona palavra aleatória da lista
  word = random.choice(words_list)
  word = normalize('NFKD', word).encode('ASCII','ignore').decode('ASCII')
  return word.upper()

def play_game(word):
  len_secret_word = " _" * len(word)
  max_number_tries = 6
  guessed_letters = []
  num_letters_left = len(word)
  print("Seja vem Vindo ao Jogo da Forca!")
  print('''
      +---+
      |   |
      O   |
      /|\  |
      / \  |
          |
  =============''')
  print("  Versão 0.0.1b\n  =============\n")
  
  print(f"A palavra possui {len(word)} letras, e você possui" + str(number_max_tries) + "de tentativas para encontrar\n\n" + " => PALAVRA: " + len_secret_word + "\n")
  
  while max_number_tries > 0:
    
    guess = input("Digite uma letra: ").upper()
    
    if guess in word:
      
      num_letters_left -= 1
      
      print("Parabéns, " + guess + "pertence a palavra, ainda resta " + str(num_letters_left))
      
      len_secret_word.append(guess)
      
      print(len_secret_word)
      
      
      
      



word = get_word_from_list(word)

play_game(word)
  

  
