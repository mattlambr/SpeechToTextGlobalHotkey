import sounddevice as sd
import numpy as np
import whisper
import pyperclip
import keyboard
import time
import wave
import os

# Define audio settings
SAMPLE_RATE = 44100  # Sample rate in Hz
AUDIO_FILE = "temp_recording.wav"  # Temporary audio file for debugging
DEVICE_INDEX = 1  # Replace with the index of your desired input device

# Load Whisper model
model = whisper.load_model("medium")  # Change "base" to "small", "medium", or "large" for different accuracy levels

# State flag to track whether recording is active
is_recording = False
audio_data = None  # Variable to hold recorded audio

def start_recording():
    global audio_data, is_recording
    print("Recording started...")

    # Beep to indicate the start of recording
    sd.play(np.sin(2 * np.pi * 440 * np.linspace(0, 0.1, int(SAMPLE_RATE * 0.1))), SAMPLE_RATE)
    time.sleep(0.1)

    # Start recording
    audio_data = sd.rec(int(30 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16', device=DEVICE_INDEX)
    is_recording = True

def stop_recording():
    global audio_data, is_recording
    print("Recording stopped.")

    # Beep to indicate the end of recording
    sd.play(np.sin(2 * np.pi * 440 * np.linspace(0, 0.1, int(SAMPLE_RATE * 0.1))), SAMPLE_RATE)
    time.sleep(0.1)

    sd.stop()  # Stop the recording stream
    is_recording = False

    # Save the recorded audio as a WAV file
    with wave.open(AUDIO_FILE, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes per sample (int16)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())  # Save the entire buffer

    print(f"Audio saved to {AUDIO_FILE}")

    # Transcribe audio
    transcribe_audio(AUDIO_FILE)

def transcribe_audio(file_path):
    """Use Whisper to transcribe the audio file."""
    print("Transcribing audio...")

    # Transcribe with Whisper
    result = model.transcribe(file_path)
    text = result["text"]
    print("Transcription:", text)

    # Copy to clipboard
    pyperclip.copy(text)
    print("Text copied to clipboard.")

    # Beep to indicate the text has been copied
    sd.play(np.sin(2 * np.pi * 440 * np.linspace(0, 0.1, int(SAMPLE_RATE * 0.1))), SAMPLE_RATE)
    time.sleep(0.1)

def toggle_recording():
    """Toggle between starting and stopping recording."""
    global is_recording
    if not is_recording:
        start_recording()
    else:
        stop_recording()

def main():
    print("Press F2 to start/stop recording and transcribe audio...")
    # Set up a hotkey to toggle recording
    keyboard.add_hotkey("F2", toggle_recording)

    # Keep the program running indefinitely
    print("Press Ctrl + C to stop the script.")
    while True:
        time.sleep(1)  # Sleep to prevent high CPU usage in the loop

if __name__ == "__main__":
    main()
