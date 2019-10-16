import pygame
import json
from siren_audio import SirenAudio


running = True
config = {}
screen = None
sa = SirenAudio()


# Is this silly? It might be silly
def load_config(fname):
    with open('config.json', 'r') as f:
        return json.load(f)



def setup_pygame():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(
        (
            config['resolution']['x'],
            config['resolution']['y']
        )
    )
    print('yeet2')


def enter_the_loop_my_dude():
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sa.play_audio('audio/scotland.mp3', True)
                if event.key == pygame.K_DOWN:
                    sa.stop()
                if event.key == pygame.K_RIGHT:
                    sa.play_audio('audio/hilo2.wav', True)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()



def main():
    global config
    print('yeet')
    config = load_config('config.json')
    setup_pygame()

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

    enter_the_loop_my_dude()


# sa.play_audio('scotland.mp3', True)

main()