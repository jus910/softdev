
def string_times(str, n):
  return str*n

print(string_times('Hi', 2))

def string_bits(str):
  new_str = ''
  for i in range(0,len(str),2):
    new_str += str[i:i+1]
  return new_str

print(string_bits('Hello'))

def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    new_str+=str[:i+1]
  return new_str

print(string_splosion('jerry'))

def front_times(str, n):
  return str[:3] * n
print(front_times('Chocolate', 2))

def last2(str):
  count = 0
  index = 0
  while index < len(str)-2 :
    if str[-2:] == str[index:index+2]:
      count += 1
    index +=1 
  return count
print(last2('hixxhi'))

def array_count9(nums):
  index = 0
  count = 0
  while index < len(nums):
    if nums[index] == 9:
      count += 1
    index +=1
  return count

print(array_count9([1, 2, 9]))

def array_front9(nums):
  index = 0
  while index < len(nums):
    if nums[index] == 9 and index < 4:
      return True
    index +=1
  return False

print(array_front9([1, 2, 9, 3, 4]))

def array123(nums):
  i = 0
  while i < len(nums):
    if [1,2,3] == nums[i:i+3]:
      return True
    i += 1
  return False
array123([1, 1, 2, 3, 1])

def string_match(a, b):
  count = 0
  index = 0
  while index < min(len(a),len(b))-1:
    if a[index:index+2] == b[index:index+2]:
      count += 1
    index += 1
  return count
print(string_match('xxcaazz', 'xxbaaz'))
