class Location:
    def __init__(self, locationType, name):#constructor method to inicilize the location!
        self.locationType = locationType
        self.name = name
        #the artwors that is in each location so in the location we have an artwork
        self.artworks = []#this is the empty list attribute so that we can stor or put artworks,
        # objects, it is in the location.py because artwork is a comp relation with location where artwork is within location
    def putArtwork(self, artwork):#adding artworks to the list
        self.artworks.append(artwork)#append so add the artwork object to the list. Attributes ""of loc obj""...
#then we can make an artwork obj that has the location type and name in it as well but in this assignment we need it from user input.
#this step is done in test.py!!