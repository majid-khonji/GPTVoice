import speech_recognition as sr
import pyttsx3
import openai
from langchain.llms import OpenAI
import os
import pygame
import tempfile
import time


# for better speak recognition
import speech_recognition as sr
from google.cloud import texttospeech_v1 as texttospeech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api/api-project-957651503585-fbacf3fb62b5.json"


# OPENAI key
if os.getenv("OPENAI_API_KEY") is None and not os.path.isfile('api/gpt.txt'):
    os.environ["OPENAI_API_KEY"] = input("Please enter your OpenAI API key: ")
elif os.path.isfile('api/gpt.txt'):
    with open('api/gpt.txt', 'r') as f:
        os.environ["OPENAI_API_KEY"] = f.read().strip()


def speak_realistic(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    fd, temp_filename = tempfile.mkstemp(suffix=".mp3")
    with open(temp_filename, "wb") as out:
        out.write(response.audio_content)
    os.close(fd)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()  # Stop playback
    pygame.mixer.quit()  # Quit the mixer
    time.sleep(1)  # Add a small delay before removing the file
    print(temp_filename)
    # os.remove(temp_filename)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate (words per minute)
    engine.setProperty('volume', 0.9)  # Adjust volume level (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def detect_wake_up_word(wake_up_word, text):
    return text.lower() == wake_up_word.lower()

def record_audio():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def audio_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    llm = OpenAI(temperature=0.9)

    wake_up_word = "hello robot"
    GPT_awake = False
    conversation_history = ""
    speak_realistic("Hello, I am your robot assistant. Say hello robot to start a conversation.")
    while True:
        audio = record_audio()
        text = audio_to_text(audio)
        if detect_wake_up_word(wake_up_word, text) and not GPT_awake:
            GPT_awake = True
            wake_up_message = "I am now actively listening to you. Go ahead with your question. Notice that I am using the GPT API to answer your questions."
            print(wake_up_message)
            speak_realistic(wake_up_message)  # Make the assistant speak the wake-up message
            audio = record_audio()
            text = audio_to_text(audio)
            conversation_history = ""  # Reset conversation history
        elif GPT_awake:

            if text == "":
                # msg = "Please try again."
                # speak_realistic(msg)
                continue
        if text != "":
            # Add previous conversations to context
            context = f"{conversation_history} {text}"

            response = llm(text)
            print(response)
            speak_realistic(response)

            # Append current conversation to history
            conversation_history = f"{conversation_history}\n{text}"



if __name__ == "__main__":
    main()
    