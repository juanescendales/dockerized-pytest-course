from typing import Tuple


class Point():
    def __init__(self,city : str ,latitude : float ,longitude : float):
        if(latitude < -90 or latitude > 90 or longitude < -90 or longitude > 90):
            raise ValueError("Not valid latitude or longitude")
        self._city = city
        self._latitude = latitude
        self._longitude = longitude
    
    #Property : city
    @property
    def city(self) -> str:
        return self._city
    
    @city.setter
    def city_setter(self,value : str) -> None:
        self._city = value

    #Property : latitude
    @property
    def latitude(self) -> float:
        return self._latitude
    
    @latitude.setter
    def city_setter(self, value : float) -> None:
        self._latitude = value

    #Property : longitude
    @property
    def longitude(self) -> float:
        return self._longitude
    
    @longitude.setter
    def city_setter(self, value : float) -> None:
        self._city = value
    
    #Property: latitude_and_longitude
    @property
    def latitiude_longitude(self)->Tuple[float,float]:
        return (self.latitude, self.longitude)