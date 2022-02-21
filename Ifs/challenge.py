import time

seconds = int(time.time())
print(seconds)

if seconds % 15 == 0:
  print("FizzBuzz")
elif seconds % 5 == 0:
  print("Buzz")
elif seconds % 3 == 0:
  print("Fizz")
else:
  print(seconds)
