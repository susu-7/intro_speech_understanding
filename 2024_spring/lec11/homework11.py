import speech_recognition as sr

def transcribe_wavefile(filename, language='en-US'):
    '''
    Use sr.Recognizer and sr.AudioFile to transcribe speech from an audio file.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)

    @returns:
    text (str) - the recognized speech
    '''
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)  # read the entire audio file
    
    # Attempt to recognize the speech
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

