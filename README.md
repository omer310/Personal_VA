# Personal voice assasstiant

This repository hosts a personal voice assistant that transcribes audio files and generates responses. You can give it a personality and a cloned voice. It leverages OpenAI's GPT-3.5 model for generating text and Eleven Labs' API for text-to-speech conversion. The script includes a Gradio interface, providing a user-friendly platform for audio file uploads and response visualization.

## Features

- Audio transcription with OpenAI's Whisper model.
- Response generation using OpenAI's GPT-3.5 model.
- Conversion of generated text to speech via Eleven Labs API.
- A Gradio interface for easy audio file upload and interaction.
- Supports chunk-wise audio processing for efficient transcription.
- Generates a comprehensive chat transcript combining user and system messages.
- Streamlined audio streaming of the generated response.

## Technologies Used

- Python
- OpenAI API
- Eleven Labs API
- Gradio
- PyDub

## Installation and Usage

First, ensure the necessary libraries are installed:

```sh
pip install requirements.txt
```

Configure your API key in `config.py`:

```python
# config.py
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

To run the script:

```sh
python script_name.py
```

After launching, upload an audio file or record your audio via the Gradio interface to receive the transcribed and generated response.

## License

This project is available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- OpenAI for the Whisper and GPT-3.5 models.
- Eleven Labs for their text-to-speech technology.
- PyDub for handling audio file operations.
- Gradio for providing the interactive interface.
```
