class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def make_call(self, phone_number):
        if self.battery_percentage > 0:
            print(f"Calling {phone_number} from {self.brand} {self.model}...")
            self.battery_percentage -= 5
        else:
            print("Battery is too low to make a call.")

    def charge(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"{self.brand} {self.model} charged to {self.battery_percentage}%.")

# Creating an object of Smartphone class
phone = Smartphone("Apple", "iPhone 13", 50)
phone.make_call("123-456-7890")
phone.charge(30)
phone.make_call("987-654-3210")

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, camera_megapixels):
        super().__init__(brand, model, battery_percentage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.battery_percentage > 0:
            print(f"Taking a photo with {self.camera_megapixels} MP camera.")
            self.battery_percentage -= 3
        else:
            print("Battery is too low to take a photo.")

# Creating an object of SmartphoneWithCamera class
phone_with_camera = SmartphoneWithCamera("Samsung", "Galaxy S21", 70, 108)
phone_with_camera.take_photo()
phone_with_camera.make_call("555-123-4567")
