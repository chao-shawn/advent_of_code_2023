import re

filename = "day1.txt"

def part1(filename):
  sum = 0

  with open(filename, "r") as file:
    for line in file:
      res = re.findall("\d", line)
      first = res[0]
      second = res[-1]
      sum += int(first + second)
  
  print(sum)

def part2(filename):
  sum = 0
  text_nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
  backwards_text_nums = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}

  def find_number(str, text_nums):
    res = re.search(f"\d|{'|'.join(text_nums.keys())}", str).group()
    return res if res.isnumeric() else text_nums[res]

  with open(filename, "r") as file:
    for line in file:
      first = find_number(line, text_nums)
      second = find_number(line[::-1], backwards_text_nums)
      sum += int(first + second)
      print(sum)

  print(sum)
