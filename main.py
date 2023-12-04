import os

# Select which day to run
day = sorted([x[0] for x in os.walk("./Days")], reverse=True)[0][-1]

# day = 5

def execute_python_file(file_path):
   try:
      os.system(f'python "{file_path}"')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

if __name__ == "__main__":
  execute_python_file(f"Days/Day {day}/day{day}.py")
