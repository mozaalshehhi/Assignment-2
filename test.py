#importing
from datetime import date #the yyyy-mm-dd format!
from artwork import Artwork
from visitor import Visitor
from ticket import TourTicket, ExhibitionTicket, SpecialEventTicket
from location import Location
from exhibition import Exhibition
from tour import Tour
from special_event import SpecialEvent
from ticket import Ticket

def makeArtwork():#making a function that will make for us the artwork obj by having the input from user?

    try:
        title = input("write artwork title--> ")
        artist = input("write the artists name--> ")
        dateOfCreation = input("write the date of creation as (yyyy-mm-dd)-->")
        dateOfCreation = date.fromisoformat(dateOfCreation)  # make sure to import
        historicalSignificance = input("write historical significance-->")
        locationType = input("write the location type--> ")
        locationName = input("write the location name--> ")
        # now the final we will get from the user input will have all the above so we will have artwork obj and the location name and type as well
      # , since it is a composition relationship! And it is basically making a,
       # location obj in the constructor of the artwork as shown in location.py I think
        artwork = Artwork(title, artist, dateOfCreation, historicalSignificance, locationType, locationName)
        return artwork
    except ValueError as e:
        print("error--> ", e)




#now the function that makes visitorr object with the inputs of the user
def makeVisitor():
    try:

        name = input("write the visitors name--> ")
        age = int(input("write the age of visitors--> "))
        visitorType = input("write visitor type--> ")
        visitor = Visitor(name, age, visitorType)#make sure to import visitor
        return visitor
    except ValueError as e:
        print("error--> ", e)

#now the ticket so a function to make ticket objects by the users input again
def makeTicket():#remember that we have 3 more types of tickets that inheret from the parent Ticket
    try:
        price = float(input("write the ticket price--> "))
        buyDate = input("write the date of buying as (yyyy-mm-dd)-->")
        buyDate = date.fromisoformat(buyDate)
        ticketType = input("write one ticket type from each *Tour/Exhibition/Special Event*--> ")
        if ticketType.lower() == "tour":#.lowe converts the user input to all small letters so that if they write in cap it does not count wrong
            tourDate = input("write tour date (yyyy-mm-dd)--> ")
            tourDate = date.fromisoformat(tourDate)#
            guide = input("write guide name--> ")
            maxCapacity = int(input("write maximum number of visitors entering--> "))
            ticket = TourTicket(price, buyDate, guide, maxCapacity) #make sure to import TourTicket
        elif ticketType.lower() == "exhibition":
            exhibitionName = input("write exhibition name--> ")
            ticket = ExhibitionTicket (price, buyDate, exhibitionName)#make sure to import ExhibitionTicket
        elif ticketType.lower() == "special event":
            eventName = input("write event name--> ")
            eventDate = input("write the date of event as (yyyy-mm-dd)--> ")
            eventDate = date.fromisoformat(eventDate)
            ticket = SpecialEventTicket(price, buyDate, eventName, eventDate)#make sure to import SpecialEventTicket
        else:
            raise ValueError("not the correct ticket types")
        return ticket
    except ValueError as e:
        print("error--> ", e)

#function for making the exhibition objs from users inputs
def makeExhibition():
    try:

        name = input("write the name of the exhibition--> ")
        startDate = input("write the starting date as (yyyy-mm-dd)--> ")
        startDate = date.fromisoformat(startDate)
        endDate = input("write the ent date as (yyyy-mm-dd)--> ")
        endDate = date.fromisoformat(endDate)
        locationType = input("write location type--> ")
        locationName = input("write the location name so if it is permanent galleries, exhibition halls, or outdoor spaces.--> ")
        location = Location(locationType, locationName)#make sure to import location
        exhibition = Exhibition(name, startDate, endDate, location)#make sure to import exhibition
        return exhibition
    except ValueError as e:
        print("error--> ", e)

#for the tour
def makeTour():
    try:
        tourDate = input("write the date of the tour as (yyyy-mm-dd)--> ")
        tourDate = date.fromisoformat(tourDate)
        guide = input("write guides name--> ")
        maxCapacity = input("write the number of the maximum visitors that can attend the tour--> ")
        tour = Tour(tourDate, guide, maxCapacity)#make sure to import Tour
        return tour
    except ValueError as e:
        print("error--> ", e)


#now the last one which is the special event function
def makeSpecialEvent():
    try:

        name = input("write events name--> ")
        eventDate = input("write the events date as (yyyy-mm-dd)--> ")
        eventDate = date.fromisoformat(eventDate )
        locationType = input("write the type of location--> ")
        locationName = input("write the locations name--> ")
        price = float(input("write the events price--> "))
        location = Location(locationType, locationName)#make sure to import location
        event = SpecialEvent(name, eventDate, location, price)#make sure to import SpecialEvent
        return event
    except ValueError as e:
        print("error--> ", e)


#now we will make a main one that will show the user the functions objects above so that they can pick which one to test and add an input to!
def main():
    while True:#here the while loop keeps going till we reach base case or exit.
        print("\n Pick One--> ")
        print("0, make Artwork--> ")
        print("1, make Visitor--> ")
        print("2, make Ticket--> ")
        print("3, make Exhibition--> ")
        print("4, make Tour--> ")
        print("5, make Special Event--> ")
        print("6, Exiting!--> ")
        opt = input("writr your pick--> ")
        if opt == "0":
            artwork = makeArtwork()
            if artwork:
                print("the artwork is done!", artwork.__dict__)
        elif opt == "1":
            visitor = makeVisitor()
            if visitor:
                print("the visitor is done!", visitor.__dict__)
        elif opt == "2":
            ticket = makeTicket()
            if ticket:
                print("the ticket is done!", ticket.__dict__)
        elif opt == "3":
            exhibition = makeExhibition()
            if exhibition:
                print("the exhibition is done!", exhibition.__dict__)
        elif opt == "4":
            tour = makeTour()
            if tour:
                print("the tour is done!", tour.__dict__)
        elif opt == "5":
            event = makeSpecialEvent()
            if event:
                print("the event  is done!", event.__dict__)
        elif opt == "6":
            print("stop the while loop and exit!")
            break
        else:
            print("wrong try the inputs again!")

if __name__ == "__main__":
    main()



