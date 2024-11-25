class Device:
    def __init__(self, brand, battery_capacity):
        self._brand = brand  
        self._battery_capacity = battery_capacity

    def get_info(self):
        return f"{self._brand} Device with {self._battery_capacity}mAh battery"

class Smartphone(Device):
    def __init__(self, brand, battery_capacity, model, camera_mp):
       
        super().__init__(brand, battery_capacity)
        
        self.__model = model  
        self.camera_mp = camera_mp 
        self.__is_on = False  
   
    def power_toggle(self):
        self.__is_on = not self.__is_on
        status = "on" if self.__is_on else "off"
        print(f"{self._brand} {self.__model} is now {status}")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Model: {self.__model}, Camera: {self.camera_mp}MP"

    
    def take_photo(self):
        if self.__is_on:
            print(f"Capturing photo with {self.camera_mp}MP camera")
        else:
            print("Phone is turned off. Cannot take photo.")

iphone = Smartphone("Apple", 3500, "iPhone 13", 12)
samsung = Smartphone("Samsung", 4000, "Galaxy S21", 64)

print(iphone.get_info())
iphone.power_toggle() 
iphone.take_photo()