#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount  = discount
    self.total     = 0
    self.items   = []
    

  def  add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([(title, price)] * quantity)

  def apply_discount(self):
    if self.discount > 0:
      self.total  *= (1 - self.discount / 100)
      print(f"After the discount, the total comes to $800.\n")

    else:
      print("There is no discount applied.")

  def void_last_transaction(self):
     if self.items:
      last_title, last_price = self.items.pop()
      self.total -= last_price
      if not self.items:
        self.total = 0
      else:
            print("No transaction to void.")