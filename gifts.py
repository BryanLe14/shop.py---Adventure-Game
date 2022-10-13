import random

player_inv = []
possible_gifts = ["gift1", "gift2", "gift3"]
shop_gift = random.choice(possible_gifts)

give_gift = input("Would you like to give a gift? Y/N? ")
def interest1_gift():
  interest1 = 0
  if shop_gift == "gift1":
    interest1 = interest1 + random.randint(10, 25)
  elif shop_gift == "gift2":
    interest1 = interest1 + random.randint(5, 15)
  elif shop_gift == "gift3":
    interest1 = interest1 + random.randint(1, 10)
  print(interes1)
gifts = []
gift_count = 1
for i in player_inv:
    if i in possible_gifts:
        gifts.append(i)
        print(f"{gift_count}) {i}")

if give_gift == "Y":
  chosen_interest = int(input("Who would you like to give your gift to? (1, 2, 3)? "))
  if chosen_interest == 1:
    interest1_gift()




interest2 = 0
interest3 = 0


  


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    # method to add/subtract quantity of item
    def change(self, quantity):
        self.quantity = self.quantity + quantity



class Gift(Item):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)
    def use(self):
        # 
        player_inv.pop(player_inv.index(self))

