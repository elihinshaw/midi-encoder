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


midi_file = input("\nPlease include your encoded message's file path:\n")
midi_data = mido.MidiFile(midi_file)

decoded_text = midi_to_text(midi_data)

print(decoded_text)
