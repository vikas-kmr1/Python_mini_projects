#string concatenation
# a few ways to do this

# word="World"
# print("Hello " +word)
# print("Hello {}".format(word))
# print(f"Hello {word}")
from madlibs_demo import hp, code, zombies, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombies, hungergames])
    m.madlib()
