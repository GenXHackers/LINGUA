#morse code (both text and music sound audio) generation from english text
#this would be integrated in the dropdown menu that we offer with out frontend, along with other some 22 language translations
# Install necessary packages
!pip install gtts

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from gtts import gTTS
from IPython.display import Audio, display
import scipy.io.wavfile as wav

# Define Morse code mapping
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '@': '.--.-.', ' ': '/'
}

# Function to convert English text to Morse code
def text_to_morse_code(text):
    text = text.upper()
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse_code

# Function to generate audio for Morse code
def morse_code_to_audio(morse_code, dot_length=0.1, frequency=1000):
    def create_signal(frequency, duration):
        t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * t)
    
    audio_signal = np.array([])

    for char in morse_code:
        if char == '.':
            audio_signal = np.concatenate([audio_signal, create_signal(frequency, dot_length)])
        elif char == '-':
            audio_signal = np.concatenate([audio_signal, create_signal(frequency, 3 * dot_length)])
        elif char == ' ':
            audio_signal = np.concatenate([audio_signal, np.zeros(int(44100 * dot_length))])
        elif char == '/':
            audio_signal = np.concatenate([audio_signal, np.zeros(int(44100 * dot_length * 3))])

    return audio_signal

# Function to save and play audio
def save_and_play_audio(audio_signal, filename='morse_code.wav'):
    wav.write(filename, 44100, (audio_signal * 32767).astype(np.int16))
    display(Audio(filename, autoplay=True))

# Get input text from user
input_text = input("Enter the English text to convert to Morse code: ")

# Convert to Morse code
morse_code = text_to_morse_code(input_text)
print("Morse Code:")
print(morse_code)

# Generate Morse code audio
audio_signal = morse_code_to_audio(morse_code)
save_and_play_audio(audio_signal)
