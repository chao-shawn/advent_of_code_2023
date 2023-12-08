from collections import defaultdict

filename = "day4.txt"

def part1(filename):
  points = 0

  with open(filename, "r") as file:
    for line in file:
      matches = 0
      _, data = line.split(":")
      nums, winning_nums = data.split("|")

      nums = [int(n) for n in nums.split()]
      winning_nums = [int(n) for n in winning_nums.split()]

      for num in nums:
        if num in winning_nums:
          matches += 1
       
      if matches > 0:
        points += 2 ** (matches - 1)

  print(points)

def part2(filename):
  total = 0
  # index of dict is the card number, value is the number of copies 
  cards = defaultdict(lambda: 1)
  cards[1] = 1

  with open(filename, "r") as file:
    index = 1
    
    for line in file:
      if index not in cards.keys():
        cards[index] = 1

      matches = 0
      _, data = line.split(":")
      nums, winning_nums = data.split("|")

      nums = [int(n) for n in nums.split()]
      winning_nums = [int(n) for n in winning_nums.split()]

      for num in nums:
        if num in winning_nums:
          matches += 1
      
      for i in range(matches):
        cards[index + 1 + i] += cards[index]

      index += 1

  for value in cards.values():
    total += value

  print(total)
