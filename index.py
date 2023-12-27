import pyttsx3
def talk(text):
    engine = pyttsx3.init()

    # # List available voices (optional)
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice:", voice.id)

    # Set the desired voice (optional)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0")  # Replace 'VOICE_NAME' with the desired voice

    # Text to be spoken

    # Make Python speak
    engine.say(text)
    engine.runAndWait()
while True:   
    text = input("Talk")
    talk(text)