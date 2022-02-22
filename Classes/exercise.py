class Introducer:
  
  def __init__(self, name):
    self.name = name

  def announce(self):
    return f'I am {self.name}!'

  def introduce(self, str):
    return f'Hello {str}, I am {self.name}!'

introducer = Introducer("Sonali")
print(introducer.announce())
print(introducer.introduce("Sapna"))

    