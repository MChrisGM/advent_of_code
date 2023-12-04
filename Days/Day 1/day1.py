import os
import re

numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def words_to_digits(str_input):
  str_input = str(str_input)
  for k in numbers.keys():
    str_input = str_input.replace(k, k[0]+str(numbers[k])+k[-1])
  return str_input

def remove_letters(str_input):
  str_input = str(str_input)
  s = re.sub("[^1-9]","",str_input)
  return s[0]+''+s[-1]

def star1(dir):
  with open(dir+"/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(remove_letters(numbers)) for numbers in data]
    print(sum(data))


def star2(dir):
  with open(dir+"/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [words_to_digits(numbers) for numbers in data]
    data = [int(remove_letters(numbers)) for numbers in data]
    print(sum(data))


if __name__ == '__main__':
  path, filename = os.path.split(os.path.realpath(__file__))
  star1(path)
  star2(path)
