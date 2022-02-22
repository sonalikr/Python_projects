def generate(upto):
  return "1"

def fizzbuzz(i):
  if i % 15 == 0: 
    return "FizzBuzz"
  elif i % 5 == 0:
    return "Buzz" 
  elif i % 3 == 0:
    return "Fizz"
  else:
    return i
  

print(fizzbuzz(90))

