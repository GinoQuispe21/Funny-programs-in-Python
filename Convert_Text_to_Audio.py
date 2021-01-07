# import google text to speech (gtts)
from gtts import gTTS

# import as to work on files
import os

# Enter the text you want  to listen
mytext = 'Hola mi panita'

# Enter language
language = 'es' #en = english

# Passing the text and language to the engine
# here we have marked slow = False, which tells
# the module that the converted audio should
# have a high  speed
myobj = gTTS(text = mytext, lang = language, slow = False)

# Saving the converted audio in a mp3 file named auido
myobj.save('audio.mp3')

# Playing the converted file
os.system("audio.mp3")