class Visitor: #in my uml this class has aggrigation relationship with the Ticket class since the visitor can buy many ticket but the ticket is for only one single visitor if that makes a point/since
    def __init__(self, name, age, visitorType):
        self.name = name
        self.age = age
        self.visitorType = visitorType
        self.tickets = []#the list becasue we can have many tickets for one visitor since he can go to a tour, exhibition, or a special event tickets.

    def buyTicket(self, ticket):
        self.tickets.append(ticket)#like what we did in location.py
        ticket.setVisitor(self)

