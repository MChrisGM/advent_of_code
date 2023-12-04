import os


def star1(dir):
  with open(dir + "/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    return


def star2(dir):
  with open(dir + "/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    return


if __name__ == '__main__':
  path, filename = os.path.split(os.path.realpath(__file__))
  star1(path)
  star2(path)
