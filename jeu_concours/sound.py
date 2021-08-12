import pygame

class Sound:
    def __init__(self):
        self.compteur = 1
        self.sound = "background.mp3"
        self.sound2 = "win.mp3"

        self.sound4 = "game_over.mp3"
        self.sound_game = pygame.mixer.Sound(f"music/{self.sound}")
        self.sound_game2 = pygame.mixer.Sound(f"music/{self.sound2}")

        self.sound_game4 = pygame.mixer.Sound(f"music/{self.sound4}")

    def play(self):
        self.sound_game.play(100)
    def stop(self):
        self.sound_game.stop()

    def play2(self):

        self.sound_game.stop()

        self.sound_game2.play()
        
        
    def play3(self):

        self.sound_game.stop()

        self.sound_game3.play()
    def play1(self):

        self.sound_game2.stop()

        self.sound_game.play()

    def play4(self):
        self.sound_game.stop()

        self.sound_game4.play()
    def play5(self):
        self.sound_game4.stop()

        self.sound_game.play()


