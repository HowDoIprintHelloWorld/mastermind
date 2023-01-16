from random import sample


def inF(l, color):
  for corr in l:
    if corr == color:
      return True
  return False


# Guess already formatted
# Returns (valid, pinresponses)
def guessCLI(correct, guess):
  response = []
  if len(guess) != len(correct):
    print(f"Please enter a sequence of {str(len(correct))} colors sperated by commas!")
    return False, []
  
  for i, color in enumerate(guess):
    color = color.lower().strip()
    if correct[i] == color:
      response.append("black")
    elif inF(correct, color):
      response.append("white")


  return True, sample(response, len(response))



def formatGuess(guess):
  return [g.strip() for g in guess.strip().split(",")]


def formatResult(result):
  return "Result:   "+", ".join(result)
  