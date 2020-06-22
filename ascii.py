import pyfiglet
from termcolor import colored

text = colored("Hi",color="red")
print(text)

result = pyfiglet.figlet_format("hi")

print(result)