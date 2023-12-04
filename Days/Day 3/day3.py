import os
import math as m, re

def star1(dir):
  board = list(open(dir+'/input.txt'))
  chars = {(r, c): [] for r in range(140) for c in range(140)
                      if board[r][c] not in '01234566789.'}

  for r, row in enumerate(board):
      for n in re.finditer(r'\d+', row):
          edge = {(r, c) for r in (r-1, r, r+1)
                         for c in range(n.start()-1, n.end()+1)}

          for o in edge & chars.keys():
              chars[o].append(int(n.group()))

  print(sum(sum(p) for p in chars.values()))
  return


def star2(dir):
  board = list(open(dir+'/input.txt'))
  chars = {(r, c): [] for r in range(140) for c in range(140)
                      if board[r][c] not in '01234566789.'}

  for r, row in enumerate(board):
      for n in re.finditer(r'\d+', row):
          edge = {(r, c) for r in (r-1, r, r+1)
                         for c in range(n.start()-1, n.end()+1)}

          for o in edge & chars.keys():
              chars[o].append(int(n.group()))

  print(sum(m.prod(p) for p in chars.values() if len(p)==2))
  return


if __name__ == '__main__':
  path, filename = os.path.split(os.path.realpath(__file__))
  star1(path)
  star2(path)
