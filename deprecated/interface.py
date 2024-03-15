import tkinter as tk
from tkinter import Text, Button, messagebox
from encode_message import generate_midi, play_midi


def generate_midi_and_play():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        midi_file_path = generate_midi(text)
        play_midi_prompt(midi_file_path)
    else:
        messagebox.showwarning("Warning", "Please enter some text.")


def play_midi_prompt(file_path):
    play_midi_response = messagebox.askyesno(
        "Playback", "Do you wish to hear the encoded message?"
    )
    if play_midi_response:
        play_midi(file_path)


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))


root = tk.Tk()
root.title("Text to MIDI Converter")
root.configure(background="#f0f0f0")

text_entry = Text(root, height=5, width=40, font=("Arial", 12))
text_entry.pack(pady=20)

generate_button = Button(
    root,
    text="Generate MIDI",
    command=generate_midi_and_play,
    font=("Arial", 14),
    bg="#4caf50",
    fg="#ffffff",
    relief="raised",
)
generate_button.pack(pady=10)

center_window(root)
root.mainloop()
