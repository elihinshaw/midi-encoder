# Text to MIDI Encoder/Decoder

This Python application allows you to encode text messages into MIDI files and decode MIDI files back into text messages. It utilizes the tkinter library for the GUI, mido for MIDI file processing, and pygame for MIDI playback.

## Features

- **Text to MIDI Encoding**
- **MIDI to Text Decoding**
- **Listen to Encoded Files**
- **Simplistic Interface**

## How It Works

- The application maps each character of the alphabet, numbers, and some special characters to MIDI note values.
- Inputed text is converted into MIDI notes, with each character representing a MIDI note.
- The decoding process extracts MIDI note values and maps them back to the corresponding characters.
- Of course it only works if encoded via this application!

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/elihinshaw/midi-encoder.git
    ```

2. Navigate to directory:

    ```bash
    cd midi-encoder
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    py .\main\full_gui.py
    ```

## Usage



1. **Encode Text to MIDI**:
   - Enter the text message you want to encode in the provided text entry field.
   - Click on the "Save Encoded File" button to save the encoded MIDI file.

2. **Decode MIDI to Text**:
   - Click on the "Open Encoded File" button to select the MIDI file you want to decode.
   - The decoded text will be displayed in the text area below.

3. **Listen to Encoded File**:
   - Navigate to the "Listen to Encoded File" tab.
   - Click on the "Listen to Encoded File" button to listen to the encoded MIDI file.

---