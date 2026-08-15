# https://www.metacareers.com/profile/coding_puzzles?puzzle=587690079288608
# You solved 31 / 33 test cases. Time Limit Exceeded on 2 test cases

from typing import List
# Write any import statements here

def addToRange(rr, new:List[int]):
  # would be faster with binary search into sorted range list
  if len(rr) == 0:
    rr.append(new)
    return
  
  below = 0
  above = len(rr)-1
  while below < above:
    middle = int((below + above)/2)
    r = rr[middle]
    if new[1] < r[0]: # new ends before middle begins
      above = middle # above still above but middle will be lower
    elif r[1] < new[0]: # middle ends before new begins
      below = middle + 1
    else: # new and middle overlap, merge into the middle item then return
      if new[0] < r[0]:
        r[0] = new[0]
      if new[1] > r[1]:
        r[1] = new [1]
      #print(f"addToRange new({new[0]},{new[1]}) at={middle} merge({r[0]},{r[1]})")
      return
  #print(f"addToRange insert({new[0]},{new[1]}) at={below}")
  rr.insert(below, new)
  return

def getPlusSignCount(N: int, L: List[int], D: str) -> int:
  up,down,left,right = 1,2,4,8
  horizontal = {}
  vertical = {}
  # add ranges to horizontal,vertical hashes, merging as we go
  x,y = 0,0
  for i in range(N):
    direction = D[i]
    length = L[i]
    # print(f"[{x},{y}] direction={direction} length={length}")
    if direction == 'U':
      y2 = y - length
      if not x in vertical:
        vertical[x] = []
      addToRange(vertical[x], [y2, y])
      y = y2
    elif direction == 'D':
      y2 = y + length
      if not x in vertical:
        vertical[x] = []
      addToRange(vertical[x], [y, y2])
      y = y2
    elif direction == 'L':
      x2 = x - length
      if not y in horizontal:
        horizontal[y] = []
      addToRange(horizontal[y], [x2, x])
      x = x2
    elif direction == 'R':
      x2 = x + length
      if not y in horizontal:
        horizontal[y] = []
      addToRange(horizontal[y], [x, x2])
      x = x2
    # if direction
  # for range(N)
  # now compare ranges to find pluses
  plusses = 0
  for y in horizontal:
    for x in vertical:
      plus = 0
      for yy in vertical[x]:
        if yy[0] <= y and y < yy[1]:
          plus |= up
        if yy[0] < y and y <= yy[1]:
          plus |= down
      for xx in horizontal[y]:
        if xx[0] <= x and x < xx[1]:
          plus |= right
        if xx[0] < x and x <= xx[1]:
          plus |= left
      # print(f"[{x},{y}] xx={horizontal[y]} yy={vertical[x]} plus={plus}")
      if plus == up|down|left|right:
        plusses += 1
  return plusses
