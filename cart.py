class ShoppingCart(object):
  def __init__(self):
    self.total = 0
    self.items = dict()
    
  def add_item(self, item_name, quantity, price):
    self.total = self.total + (price*quantity)
    self.items[item_name] = quantity
   
  def remove_item(self, item_name, quantity, price):
    quantityLeft = self.items[item_name]
    if quantityLeft > quantity:
      self.items[item_name] = self.items[item_name] - quantity
      self.total = self.total - (price*quantity)
     
    else:
      self.total = self.total - (price*quantityLeft)
      self.items.pop(item_name)
  
  def checkout(self,cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    
    else:
      return cash_paid - self.total

class Shop(ShoppingCart):
  
  def __init__(self):
    ShoppingCart.__init__(self)
    self.quantity = 100
    
  def remove_item(self):
    self.quantity = self.quantity - 1
    
if __name__ == "__main__":
  cart = ShoppingCart()
  cart.add_item("Mango", 3, 10)
  cart.add_item("Orange", 16,10)
  
  print ("All Items in Cart: ", cart.items)
  print ("Current Total: ", cart.total)
  
  cart.remove_item("Mango", 3,10)
  cart.remove_item("Orange",2,10)
  
  print()
  print("After removing Mango and Oranges: ", cart.items)
  print("Total balance after removing: ", cart.total)
  
  print()
  print("after payment of 200")
  print(cart.checkout(200))
  
  print
  shop = shop()
  shop.remove_item()
  print ("Total Quantity in shop: ",shop.quantity)
  