class Reminder:

  def __init__(self, name):
    self.name = name
    
  def remind_me_to(self, work):
    self.work = work

  def remind(self):
    return f'{self.name}! {self.work}!'

reminder = Reminder("Sonali")

reminder.remind_me_to("Walk the dog")

print(reminder.remind())