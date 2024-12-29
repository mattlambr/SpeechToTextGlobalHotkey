# Speech-to-Text Hotkey Script

This Python script enables speech-to-text functionality using the Whisper AI model and a global hotkey (`F2`) to start and stop recording. Audio is recorded via a microphone, transcribed using the Whisper model, and the resulting text is automatically copied to the clipboard.

---

## Features
- **Global Hotkey**: Press `F2` to toggle recording on or off.
- **Audio Transcription**: Uses the Whisper model to transcribe recorded audio into text.
- **Clipboard Integration**: Automatically copies the transcribed text to the clipboard.
- **Configurable**: Easily change the Whisper model size, microphone input device, or hotkey.

---

## Prerequisites

### 1. Install Python 3.10
Ensure Python 3.10 or a compatible version is installed on your system.

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install sounddevice numpy openai-whisper pyperclip keyboard
```

### 3. Install FFmpeg
The Whisper model relies on FFmpeg for audio processing. Ensure FFmpeg is installed and added to your PATH:

- **Verify FFmpeg**:
  ```bash
  ffmpeg -version
  ```
- **Install FFmpeg**: Download FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) and follow installation instructions.

---

## How to Use

1. Clone the Repository or Copy the Script
   - Save the `SpeechToText.py` script to a directory on your computer.

2. Run the Script
   - Open a terminal and navigate to the script's directory.
   - Run the script:
     ```bash
     python SpeechToText.py
     ```

3. Start/Stop Recording
   - Press `F2` to start recording audio.
   - Press `F2` again to stop recording and transcribe the audio.

4. View Transcription
   - The transcribed text will be printed in the terminal and automatically copied to your clipboard.

---

## Configuration

### Change Whisper Model
The script uses the Whisper "medium" model by default. To change the model size, edit this line in `SpeechToText.py`:
```python
model = whisper.load_model("medium")
```
Replace `medium` with `base`, `small`, or `large` based on your requirements.

### Change Audio Device
To use a specific microphone, update the `DEVICE_INDEX` variable:
```python
DEVICE_INDEX = 1  # Replace with your device's index
```
Run the following code to list available devices:
```python
import sounddevice as sd
print(sd.query_devices())
```

### Change the Hotkey
To use a different hotkey for starting and stopping recording, modify this line in `SpeechToText.py`:
```python
keyboard.add_hotkey("F2", toggle_recording)
```
Replace `"F2"` with any other key or key combination, such as `"Ctrl+Alt+R"`. Refer to the [keyboard documentation](https://pypi.org/project/keyboard/) for valid hotkey formats.

---

## Troubleshooting

- **Issue: Missing FFmpeg**
  - Ensure FFmpeg is installed and added to PATH.

- **Issue: Hotkey Not Working**
  - Ensure no other application is using the specified hotkey.

- **Issue: Audio Device Not Found**
  - Verify the `DEVICE_INDEX` corresponds to an available input device.

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgments
- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model.
- [FFmpeg](https://ffmpeg.org/) for audio processing.
- Contributors to the Python libraries used in this project.
