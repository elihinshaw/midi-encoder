import mido
import os
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Dictionary mapping characters to MIDI notes
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

    # Increment midi output name if path already exists
    def next_path(path_pattern):
        i = 1
        while os.path.exists(path_pattern % i):
            i += 1
        return path_pattern % i

    output_file_path = next_path(os.path.join(output_directory, path_name))
    midi_data.save(output_file_path)
    return output_file_path


def play_midi(output_file_path):
    play_midi = messagebox.askyesno(
        "Play MIDI", "Do you wish to hear the encoded message?"
    )

    if play_midi:
        pygame.mixer.init()
        pygame.mixer.music.load(output_file_path)
        pygame.mixer.music.play()


def convert_text_to_midi():
    text = entry_text.get()
    if text:
        midi_data = text_to_midi(text)
        output_file_path = save_midi("../midis/", midi_data)
        messagebox.showinfo(
            "MIDI Saved", f"MIDI file saved to: {os.path.abspath(output_file_path)}"
        )
        play_midi(output_file_path)
    else:
        messagebox.showwarning("No Text Entered", "Please enter some text to convert.")


# Create main window
root = tk.Tk()
root.title("Text to MIDI Converter")

# Configure style
style = ttk.Style(root)
style.theme_use("clam")  # Use a different theme for a modern look
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Set window size
root.geometry("600x300")  # Set width to 600 and height to 300


# Function to center the window
def center_window(width, height):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the window to be centered
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry("%dx%d+%d+%d" % (width, height, x, y))


# Center the window
center_window(600, 300)

# Create explanation label
label_explanation = ttk.Label(
    root, text="Enter the text you want to convert to MIDI below:"
)
label_explanation.pack(pady=10)

# Create input field
entry_text = ttk.Entry(root, width=60, font=("Arial", 12))
entry_text.pack(pady=10)

# Create convert button
button_convert = ttk.Button(
    root, text="Convert Text to MIDI", command=convert_text_to_midi
)
button_convert.pack(pady=10)

root.mainloop()
