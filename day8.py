from functools import reduce
from math import lcm
from re import search

filename = "day8.txt"

def find_steps_part1(start, end, map, pattern):
  steps = 0
  length = len(pattern)
  current = start
  
  while True:
    if current == end:
      print(steps)
      break

    next_step = pattern[steps % length]
    if next_step == 'L':
      current = map[current][0]
    else:
      current = map[current][1]
    steps += 1

def find_steps_part2(start, map, pattern):
  steps = 0
  length = len(pattern)
  current = start
  
  while True:
    if current[2] == 'Z':
      return steps

    next_step = pattern[steps % length]
    if next_step == 'L':
      current = map[current][0]
    else:
      current = map[current][1]
    steps += 1

def part1(filename):
  map = {}

  with open(filename, 'r') as file:
    pattern = file.readline().strip()
    file.readline()
    for line in file:
      node, connected = line.split('=')
      node = node.strip()
      left, right = connected.split()
      left = search("[A-Z]+", left).group()
      right = search("[A-Z]+", right).group()
      map[node] = [left, right]
    
  find_steps_part1('AAA', 'ZZZ', map, pattern)

def part2(filename):
  map = {}
  current_nodes = []

  with open(filename, 'r') as file:
    pattern = file.readline().strip()
    file.readline()
    for line in file:
      node, connected = line.split('=')
      node = node.strip()
      if node[2] == 'A':
        current_nodes.append(node)

      left, right = connected.split()
      left = search("[0-9A-Z]+", left).group()
      right = search("[0-9A-Z]+", right).group()
      map[node] = [left, right]

  steps = []
  for node in current_nodes:
    steps.append(find_steps_part2(node, map, pattern))

  print(reduce(lcm, steps))
