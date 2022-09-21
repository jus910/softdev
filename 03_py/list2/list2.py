def count_evens(nums):
  ans = 0
  for n in nums:
    if n % 2 == 0:
      ans += 1
  return ans

def big_diff(nums):
  #one liner
  return max(nums) - min(nums)

def centered_average(nums):
  return (sum(nums)-min(nums)-max(nums))/(len(nums)-2)

def sum13(nums):
  index=0
  summmm=0
  while index<len(nums):
    if nums[index] == 13:
      index+=2
    else:
      summmm+=nums[index]
      index+=1
  return summmm

def sum67(nums):
  #state variable
  inside_67=False
  i = 0
  sum = 0
  while i < len(nums):
    if nums[i] == 6:
      inside_67 = True
    elif not inside_67:
      sum += nums[i]
    elif nums[i] == 7:
      inside_67 = False
    i+= 1
  return sum

def has22(nums):
  index = 0
  while index < len(nums)-1:
    if nums[index] == 2 and nums[index + 1] == 2:
      return True
    index += 1
  return False
    

print(count_evens([2, 1, 2, 3, 4]))
print(big_diff([10, 3, 5, 6]))
print(centered_average([1, 2, 3, 4, 100]))
print(sum13([1, 2, 2, 1]))
print(sum67([1, 2, 2]))
print(has22([1, 2, 2]))