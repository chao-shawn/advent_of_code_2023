filename = "day6.txt"

def part1(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()

  result = 1
  times = lines[0].split(':')
  times = [int(time) for time in times[1].split()]

  distances = lines[1].split(':')
  distances = [int(dist) for dist in distances[1].split()]

  for i in range(len(times)):
    wins = 0
    duration = times[i]
    record = distances[i]

    for i in range(1, duration):
      traveled = i * (duration - i)
      if traveled > record:
        wins += 1

    if wins > 0:
      result *= wins

  print(result)

def part2(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()

  wins = 0
  times = lines[0].split(':')
  duration = int(''.join(times[1].split()))

  distances = lines[1].split(':')
  record = int(''.join(distances[1].split()))

  for i in range(1, duration):
    traveled = i * (duration - i)
    if traveled > record:
      wins += 1

  print(wins)
