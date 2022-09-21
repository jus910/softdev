def sleep_in(weekday, vacation):
  if weekday == False:
    return True
  elif vacation == True:
    return True
  else: 
    return False

print(sleep_in(False, False))

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile: 
    return True 
  else: 
    return False

print(monkey_trouble(True, True))

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  return a+b

print(sum_double(1, 2) )

def diff21(n):
  if n>21:
    return 2*(n-21)
  return 21-n

print(diff21(19))

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))

def makes10(a, b):
  return a+b==10 or a==10 or b==10

print(makes10(9, 10))

def near_hundred(n):
  if (abs(100 - n)) <= 10:
    return True
  elif (abs(200 - n)) <=10: 
    return True
  else:
    return False

print(near_hundred(93))

def pos_neg(a, b, negative):
  if negative:
    return a<0 and b<0
  return (a<0 and b>0) or (a>0 and b<0)

print(pos_neg(1, -1, False) )

def not_string(str):
  if str[:3] == "not": 
    return str
  return "not " + str

print(not_string('candy'))

def missing_char(str, n):
  return str[:n] + str[n+1:]

print(missing_char('kitten', 1))

def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1:] + str[1:len(str)-1] + str[0:1]

print(front_back('code'))

def front3(str):
  if len(str) < 3:
    return str * 3
  return str[:3] * 3

print(front3('Java'))

print(not_string("jerry"))
