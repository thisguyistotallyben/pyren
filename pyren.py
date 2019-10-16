import pygame
import json
from siren_audio import SirenAudio


class PGButton:
    label = ''
    posx = 0
    posy = 0

    sizex = 0
    sizey = 0

    def was_clicked(self, pos):
        if pos[0] in range(self.posx, self.posx + self.sizex) and pos[1] in range(self.posy, self.posy + self.sizey):
           print('clicked')
           return True
        return False


running = True
config = {}
screen = None
sa = SirenAudio()

siren_buttons = []


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


def handle_mouse_click(pos):
    sa.stop()
    print(pos[0])
    if siren_buttons[0].was_clicked(pos):
        sa.play_audio('audio/wail.wav', True)



def enter_the_loop_my_dude():
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if siren_buttons[1].was_clicked(pygame.mouse.get_pos()):
                    sa.play_audio('audio/wail.wav', True)
            if event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_click(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sa.play_audio('audio/scotland.mp3', True)
                if event.key == pygame.K_DOWN:
                    sa.stop()
                if event.key == pygame.K_RIGHT:
                    sa.play_audio('audio/wail.wav', True)



def main():
    global config
    global siren_buttons

    sa.load('audio/smartprty.wav')

    print('yeet')
    config = load_config('config.json')
    setup_pygame()

    wailButton = PGButton()
    wailButton.label = 'Wail'
    wailButton.posx = 0
    wailButton.posy = 0
    wailButton.sizex = 100
    wailButton.sizey = 100

    man = PGButton()
    man.label = 'Manual'
    man.posx = 120
    man.posy = 0
    man.sizex = 100
    man.sizey = 100


    siren_buttons.append(wailButton)
    siren_buttons.append(man)

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 100, 100))
    pygame.display.flip()

    enter_the_loop_my_dude()


# sa.play_audio('scotland.mp3', True)

main()