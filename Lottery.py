import operator
from random import randint
from collections import defaultdict
from Ticket import Ticket

"""
  Lottery stores tickets, runs tallys and picks winning numbers.
"""
class Lottery(object):

  # Singleton class
  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, '_lottery'):
      cls._lottery = super(Lottery, cls).__new__(cls, *args, **kwargs)
    return cls._lottery

  # basic init
  def __init__(self, tickets=[]):
    self.tickets = tickets
    self.tally = defaultdict(int)
    self.tallyPowerball = defaultdict(int)
    self.picks = []
    self.powerballs = []

  # Add ticket to ticket store
  def addTickets(self, tickets):
      self.tickets.append(tickets)

  # pick top numbers
  def topNumbers(self):
    previous = 0
    t = []
    topNumbers = []
    for key, value in sorted(self.tally.items(), key=operator.itemgetter(1), reverse=True):
      if previous > value:
        topNumbers.append(t)
        t = []
      t.append(key)
      previous = value
    topNumbers.append(t)
    for s in topNumbers:
      if len(s) == 1:
        self.picks.append(s[0])
      else:
        self.picks.append(s[randint(0,len(s)-1)])

  # pick remaining winning numbers
  def fillIn(self):
    for pick in xrange(5-len(self.picks)):
      self.picks.append(str(randint(0,64)))

  # pick winning powerball number
  def pickPowerball(self):
    previous = 0
    powerball = 0
    picks = []
    for key, value in sorted(self.tallyPowerball.items(), key=operator.itemgetter(1), reverse=True):
      if previous > value:
        break
      else:
        picks.append(key)
        previous = value
    if (len(picks) == 1):
      self.powerball = picks[0]
    else:
      self.powerball = picks[randint(0,len(picks)-1)]

  # Tally or count numbers on powerball tickets
  def tallyTickets(self):
    self.tally = defaultdict(int)
    self.tallyPowerball = defaultdict(int)
    for ticket in self.tickets:
      for number in ticket.numbers:
        self.tally[str(number)] += 1
      self.tallyPowerball[str(ticket.powerball)] += 1

  # print entered ticket info.
  def printTickets(self):
    numbers = ""
    for ticket in self.tickets:
      print("{0} {1} {2} {3} {4} {5} {6} Powerball: {7}".format(
        ticket.fname,
        ticket.lname,
        ticket.numbers[0],
        ticket.numbers[1],
        ticket.numbers[2],
        ticket.numbers[3],
        ticket.numbers[4],
        ticket.powerball))

  # Run lottery, talley, selection and remaining numbers.
  def runLottery(self):
    self.printTickets()
    self.tallyTickets()
    self.topNumbers()
    self.fillIn()
    self.pickPowerball()

if __name__ == '__main__':
  lotto = Lottery()
  t1 = Ticket()
  t1.addNumber(10)
  t1.addNumber(12)
  t1.addNumber(13)
  t1.addNumber(14)
  t1.addNumber(15)
  t1.addNumber(16)
  t1.addPowerball(18)
  lotto.addTickets(t1)
  t1 = Ticket()
  t1.addNumber(10)
  t1.addNumber(12)
  t1.addNumber(23)
  t1.addNumber(54)
  t1.addNumber(62)
  t1.addNumber(16)
  t1.addPowerball(20)
  lotto.addTickets(t1)
  t1 = Ticket()
  t1.addNumber(10)
  t1.addNumber(40)
  t1.addNumber(41)
  t1.addNumber(42)
  t1.addNumber(43)
  t1.addNumber(44)
  t1.addNumber(45)
  t1.addPowerball(23)
  lotto.addTickets(t1)
  lotto.runLottery()
  print lotto.picks
  print lotto.powerball
