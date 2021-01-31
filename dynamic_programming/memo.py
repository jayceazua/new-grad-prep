# def gridTravel(m, n, memo={}):

#     key = tuple((m, n))
#     if key in memo:
#         return memo[key]

#     if m == 1 and n == 1:
#         return 1

#     if m == 0 or n == 0:
#         return 0
#     # down, right
#     memo[key] = gridTravel(m - 1, n, memo) + gridTravel(m, n - 1, memo)

#     return memo[key]

# slow program > wrong program
# print(gridTravel(1, 1))
# print(gridTravel(2, 3))
# print(gridTravel(3, 3))
# print(gridTravel(18, 18))


def canSum(targetSum, nums, memo={}):
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


def howSum(t, nums, memo={}):

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


def bestSum(target, nums, memo={}):

    if target in memo:
        return memo[target]

    if target is 0:
        return []

    if target < 0:
        return None

    shortest = None

    for num in nums:
        remainder = target - num
        result = bestSum(remainder, nums, memo)
        if result is not None:
            combo = result + [num]
            if shortest is None or len(combo) < len(shortest):
                shortest = combo

    memo[target] = shortest
    return shortest

# print(bestSum(7, [5, 3, 4, 7]))
# print(bestSum(8, [2, 3, 5]))
# print(bestSum(8, [1, 4, 5]))
# print(bestSum(100, [1, 2, 5, 25]))


def canConstruct(target, wordbank, memo={}):
    if target in memo:
        return memo[target]

    if target is "":
        return True

    for word in wordbank:
        if target.find(word) is 0:

            suffix = target[len(word):]

            if canConstruct(suffix, wordbank, memo):
                memo[target] = True
                return memo[target]

    memo[target] = False
    return memo[target]


# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

def countConstruct(target, wordbank, memo={}):

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0
    for word in wordbank:

        if target.find(word) is 0:
            suffix = target[len(word):]
            totalCount += countConstruct(suffix, wordbank, memo)

    memo[target] = totalCount
    return memo[target]


# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))


def allConstruct(target, wordbank):
  if target == "":
    return [[]]

  result = []

  for word in wordbank:
    if target.find(word) == 0:
      suffix = target[len(word):]
      suffixWays = allConstruct(suffix, wordbank)
      targetWays = list(map(lambda way: [word, way], suffixWays))
      result += targetWays
  
  return result


# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


def fib_tab(n):
    # build table with initial values
    dp = [0 for i in range(n + 1)]
    # seed a default value
    dp[1] = 1

    # iterate through the table
    for i in range(n + 1):
        # fill further positions based on the current position
        if i + 1 <= n:
            dp[i + 1] += dp[i]
        if i + 2 <= n:
            dp[i + 2] += dp[i]
    return dp[n]

# print(fib_tab(6))
# print(fib_tab(8))


def gridTravel_tab(m, n):
    # visualize the problem as a table
    # size the table based on the inputs
    # initialize the table with default values
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # seed the trivial answer into the table
    dp[1][1] = 1
    print("Table:", dp)

    # iterate through the table
    for row in range(m + 1):
        for col in range(n + 1):
            current = dp[row][col]
            # fill further positions based on the current position
            if col + 1 <= n:
                dp[row][col + 1] += current
            if row + 1 <= m:
                dp[row + 1][col] += current
    print("Table:", dp)
    return dp[m][n]


# print(gridTravel_tab(3, 3)) # 6

def canSum_tab(k, nums):
    dp = [False for _ in range(k + 1)]
    dp[0] = True

    for i in range(k + 1):
        if dp[i] == 0:
            for num in nums:
                    if (i + num) <= k:
                        dp[i + num] = True
    
    return dp[k]


# print(canSum_tab(7, [2, 3]))
print(canSum_tab(7, [5, 3, 4, 7]))
print(canSum_tab(7, [2, 4]))
print(canSum_tab(8, [2, 3, 5]))
