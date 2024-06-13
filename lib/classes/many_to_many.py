class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.__hometown = None
        self.hometown = hometown
        self.__concerts = []
        

    #Band name property
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, band_name):
        if not isinstance(band_name, str) or len(band_name) <= 0:
            raise ValueError("Band name must be non-empty string!!")
        else:
            self._name = band_name

    #Band's hometown property
    @property
    def hometown(self):
        return self.__hometown 

    @hometown.setter
    def hometown(self,band_hometown):
        if self.__hometown is not None:
            raise AttributeError("Hometown cannot be modified")
        if not isinstance(band_hometown, str) or len(band_hometown) <= 0:
            raise ValueError("Hometown must be none-empty string")
        self.__hometown = band_hometown
        
        
             

    def concerts(self):
        return [concert for concert in Concert.all if concert.band is self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue,  date):
        concert = Concert(date, self, venue)
        self.__concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts() if concert.introduction()]


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    #Concert date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str) or len(date) <= 0:
            raise ValueError("Date must be of type string or greater than zero characters")
        self._date = date 

    @property
    def band(self):
        return self._band 

    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise ValueError("Object must be of type Band")
        self._band = band

    @property
    def venue(self):
        return self._venue 

    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise ValueError("Object must be of type Venue")
        self._venue = venue


    def hometown_show(self):
        return  self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,venue_name):
        if not isinstance(venue_name, str) or len(venue_name) <= 0:
            raise ValueError("Venue name must be non-empty string")
        self._name = venue_name

    @property
    def city(self):
        return self._city 
    @city.setter
    def city(self, city):
        if not isinstance(city, str)or len(city) <= 0:
            raise ValueError("City must be non-empty string!!")
        self._city = city        

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})
