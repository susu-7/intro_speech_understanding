from gtts import gTTS

def synthesize(text, lang, filename):
    '''
    Use gTTS (Google Text-to-Speech) to synthesize speech, then save it to a file.
    
    @params:
    text (str) - the text to synthesize
    lang (str) - the language in which to synthesize the text
    filename (str) - the filename where the synthesized speech should be saved
    '''
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

