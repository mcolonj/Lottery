from Ticket import Ticket
from Lottery import Lottery

"""
  Interface - for console input
"""
class Interface(object):

  def __init__(self):
    self.option = 'ticket'
    self.positional = ['1st', '2nd', '3rd', '4th', '5th']

  # input powerball tickets
  def ticket(self, ticket):
    if ticket.fname == None or ticket.fname == "":
      fname = raw_input("Enter your first name: ")
      ticket.fname = fname
    elif ticket.lname == None or ticket.lname == "":
      lname = raw_input("Enter your last name: ")
      ticket.lname = lname
    elif len(ticket.numbers) < 5:
      excluding = ""
      e = ""
      if len(ticket.numbers) > 0:
        excluding = "excluding "
        for n in ticket.numbers:
          e = e+str(n)+", "
      number = raw_input("Select {0} # (1 thru 69 {1} {2}): ".format(self.positional[len(ticket.numbers)], excluding, e))
      if not number:
        print ("please enter a number")
      else:
        number = int(number)
      if (number):
          ticket.addNumber(number)
    elif ticket.powerball == None or ticket.powerball == 0:
      number = int(raw_input("Select Powerball # (1 thru 26): "))
      ticket.addPowerball(number)

if __name__ == '__main__':
  interface = Interface()
  ticket = Ticket()
  lottery = Lottery()
  interface.option = 'ticket'
  while interface.option != "":
    # Input ticket information
    if interface.option == 'ticket':
      interface.ticket(ticket)
      if ticket.fname and ticket.lname and len(ticket.numbers) == 5 and ticket.powerball > 0:
        lottery.addTickets(ticket)
        ticket = Ticket()
        print("")
        i = raw_input("Do you want to continue adding numbers? [y,n]")
        print("")
        if i == 'n': interface.option = 'pick'
    # Run lottery tickets
    elif interface.option == 'pick':
      print("")
      lottery.runLottery()
      interface.option = ''
      print("")
      print("Powerball Winning Numbers: ")
      print("{0} {1} {2} {3} {4} powerball: {5}".format(
        lottery.picks[0],
        lottery.picks[1],
        lottery.picks[2],
        lottery.picks[3],
        lottery.picks[4],
        lottery.powerball
      ))
