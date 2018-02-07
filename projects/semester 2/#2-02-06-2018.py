def encoder(message):
  string=''
  for i in message:
    string = string + str((ord(i))) + ' '
  print(string)
