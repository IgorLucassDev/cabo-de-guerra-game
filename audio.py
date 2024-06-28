import pygame

pygame.init()
pygame.mixer.init()



class Audio:
    def effect(audio):
        myaudio = pygame.mixer.Sound(audio)
        myaudio.play()

    def playAudio(audio):
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
        pygame.event.wait()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()


    def playMusic(music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
        

