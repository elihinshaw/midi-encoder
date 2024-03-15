import tkinter as tk
from tkinter import ttk, filedialog
import mido

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


def open_midi_file():
    midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    if midi_file_path:
        try:
            midi_data = mido.MidiFile(midi_file_path)
            decoded_text = midi_to_text(midi_data)
            text_output.config(state="normal")
            text_output.delete("1.0", "end")
            text_output.insert("end", decoded_text)
            text_output.config(state="disabled")
        except Exception as e:
            text_output.config(state="normal")
            text_output.delete("1.0", "end")
            text_output.insert("end", f"Error: {str(e)}")
            text_output.config(state="disabled")


root = tk.Tk()
root.title("MIDI Decoder")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

root.geometry("400x300")

label_explanation = ttk.Label(
    root, text="Click the button below to select a MIDI file and decode it:"
)
label_explanation.pack(pady=10)

button_open_midi = ttk.Button(root, text="Open MIDI File", command=open_midi_file)
button_open_midi.pack(pady=10)

text_output = tk.Text(root, height=10, width=50, state="disabled")
text_output.pack(pady=10)

root.mainloop()
