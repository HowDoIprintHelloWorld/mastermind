from random import randint

colors = ["red", "blue", "black", "white", "green", "yellow", "grey", "brown"]
def generate(amount, coloramount):
  return [colors[:coloramount][randint(0, i)] for i in range(amount)]