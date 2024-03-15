import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import mido
import os
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame

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

note_to_char = {note: char for char, note in char_to_note.items()}


def midi_to_text(midi_file):
    text = ""
    for msg in midi_file:
        if msg.type == "note_on":
            note = msg.note
            if note in note_to_char:
                text += note_to_char[note]
    return text


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


def open_midi_file():
    midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    if midi_file_path:
        try:
            midi_data = mido.MidiFile(midi_file_path)
            decoded_text = midi_to_text(midi_data)
            text_output_decoded.config(state="normal")
            text_output_decoded.delete("1.0", "end")
            text_output_decoded.insert("end", decoded_text)
            text_output_decoded.config(state="disabled")
        except Exception as e:
            text_output_decoded.config(state="normal")
            text_output_decoded.delete("1.0", "end")
            text_output_decoded.insert("end", f"Error: {str(e)}")
            text_output_decoded.config(state="disabled")


def save_midi(output_directory, midi_data):
    output_file_path = filedialog.asksaveasfilename(
        defaultextension=".mid",
        filetypes=[("MIDI files", "*.mid")],
        initialdir=output_directory,
        title="Save MIDI file",
    )

    if output_file_path:
        try:
            midi_data.save(output_file_path)
            return output_file_path
        except Exception as e:
            messagebox.showerror("Error", f"Error saving MIDI file: {str(e)}")
    return None


def convert_text_to_midi():
    text = entry_text.get()
    if text:
        midi_data = text_to_midi(text)
        output_file_path = save_midi("../midis/", midi_data)
        if output_file_path:
            messagebox.showinfo(
                "MIDI Saved", f"MIDI file saved to: {os.path.abspath(output_file_path)}"
            )
            play_midi(output_file_path)
    else:
        messagebox.showwarning("No Text Entered", "Please enter some text to convert.")


def play_midi(output_file_path):
    play_midi = messagebox.askyesno(
        "Play MIDI", "Do you wish to hear the encoded message?"
    )

    if play_midi:
        pygame.mixer.init()
        pygame.mixer.music.load(output_file_path)
        pygame.mixer.music.play()


def listen_to_midi():
    midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    if midi_file_path:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(midi_file_path)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")


root = tk.Tk()
root.title("Encode / Decode Text")
root.configure(bg="#2b2b2b")
root.minsize(800, 600)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

encode_tab = ttk.Frame(notebook)
notebook.add(encode_tab, text="Encode")

canvas_encode = tk.Canvas(encode_tab, bg="#2b2b2b", highlightthickness=0)
canvas_encode.pack(fill="both", expand=True)

label_explanation_text_to_midi = ttk.Label(
    encode_tab,
    text="Enter the text you want to encode below",
    font=("Arial", 20, "bold"),
    foreground="white",
    background="#2b2b2b",
)
label_explanation_text_to_midi.place(relx=0.5, rely=0.1, anchor="center")

entry_text = ttk.Entry(encode_tab, width=50, font=("Arial", 20))
entry_text.place(relx=0.5, rely=0.3, anchor="center")

button_convert_text_to_midi = ttk.Button(
    encode_tab, text="Save Encoded File", command=convert_text_to_midi, width=20
)
button_convert_text_to_midi.place(relx=0.5, rely=0.5, anchor="center")

decode_tab = ttk.Frame(notebook)
notebook.add(decode_tab, text="Decode")

canvas_decode = tk.Canvas(decode_tab, bg="#2b2b2b", highlightthickness=0)
canvas_decode.pack(fill="both", expand=True)

label_explanation_midi_to_text = ttk.Label(
    decode_tab,
    text="Select an encoded file and decode it below",
    font=("Arial", 20, "bold"),
    foreground="white",
    background="#2b2b2b",
)
label_explanation_midi_to_text.place(relx=0.5, rely=0.1, anchor="center")

button_open_midi = ttk.Button(
    decode_tab, text="Open Encoded File", command=open_midi_file, width=20
)
button_open_midi.place(relx=0.5, rely=0.225, anchor="center")

text_output_decoded = tk.Text(
    decode_tab,
    height=10,
    width=50,
    state="disabled",
    font=("Arial", 12),
    background="black",
    foreground="white",
)
text_output_decoded.place(relx=0.5, rely=0.5, anchor="center")

listen_tab = ttk.Frame(notebook)
notebook.add(listen_tab, text="Listen to Encoded File")

canvas_listen = tk.Canvas(listen_tab, bg="#2b2b2b", highlightthickness=0)
canvas_listen.pack(fill="both", expand=True)

button_listen_to_midi = ttk.Button(
    listen_tab,
    text="Listen to Encoded File",
    command=listen_to_midi,
    width=100,
    padding=50,
)
button_listen_to_midi.place(relx=0.5, rely=0.445, anchor="center")

root.mainloop()
