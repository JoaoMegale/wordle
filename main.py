import base64
import requests
import random
from colorama import Fore
from unidecode import unidecode


def word_filter(word_list):
    result = []
    for word in word_list:
        if len(word) == 5:
            result.append(unidecode(word.lower()))
            
    return result

def check_word(user_word, selected_word, state):

    pos = 0
    for letter in user_word:
        
        if letter in selected_word:
            if selected_word[pos] == letter:
                state[pos] = 2
            else:
                state[pos] = 1
        else:
            state[pos] = 0
            
        pos += 1

def print_state(word, state):

    print("  ", end="")     # alinhamento
    for letter, st in zip(word, state):
        if st == 0:
            print(Fore.RED + letter, end="")
        elif st == 1:
            print(Fore.YELLOW + letter, end="")
        elif st == 2:
            print(Fore.GREEN + letter, end="")
        else:
            print("Invalid state.")
    print('\n')

def check_win(state):

    if state == [2,2,2,2,2]:
        return True
    else:
        return False


master = "https://www.ime.usp.br/~pf/dicios/br-utf8.txt"
req = requests.get(master)
req = req.text
portuguese_words_dict = req.split('\n')

valid_words = word_filter(portuguese_words_dict)
selected_word = random.choice(valid_words)

state = [0,0,0,0,0]
num_tries = 6
i = 0

while True:

    user_word = input(Fore.WHITE + '> ')
    if user_word not in valid_words:
        print("Palavra inválida")
        continue
    
    check_word(user_word, selected_word, state)

    if (check_win(state)):
        print(Fore.GREEN + "Ganhou!")
        break

    i += 1       
    print_state(user_word, state)

    if i >= num_tries:
        print(Fore.RED + "Perdeu!")
        break
        

print(Fore.WHITE + "A palavra era: " + selected_word)
    
