my_list = ["Cat", "Mouse", "Frog"]
my_list.remove("Mouse")
my_list.insert(0,"Mouse")
my_list.insert(1, "Lynx")
print(my_list)

my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

for animal in my_list:
  changed_animal = animal.lower()

  if changed_animal in counters:
    counters[changed_animal] = counters[changed_animal] + 1
  else:
    counters[changed_animal] = 1

print(counters)