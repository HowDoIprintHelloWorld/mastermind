from src.gencode import generate
from src.guess import guessCLI, formatGuess, formatResult
from src.hallo import *

hallo()

correct = generate(5, 8)
guess = []
print("correct: ",correct)

while guess != correct:
  guess = formatGuess(input(">>   "))
  res = guessCLI(correct, guess)
  if res[0]:
    print(formatResult(res[1]))
  

print("congratulations, you cracked the code!")