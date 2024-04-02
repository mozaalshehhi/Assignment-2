from location import Location #importing because of the comp relation we have i THINK..
class Artwork:
    def __init__(self, title, artist, dateOfCreation, historicalSignificance, locationType, locationName):
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        #based on the uml I did there is a composition relation between artwork and location since every artwork has a location
        self.location = Location(locationType, locationName)#for this to work make sure to import location from Location!!
    def displayInfo(self):#attributes of the artwork!
        print("the artwork informations: ")
        print(f"title--> {self.title}")
        print(f"atrists--> {self.artist}")
        print(f"date of creation--> {self.dateOfCreation}")
        print(f"the history significance--> {self.historicalSignificance}")
        print("location--> ")
        print(f"type--> {self.locationType}")
        print(f"name--> {self.locationNmae}")
