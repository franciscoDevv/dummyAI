import cohere
import os
import platform
from pyfiglet import Figlet
from termcolor import colored
from deep_translator import GoogleTranslator

def checkLanguage(s):
  co = cohere.Client(API_KEY)
  response = co.detect_language
  response = co.detect_language(
  texts=[s, "'Здравствуй, Мир'"]
  )
  return response.results[0].language_code


if platform.system() == 'Windows':
  os.system('cls')
elif platform.system() == 'Linux':
  os.system('clear')

  
# YOUR API KEY HERE
API_KEY = 'YOUR_API_KEY_HERE'
# YOUR API KEY HERE

f = Figlet(font='big')
print(f.renderText('dummyAI'))
print(colored('Welcome to DummyAI', 'red'))
print("DummyAI is an AI that helps you in a lot of things. It is designed to automate many of your every tasks, so that you can have more time to focus on the things that matter for you.")
print("How can i help you?")
print("")
while 1:
  s = input("> ")
  print(colored("[Working] . . .", "green"))
  translated = GoogleTranslator(source='auto', target='en').translate(s)
    

  if s == 'exit':
    print(colored("Thanks for using DummyAI", "red"))
    break
  else:
    co = cohere.Client(API_KEY)
    response = co.generate(
    model='command-nightly',
    prompt=translated,
    max_tokens=4000,
    temperature=0.9,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    p = checkLanguage(s)
    q = response.generations[0].text
    to_print = GoogleTranslator(source='auto', target=p).translate(q)
    print('{}'.format(to_print))
