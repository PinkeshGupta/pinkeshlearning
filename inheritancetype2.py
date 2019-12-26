
# # types of inheritance 




# # Single Inheritance 
# class Parent:
#     pass
# class Child(Parent):
#     pass


# #Multilevel Inheritane

# class Parent:
#     pass
# class Child(Parent):
#     pass
# class NewChild(Child):
#     pass

# # Multiple inheritance

# class Parent:
#     pass
# class Child:
#     pass
# class NewChild(Child,Parent):
#     pass


# # Hierarical Inheritance
# class Parent:
#     pass
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass


# # Hybrid Inheritance


class ElectronicGadget:
         brand ="MI"
         rating =5
         
            
class PocketGadget(ElectronicGadget):
    YOM =2019
    def headfphone(self):
        
        return f"Headphone brand is {super().brand} and rating is {super().rating} and YOM is {self.YOM}"
        
class Phone(PocketGadget):
    price=9999
    def phonetype(self):
        
        return f"Mobile Brand is {super().brand} and price is {self.price} and YOM{super().YOM}"

mobile =Phone()
print(mobile.phonetype())

earphone =PocketGadget()
print(earphone.headfphone())























