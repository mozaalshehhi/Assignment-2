class Ticket: #this class hase inheretenc and aggrigation relationships
    def __init__(self, price, buyDate, ticketType):
        self. price = price
        self. buyDate = buyDate
        self. ticketType = ticketType
        self. visitor = None #the aggrigation that we talked about is with visitor class in visitor.py
        #the ticket is an aggrigation association with only one visitor
    def setVisitor(self, visitor):#the one in visitor.py
        from visitor import Visitor
        if not isinstance(visitor, Visitor):#isinstance(__obj, __class_or_tuple)
            raise ValueError("not the correct objects visitors")
        self.visitor = visitor
    def displayTicketInfo(self):
        print(f" ticket type--> {self.ticketType}")
        print(f"price--> {self.price}")
        print(f"buy date--> {self.buyDate}")
        if self.visitor:
            print(f"visitor--> {self.visitor.name}")

        # making sure to use overriding (refrence is session 24 polymorphism vidio recording (0:21:41 - 0:23:10)
        #make sure to import visitor as well..
class TourTicket(Ticket):#here is the inheretence relatioship we have 3 of them
    def __init__(self, price, buyDate, tourDate, guide, maxCapacity):#add the ticket and tourticket attributes
        super().__init__(price, buyDate, "Tour")
        self.tourDate = tourDate
        self.guide = guide
        self.maxCapacity = maxCapacity

    def displayTicketInfo(self):
        super().displayTicketInfo()
        print(f"tour date--> {self.tourDate}")
        print(f"guid--> {self.guide}")
        print(f"max Capacity--> {self.maxCapacity}")
class ExhibitionTicket(Ticket):#repeat as above
    def __init__(self, price, buyDate, exhibitionName):
        super().__init__(price, buyDate, "Exhibition")
        self.exhibitionName = exhibitionName

    def displayTicketInfo(self):
        super().displayTicketInfo()
        print(f"exhibition Name--> {self.exhibitionName}")

class SpecialEventTicket(Ticket):#do it all again!
    def __init__(self, price, buyDate, eventName, eventDate):
        super().__init__(price, buyDate, "Special Event")
        self.eventName = eventName
        self.eventDate = eventDate

    def displayTicketInfo(self):
        super().displayTicketInfo()
        print(f"event Name--> {self.eventName}")
        print(f"event date--> {self.eventDate}")

