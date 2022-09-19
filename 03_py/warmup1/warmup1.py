def not_string(str):
  if str[:3] == "not": 
    return str
  return "not " + str


def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1:] + str[1:len(str)-1] + str[0:1]

def front3(str):
  if len(str) < 3:
    return str * 3
  return str[:3] * 3
  
print(not_string("jerry"))
