from collections import Counter
filename = "day9.txt"

def predict(nums, direction):
  length = len(nums)
  counts = Counter(nums)
  if counts[0] == length:
    return 0

  new_nums = []
  for i in range(len(nums)-1):
    new_nums.append(nums[i+1] - nums[i])

  if direction == 'next':
    return nums[length-1] + predict(new_nums, 'next')
  else:
    return nums[0] - predict(new_nums, 'first')

def solution(filename, direction):
  sum = 0
  with open(filename, 'r') as file:
    for line in file:
      nums = [int(x) for x in line.split()]
      sum += predict(nums, direction)

  print(sum)

solution(filename, 'next')
solution(filename, 'first')