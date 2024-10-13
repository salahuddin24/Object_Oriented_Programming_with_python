
#masic method gola shadaronoto (__) double underscore diya shoro o sesh hoy
# some example :
# 1. __init__()
# ** mesic mathods for comparison
# 1. __eq__(self, other) ( eq for =)
# 2. __nq__(self, other) ( ne for !=)
# 3. __lt__(self, other) ( lt for <)
# 4. __gt__(self, other) ( gt for >)
# 5. __le__(self, other) ( le for <=)
# 6. __ge__(self, other) ( ge for >=)


class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return (f"Name = {self.name} , Color = {self.color}")
    # def display(self):
        # print(f"Name = {self.name} , Color = {self.color}")

bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha R15", "Blue")
# print(bike1.display())

print(bike1)

print(bike1 == bike2)

















