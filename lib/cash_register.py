#!/usr/bin/env python3
import ipdb;

class CashRegister:
  def __init__(self,discount=0,total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0

  def add_item(self,title='',price=0,quantity=1):
    i = 0
    self.last_transaction = price*quantity
    while i < quantity:
      self.items.append(title)
      self.total += (price)
      i+=1

  def apply_discount(self):
    self.total -= self.discount*10
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      print(f'After the discount, the total comes to ${self.total}.')

  def void_last_transaction(self):
    self.total -= self.last_transaction