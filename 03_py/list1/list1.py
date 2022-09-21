def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  if len(nums) <1 :
    return False
  return nums[0] == nums[-1]

def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  max_num = max(nums[0],nums[2])
  return [max_num] * 3

def sum2(nums):
  if len(nums)==0:
    return 0
  elif len(nums) < 2:
    return nums[0]
  return nums[1]+nums[0]

print(rotate_left3([1, 2, 3]))
print(reverse3([1, 2, 3]))
print(max_end3([1, 2, 3]) )
print(sum2([1, 2, 3]) )