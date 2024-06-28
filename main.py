import keyboard
from board import Board
import os


# Variaveis de configuração
score = 0
isPlaying = True

def increment():
    global score
    global isPlaying
    score = score + 1
    Board.draw(score)




def decrement():
    global score
    global isPlaying
    score = score - 1
    Board.draw(score)
    



while isPlaying:
    os.system('cls')
    print(f"""
               ______________
              |CABO DE GUERRA|
--------------------------------------------
 Player1                             Player2             

                      |
                      |
          ############ ############
                      |
                      |
    
--------------------------------------------
    """)
    keyboard.add_hotkey('a', callback=decrement)
    keyboard.add_hotkey('l', callback=increment)

    
    keyboard.wait()
    