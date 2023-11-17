import os
import io
import openai
import config
from elevenlabs import set_api_key, generate, stream
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import gradio as gr

# Set your ElevenLabs API key
set_api_key("ELEVEN LABS API KEY")

openai.api_key = config.OPENAI_API_KEY

# Messages initialization
messages = [{"role": "system",
             "content": 'PUT YOU THE PERSONLITY YOU WANT'}]

# Splitting audio into chunks


def split_audio(file_path, chunk_length_ms=10000):
    audio = AudioSegment.from_file(file_path)
    return [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

# Transcribing a single chunk


def transcribe_chunk(chunk):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, "temp_audio.wav")
        chunk.export(temp_file_path, format="wav")

        # Transcribe the audio file
        with open(temp_file_path, 'rb') as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            return response["text"]


# Transcribing the entire audio

def transcribe(audio_path):
    global messages
    chunks = split_audio(audio_path)
    full_transcription = " ".join(
        [transcribe_chunk(chunk) for chunk in chunks])

    messages.append({"role": "user", "content": full_transcription})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    # Generate streaming audio response
    def text_stream():
        yield system_message['content']

    audio_stream = generate(
        text=text_stream(),
        voice="ELEVEN LABS VOICE ID",
        model="eleven_monolingual_v1",
        stream=True
    )

    # Stream the audio
    stream(audio_stream)

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += f"{message['role']}: {message['content']}\n\n"

    return chat_transcript


# Gradio Interface
ui = gr.Interface(fn=transcribe, inputs=gr.Audio(
    type="filepath"), outputs="text")
ui.launch(debug=True, share=True)
