from collections import Counter, deque, namedtuple

class Ticket(object):

  numbers = []
  def __init__(self):
    self.powerballRange = [1,26]
    self.range = [1,64]
    self.numbers = [ ]
    self.powerball = 0;
    self.fname = ""
    self.lname = ""

  def isInPowerballRange(self, number):
    return number >= self.powerballRange[0] and number <= self.powerballRange[1]

  def isInRange(self, number):
    return number >= self.range[0] and number <= self.range[1]

  def isDuplicate(self, number):
    return number in self.numbers

  def isFilled(self):
      return len(self.numbers) >= 4 and self.powerball != 0

  def isPowerBallEntry(self):
      return len(self.numbers) >= 4 and self.powerball == 0

  def addNumber(self, number):
    if len(self.numbers) < 5:
      if not self.isDuplicate(number):
        if self.isInRange(number):
          self.numbers.append(number)
          return 0
        else:
          print("Number out of range.")
      else:
        print("Duplicate number, please select another number.")
    return -1

  def addPowerball(self, number):
    if self.isInPowerballRange(number):
      self.powerball = number
      return 0
    return -1

  def numberDeque(self):
    return deque(self.numbers)

if __name__ == '__main__':
  ticket = Ticket()
  print (ticket.addNumber(21))
  print (ticket.addNumber(26))
  print (ticket.addNumber(24))
  print (ticket.addNumber(23))
  print (ticket.addNumber(31))
  print (ticket.addNumber(46))
  print (ticket.addNumber(54))
  print (ticket.addNumber(23))
  print(ticket.addPowerball(21))
  print("Numbers: {0} and powerball {1}".format(ticket.numbers, ticket.powerball))
