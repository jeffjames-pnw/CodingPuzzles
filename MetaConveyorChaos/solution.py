# https://www.metacareers.com/profile/coding_puzzles?puzzle=280063030479374
# Congratulations, you solved 2 / 2 sample test cases! Click Submit next to make a full submission.
# We were unable to process your submission.

from typing import List

maxHeight = 1000000
farthestLeft = 0
farthestRight = 1000000

class conveyor:
  def __init__(self, h:int, a:int, b:int):
    self.h,self.a,self.b,self.f = h,a,b,False
  def __str__(self) -> str:
    return f"[h={self.h},a={self.a},b={self.b},f={self.f}]"

class exposure:
  def __init__(self, x:int, c:int):
    self.x,self.c = x,c
  def __str__(self) -> str:
    return f"[x={self.x},c={self.c}]"

# ---------------------------------------------------------------------------------------------------
# findConveyorsDrop(cc,ci,height,x) -> ci of next conveyor
# findConveyorsTop(cc,ci,height,left,right) -> [[x,ci]...] of exposed conveyors

def findConveyorDrop(cc, ci: int, height: int, x: int) -> int:
  # skip conveyors that at/above our height or not in this range
  while ci < len(cc) and (height <= cc[ci].h or cc[ci].b <= x or x <= cc[ci].a): 
    ci += 1
  return ci

def findConveyorsTop(cc, ci: int, height: int, left: int, right: int) -> []: # List[exposure]:
  # null range
  if left > right: 
    return []
  
  # skip conveyors that at/above our height or not in this range
  while ci < len(cc) and (height <= cc[ci].h or cc[ci].b <= left or right <= cc[ci].a): 
    ci += 1
  if ci == len(cc): # hits the floor
    e = exposure(left, -1)
    return [e]
  
  # recurse left of this platform
  result = [] # List[exposure]
  if left < cc[ci].a:
    ee = findConveyorsTop(cc, ci + 1, cc[ci].h, left, cc[ci].a) 
    result += ee
    # print(f"left ci={ci+1}, height={cc[ci].h}, left={left}, right={cc[ci].a} = [{','.join(map(str,ee))}]")
    left = cc[ci].a
    # + 1 # misses left edge of conveyor

  # hits the current platform
  result.append(exposure(left, ci))
  
  # recurse right of this platform
  if cc[ci].b < right:
    ee = findConveyorsTop(cc, ci + 1, cc[ci].h, cc[ci].b, right)
    result += ee
    # print(f"right ci={ci+1}, height={cc[ci].h}, left={cc[ci].b}, right={right} = [{','.join(map(str,ee))}]")
  return result

# ---------------------------------------------------------------------------------------------------
# expectedDistanceDrop(cc,ci,height,x) -> expected distance travelled after falling off a conveyor
# expectedDistance(cc,ee) -> expected distance for this configuration
# expectedDistanceRecurse(cc, ee, ci, results, ri) - fill results recursively through possibilities
# expectedDistanceBest(cc,ee) - pick the best conveyor to fix and aggregate the rest

def expectedDistanceDrop(cc, ci:int, h:int, x:int):
  d = 0
  ci = findConveyorDrop(cc, ci, h, x)
  while ci < len(cc):
    c = cc[ci]
    h = c.h # drop down to this height
    if c.f: # move forward to the right side
      d += c.b-x
      x = c.b
    else: # move backward to the left side
      d += x-c.a
      x = c.a
    ci = findConveyorDrop(cc, ci, h, x)
  return d

def expectedDistance(cc, ee):
  d = 0.0
  fullspan = farthestRight - farthestLeft
  for ei in range(len(ee)-1):
    ci = ee[ei].c
    if ci >= 0: # not already on the floor
      # exposure from above
      eleft = ee[ei].x
      eright = ee[ei+1].x
      ecenter = (eleft + eright)/2
      espan = eright - eleft

      # expected distance on this conveyor
      c = cc[ci]
      drop = 0.0
      cd = 0.0
      if c.f: # forward from center off the right end
        cd = 0.0 + c.b - ecenter
        drop = expectedDistanceDrop(cc, ci, c.h, c.b)
      else: # backward from center off the left end
        cd = 0.0 + ecenter - c.a
        drop = expectedDistanceDrop(cc, ci, c.h, c.a)
      # print(f"{c.f} ei={ei} ci={ci} cd={cd} drop={drop} espan={espan}")
      d += (cd + drop) * espan / fullspan
  return d    

def expectedDistanceRecurse(cc, ee, ci: int, results: [], ri: int):
  mask = 1 << ci
  if ci < len(cc):
    expectedDistanceRecurse(cc, ee, ci+1, results, ri)
    cc[ci].f = True
    expectedDistanceRecurse(cc, ee, ci+1, results, ri | mask)
    cc[ci].f = False
  else:    
    results[ri] = expectedDistance(cc,ee)

def expectedDistanceBest(cc,ee):
  max = 1 << len(cc)
  dd = [-1] * max
  expectedDistanceRecurse(cc, ee, 0, dd, 0)
  min = -1
  for ci in range(len(cc)):
    mask = 1 << ci
    tf = 0
    tb = 0
    for ri in range(max):
      if ri & mask == 0:
        tb += dd[ri]
      else:
        tf += dd[ri]
    if min < 0 or tb < min:
      min = tb
    if min < 0 or tf < min:
      min = tf
  return min / (1 << (len(cc)-1))

# ---------------------------------------------------------------------------------------------------

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
  cc = [] #  List[conveyor]
  for i in range(N):
    cc.append(conveyor(H[i], A[i], B[i]))
  cc.sort(key=lambda c: -c.h)

  # def findConveyorsTop(cc: List[conveyor], ci: int, height: int, left: int, right: int) -> List[exposure]:
  ee = findConveyorsTop(cc, 0, maxHeight, farthestLeft, farthestRight)
  return expectedDistanceBest(cc, ee)

# ---------------------------------------------------------------------------------------------------

def test1():
  print("hello world!")
  cc = [conveyor(10,100000,600000), conveyor(20,400000,800000)]
  cc.sort(key=lambda c: -c.h)
  print(f"cc=[{','.join(map(str,cc))}]")
  ee = findConveyorsTop(cc, 0, maxHeight, farthestLeft, farthestRight)
  print(f"ee=[{','.join(map(str,ee))}]")
  # print(f"findConveyors ci=0, height={maxHeight}, left={farthestLeft}, right={farthestRight}")

  cc[0].f, cc[1].f = True, False
  d2 = expectedDistance(cc,ee)
  cc[0].f, cc[1].f = True, True
  d3 = expectedDistance(cc,ee)
  print(F"known best: d2={d2} d3={d3}")
  d = expectedDistanceBest(cc, ee)
  print(f"ee=[{','.join(map(str,ee))}] d={d}")

# cc=[[h=20,a=400000,b=800000,f=True],[h=10,a=100000,b=600000,f=True]]
# C  H 0 1 2 3 4 5 6 7 8 9
# 0 20         ---------
# 1 10   -----------
#    h 001111112222222220
# c    xx111111000000000x
# ee=[[x=0,c=-1],[x=100001,c=1],[x=400001,c=0],[x=800000,c=-1]]
#         0       L150,R350     B200 L300/R200   0 = 250*0.3+200*0.4 = 155
# expected travel 0∗0.3+200,000∗0.4+((150,000+350,000)/2)∗0.3=155,000
# Expected Return Value = 155000.00000000

def test2():
  print("hello world!")
  cc = [conveyor(2,5000,7000), conveyor(8,2000,8000),conveyor(5,7000,11000), conveyor(9,9000,11000),conveyor(4,0,4000)]
  cc.sort(key=lambda c: -c.h)
  print(f"cc=[{','.join(map(str,cc))}]")
  ee = findConveyorsTop(cc, 0, maxHeight, farthestLeft, farthestRight)
  d = expectedDistanceBest(cc, ee)
  print(f"ee=[{','.join(map(str,ee))}] d={d}")

# cc=[[h=9,a=9000,b=11000,f=True],[h=8,a=2000,b=8000,f=True],[h=5,a=7000,b=11000,f=True],[h=4,a=0,b=4000,f=True],[h=2,a=5000,b=7000,f=True]]
# C H 0 1 2 3 4 5 6 7 8 9 A B
# 0 9                   -----
# 1 8     -------------
# 2 5               ---------
# 3 4 ---------
# 4 2     -----------
#   h 44442222222222225559999
# c   33331111111111112220000
# ee=[[x=0,c=3],[x=2001,c=1],[x=8000,c=2],[x=9001,c=0],[x=11000,c=-1]] d=183.86399999999998 was d=46.492999999999995
# Expected Return Value = 36.50000000
