from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame


def play_midi():
    pygame.mixer.init()
    midi_file = input("\nPlease include your encoded message's file path:\n")
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


play_midi()
