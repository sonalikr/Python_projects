def add_five(num):
  return num + 5

def subtract_low_from_high(num1, num2):
  if num1 < num2:
    return num2 - num1
  else:
    return num1 - num2


print(add_five(subtract_low_from_high(1463, 16475)))
