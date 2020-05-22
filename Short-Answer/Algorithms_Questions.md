# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I'm going to try this in psuedocode:

def dropegg(egg, floor):
  #drop egg off building
  does egg == broken?
  if egg broken
    return true
  return false

def eggdropper(floors, egg):
#determine the floor it is safe to drop eggs from, the highest floor
#where they dont break


  breakingfloor = 0

  breaking_floor_found = false

  for i in range(floors):
  while not breaking_floor_found:
    if droppedegg(egg, i): # see if egg breaks when dropped on current floor
    breakingfloor = i
    breaking_floor_found = true

    safefloor = [i for i in floors:breakingfloor - 1] 
    
     #make the safe floors #range the first floor all the way up to the floor previous to the egg #breaking floor

  return safe_floors

  #Now you know where you can drop eggs from without them breaking. The time for this equation is O(n) in the worst case. 

  #I could also imagine a scenario where binary sort is possible, because floors are always sorted, one could start in the middle (floor 10 lets say), drop the egg, if it breaks, half that, drop the egg at floor 5, etc.  The worst case scenario for this method would be O(log of n) 


