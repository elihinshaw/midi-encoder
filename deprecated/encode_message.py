import mido
import os
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import argparse

char_to_note = {
    "A": 60,
    "B": 61,
    "C": 62,
    "D": 63,
    "E": 64,
    "F": 65,
    "G": 66,
    "H": 67,
    "I": 68,
    "J": 69,
    "K": 70,
    "L": 71,
    "M": 72,
    "N": 73,
    "O": 74,
    "P": 75,
    "Q": 76,
    "R": 77,
    "S": 78,
    "T": 79,
    "U": 80,
    "V": 81,
    "W": 82,
    "X": 83,
    "Y": 84,
    "Z": 85,
    " ": 86,
    "?": 87,
    ",": 88,
    ".": 89,
    "!": 90,
    "0": 91,
    "1": 92,
    "2": 93,
    "3": 94,
    "4": 95,
    "5": 96,
    "6": 97,
    "7": 98,
    "8": 99,
    "9": 100,
}


def text_to_midi(text):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    track.append(mido.Message("program_change", program=2))

    for char in text.upper():
        if char in char_to_note:
            note = char_to_note[char]
            track.append(mido.Message("note_on", note=note, velocity=100, time=0))
            track.append(mido.Message("note_off", note=note, velocity=0, time=80))

    mid.tracks.append(track)
    return mid


def save_midi(output_file_path, midi_data):
    output_directory = "../midis/"
    path_name = "output%s.mid"

    def next_path(path_pattern):
        i = 1
        while os.path.exists(path_pattern % i):
            i += 1
        return path_pattern % i

    output_file_path = next_path(os.path.join(output_directory, path_name))
    midi_data.save(output_file_path)
    return output_file_path


def play_midi(output_file_path):
    play_midi = input("\nDo you wish to hear the encoded message? (y/n): \n").lower()

    if play_midi == "y":
        pygame.mixer.init()
        pygame.mixer.music.load(output_file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def main():
    parser = argparse.ArgumentParser(description="Convert text to MIDI")
    parser.add_argument("text", help="Text to encode into MIDI")
    args = parser.parse_args()

    midi_data = text_to_midi(args.text)
    output_file_path = save_midi("../midis/", midi_data)
    print(f"\nMIDI file saved to: {output_file_path}")

    play_midi(output_file_path)


if __name__ == "__main__":
    main()
