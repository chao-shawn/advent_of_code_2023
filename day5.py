filename = "test.txt"

def part1(filename):
  with open(filename, "r") as file:
    lines = file.readlines()

  for i in range(len(lines)):
    if lines[i].startswith("seeds: "):
      _, seeds = lines[i].split(":")
      seeds = [int(s) for s in seeds.split()]
      print(seeds)
    elif lines[i].startswith("seed-to-soil"):
      i += 1
      data = []
      while lines[i] != "\n":
        data.append(lines[i])
        i += 1
      print(data)

part1(filename)