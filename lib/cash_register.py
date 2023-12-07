#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        for x in range(quantity):
            self.items.append({"title": title, "price": price})
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.items[-1]["price"]
            self.total -= last_item_price * len([item for item in self.items if item["price"] == last_item_price])
            self.items = [item for item in self.items if item["price"] != last_item_price]
            if not self.items:
                self.total = 0





