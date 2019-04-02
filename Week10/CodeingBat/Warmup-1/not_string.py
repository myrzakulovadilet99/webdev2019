def not_string(str):
  s = str.split()
  if s[0]=='not':
    return str
  else:
    return 'not '+str