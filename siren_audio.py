import pygame

class SirenAudio:
    def __init__(self):
        pygame.mixer.init()

    def stop(self):
        pygame.mixer.music.stop()

    def load(self, fname):
        pygame.mixer.music.load(fname)

    def play_audio(self, fname, shouldLoop):
        self.stop()
        self.load(fname)

        if shouldLoop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(0)


