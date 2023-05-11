import cohere
import time
from pyfiglet import Figlet
from termcolor import colored

f = Figlet(font='big')
print(f.renderText('dummyAI'))
print(colored('Welcome to DummyAI', 'red'))
print("DummyAI is an AI that helps you in a lot of things. It is designed to automate many of your every tasks, so that you can have more time to focus on the things that matter for you.")
print("How can i help you?")
print("")
while 1:
  s = input("> ")
  print(colored("[Working] . . .", "green"))


  co = cohere.Client('{YOUR_API_KEY_HERE}')
  response = co.generate(
  model='command',
  prompt=s,
  max_tokens=4000,
  temperature=0.9,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  print('{}'.format(response.generations[0].text))
