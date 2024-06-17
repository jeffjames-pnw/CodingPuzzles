# https://www.metacareers.com/profile/coding_puzzles?puzzle=280063030479374

from typing import List

maxHeight = 1000000
farthestLeft = 0
farthestRight = 1000000

class conveyor:
  def __init__(self, h:int, a:int, b:int):
    self.h,self.a,self.b = h,a,b

class exposure:
  def __init__(self, x:int, c:int):
    self.x,self.c = x,c

def findConveyors(cc: List[conveyor], ci: int, height: int, left: int, right: int) -> List[exposure]:
  # null range
  if left > right: 
    return []
  # skip conveyors that are too high or not in this range
  while ci < len(cc) and height <= cc[ci].h and (cc[ci].b < left or right < cc[ci].a): 
    ci += 1
  if ci == len(cc): # hit the floor
    return [exposure(left, -1)]
  # we found the highest conveyor in the horizontal range below the last one
  # it could extend farther left & right than this range
  result = List[exposure]
  if left < cc[ci].a:
    result += findConveyors(cc, ci + 1, cc[ci].h, left, cc[ci].a) 
    left = cc[ci].a
  result += exposure(left, ci)
  if cc[ci].b < right:
    result += findConveyors(cc, ci + 1, cc[ci].h, cc[ci].b, right)
  return result

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:

  cc = List[conveyor]
  for i in range(N):
    cc += conveyor(H[i], A[i], B[i])
  cc.sort(key=lambda c: c.h)

  # def findConveyors(cc: List[conveyor], ci: int, height: int, left: int, right: int) -> List[exposure]:
  ee = findConveyors(cc, 0, maxHeight, farthestLeft, farthestRight)
  ee += exposure(right, -1) # add terminating condition
  for ei in range(len(ee)-1):
    ci = ee[ei].c
    cleft = cc[ci].a
    cright = cc[ci].b
    eleft = ee[ei].x
    eright = ee[ei+1].x
    # exposure must always be a subset of the conveyor, because edge cases fall past
    # eee       eee       eee
    # cccccc ccccccccc cccccc

cc = List[conveyor(10,100000,600000), conveyor(20,400000,800000)]
print(f"cc={cc}")
ee = findConveyors(cc, 0, maxHeight, farthestLeft, farthestRight)
print(f"ee={ee}")
