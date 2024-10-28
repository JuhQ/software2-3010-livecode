class Storage:
    def __init__(self):
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def list_files_in_storage(self):
        for file in self.files:
            print(file)

class Camera:
    def take_photo(self):
        print("click, photo taken")
        self.photo = "my_photo.jpg"

class GPS:
    lat = 61.2765
    lon = 20.2389

class Call:
    def dial(self, to_number):
        for number in to_number:
            print(f"Dialing number: {number}")
    def make_call(self, to_number):
        self.dial(to_number)
        print(f"Call is active to number {to_number}")

class Phone(Call, Storage, GPS, Camera):
    def __init__(self, brand, model, price):
        Storage.__init__(self)
        self.brand = brand
        self.price = price
        self.model = model

    def print_details(self):
        print(f"{self.brand}, {self.model}, {self.price}")

class Nokia8110Phone(Phone):
    def __init__(self, price):
        super().__init__("Nokia", 8110, price)


class Laptop(Storage, Camera):
    def __init__(self):
        Storage.__init__(self)
        Camera.__init__(self)
        print("Laptop")


laptop = Laptop()
laptop.add_file("excel.xlx")
laptop.take_photo()
laptop.photo

phone = Phone("Nokia", 8110, 200)
phone2 = Phone("Nokia", 8110, 200)
phone3 = Phone("Apple", "iPhone 16", 1700)
phone4 = Phone("Samsung", "Galaxy", 200)

phone.print_details()

phone.add_file("image.jpg")

phone.list_files_in_storage()

phone.take_photo()
print(phone.photo)
phone.add_file(phone.photo)

print("---------")

phone.list_files_in_storage()

print(phone.lat)
print(phone.lon)

phone.make_call("040-12341234")

nokia = Nokia8110Phone(50)
nokia.take_photo()
nokia.print_details()