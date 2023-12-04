import os


def star1(dir):
  with open(dir + "/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    sum_of_points = 0
    for row in data:
      row = row.split(": ")
      lists = row[1].split(" | ")
      winning = list(map(int, lists[0].split()))
      we_have = list(map(int, lists[1].split()))
      sum_of_winning = 0
      for n in winning:
        if n in we_have:
          sum_of_winning += 1
      sum_of_points += (2**(sum_of_winning-1)) if sum_of_winning > 0 else 0
      
    print(sum_of_points)
    return


def star2(dir):
  with open(dir + "/input.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    index_array = [1]*len(data)
    sum_array = [1]*len(data)
    
    for row in range(len(data)):
      data[row] = data[row].split(": ")
      lists = data[row][1].split(" | ")
      winning = list(map(int, lists[0].split()))
      we_have = list(map(int, lists[1].split()))
      
      sum_of_winning = 0
      for n in winning:
        if n in we_have:
          sum_of_winning += 1
      
      for i in range(sum_of_winning):
        sum_array[row+1+i] += sum_array[row]
        
    print(sum(sum_array))
    return


if __name__ == '__main__':
  path, filename = os.path.split(os.path.realpath(__file__))
  star1(path)
  star2(path)
