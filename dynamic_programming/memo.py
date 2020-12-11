def gridTravel(m, n, memo={}):

    key = tuple((m, n))
    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0
    # down, right
    memo[key] = gridTravel(m - 1, n, memo) + gridTravel(m, n - 1, memo)

    return memo[key]

# slow program > wrong program
# print(gridTravel(1, 1))
# print(gridTravel(2, 3))
# print(gridTravel(3, 3))
# print(gridTravel(18, 18))

def canSum(targetSum, nums, memo = {}):
    """
      Write a function that takes in a targetSum and an array of numbers as arguments. 
      The function should return a boolean indicating whether or not it is possible 
        to generate the targetSum using numbers from the array.
      You may use an element of the array as many times as needed. You may assume 
        all input numbers are non-negative.
    """
    if targetSum in memo:
      return memo[targetSum]

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in nums:

        remainder = targetSum - num

        if canSum(remainder, nums, memo) == True:
          memo[targetSum] = True
          return True


    memo[targetSum] = False
    return False

# print(canSum(7, [2, 3]))
# print(canSum(7, [2, 4]))
# print(canSum(300, [7, 14]))

def howSum(t, nums, memo = {}):

  if t in memo:
    return memo[t]

  if t == 0:
    return []
  
  if t < 0:
    return None

  for num in nums:
    remainder = t - num

    result = howSum(remainder, nums, memo)

    if result != None:
      memo[t] = result + [num]
      return memo[t]

  memo[t] = None
  return None

# print(howSum(7, [2, 3]))
# print(howSum(7, [5, 3, 4, 7]))
# print(howSum(8, [2, 3, 5]))
# print(howSum(300, [7, 14]))

def bestSum(target, nums):
  if target is 0:
    return []
  
  if target < 0:
    return None

  shortest = None

  for num in nums:
    remainder = target - num
    result = bestSum(remainder, nums)
    if result is not None:
      combo = result + [num]
      if shortest is None or len(combo) < len(shortest):
        shortest = combo
      
  
  return shortest

print(bestSum(7, [5, 3, 4, 7]))
# print(bestSum(8, [2, 3, 5]))
# print(bestSum(8, [1, 4, 5]))
# print(bestSum(100, [1, 2, 5, 25]))
