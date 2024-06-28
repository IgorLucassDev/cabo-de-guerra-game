import keyboard
from board import Board
import os

from audio import Audio


# Variaveis de configuração
score = 0

isPlaying = False
nameChoosing = True

startGameAudio = './sounds/start.mp3'
background_music = './sounds/music/background.mp3'
clickSound = './sounds/click.mp3'
selectSound = './sounds/select.mp3'


player1 = ''
player2 = ''

def increment():
    Audio.effect(clickSound)
    global score
    global isPlaying
    score = score + 1
    Board.draw(score)
    if score == 11:
        isPlaying = False


def decrement():
    Audio.effect(clickSound)
    global score
    global isPlaying
    score = score - 1
    Board.draw(score)
    if score == -11:
        isPlaying = False

def startGame():
    global nameChoosing
    global isPlaying
    global score
    score = 0
    Audio.playAudio(startGameAudio)
    nameChoosing = False
    isPlaying = True



while nameChoosing:
    player1 = input('Digite o nome no Player1 \n >> ')
    Audio.effect(selectSound)
    player2 = input('Digite o nome no Player2 \n >> ')
    Audio.effect(selectSound)
    command = input('Deseja iniciar o jogo? s/n \n >> ')
    Audio.effect(selectSound)
    if command == 's':
        startGame()
        


while isPlaying:
    Audio.playMusic(background_music)
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
    