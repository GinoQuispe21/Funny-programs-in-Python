# To use this program you need to install the package transalte:
# pip install translate

from translate import Translator

original_language = input("Writhe the original language: ")
translate_language = input("Write the language you want to translate to: ")

s = Translator(from_lang = original_language, to_lang= translate_language)

text = input("Write the text that you want to translate: ")

res = s.translate(text)
print(res)