import os

RED = 12
GREEN = 13
BLUE = 14

def star1(dir):
  with open(dir+"/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    ids_to_sum = []
    for row in data:
      cols = row.split(":")
      id = int(cols[0].replace("Game ",""))
      row = cols[1]
      row = row.split(";")
      row_to_sum = True
      for scenario in row:
        scenarios = scenario.split(",")
        to_sum = True
        for s in scenarios:
          if "red" in s:
            if int(s.replace("red","")) > RED:
              to_sum = False
          if "green" in s:
            if int(s.replace("green","")) > GREEN:
              to_sum = False
          if "blue" in s:
            if int(s.replace("blue","")) > BLUE:
              to_sum = False
        if not to_sum:
          row_to_sum = False
      if row_to_sum:
        ids_to_sum.append(id)       
    print(sum(list(dict.fromkeys(ids_to_sum))))
    return


def star2(dir):
  with open(dir+"/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    sum_row = []
    for row in data:
      cols = row.split(":")
      id = int(cols[0].replace("Game ",""))
      row = cols[1]
      row = row.split(";")
      row_sum = {"R":1, "G":1, "B":1}
      for scenario in row:
        scenarios = scenario.split(",")
        for s in scenarios:
          if "red" in s:
            if int(s.replace("red","")) > row_sum["R"]:
              row_sum["R"] = int(s.replace("red",""))
          if "green" in s:
            if int(s.replace("green","")) > row_sum["G"]:
              row_sum["G"] = int(s.replace("green",""))
          if "blue" in s:
            if int(s.replace("blue","")) > row_sum["B"]:
              row_sum["B"] = int(s.replace("blue",""))
      to_sum = row_sum["R"]*row_sum["G"]*row_sum["B"]  
      sum_row.append(to_sum)       
    print(sum(sum_row))
    return


if __name__ == '__main__':
  path, filename = os.path.split(os.path.realpath(__file__))
  star1(path)
  star2(path)
