class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = country

person1 = ContactInformation("René","Laplante","lapinet51@gmail.com","413-885-3534", "USA")
person2 = ContactInformation("Lud", "Poirier", "MarLuc38@cablevision.ca","514-843-5689", "Canada")

print(person2.country)