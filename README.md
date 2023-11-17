

```markdown
# Audio Transcription and Response Generator

This repository contains a Python script that transcribes audio files and generates responses using OpenAI's GPT-3.5 model and Eleven Labs' text-to-speech API. The script also includes a Gradio interface for easy interaction.

## Features

- Audio transcription using OpenAI's Whisper model.
- Response generation using OpenAI's GPT-3.5 model.
- Text-to-speech conversion using Eleven Labs API.
- Gradio interface for easy use.

## Installation

Before running the script, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install openai elevenlabs pydub gradio
```

## Configuration

Set your API keys for Eleven Labs and OpenAI in the `config.py` file:

```python
# config.py
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
ELEVEN_LABS_API_KEY = "YOUR_ELEVEN_LABS_API_KEY"
```

## Usage

To use the script, run the following command:

```bash
python script_name.py
```

This will launch the Gradio interface, where you can upload your audio file and view the transcribed and generated response.

## Functionality

1. **Audio Transcription**: The script uses OpenAI's Whisper model to transcribe audio files.
2. **Response Generation**: It utilizes GPT-3.5 to generate a response based on the transcription.
3. **Text-to-Speech**: Eleven Labs API is used to convert the generated response into an audio stream.
4. **Gradio Interface**: Provides a user-friendly interface to upload audio files and view responses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the GPT-3.5 and Whisper models.
- Eleven Labs for the text-to-speech API.
- PyDub for audio file manipulation.
- Gradio for creating interactive interfaces.
```

Remember to replace `script_name.py` with the actual name of your Python script and add a `LICENSE` file if you refer to it in your README.
