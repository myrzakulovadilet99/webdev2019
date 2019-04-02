def front_back(str):
  n = len(str)
  s = ""
  if len(str)<=1:
    return str
  else:
    for i in range(len(str)):
      if i>0 and i<len(str)-1:
        s+=str[i]
    return str[n-1]+s+str[0]
