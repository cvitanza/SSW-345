# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory: int  # New attribute for inventory

    def __init__(self, sale: Sale, inventory: int):
        self.__lastSale = sale
        self.__inventory = inventory  # Initialize inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    @property
    def inventory(self) -> int:
        return self.__inventory

    def sell(self, quantity: int):
        if quantity <= self.__inventory:
            self.__inventory -= quantity  # Decrease inventory
        else:
            raise ValueError("Insufficient inventory.")

    def __getitem__(self, item):
        return self

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __saleNumber: int = 0

    def __init__(self, products: List[Product]):
        Sale.__saleTimes += 1
        self.__products = products
        self.__saleNumber = Sale.__saleTimes
        for product in products:
            product.setLastSale(self)
            product.sell(1)  # Assuming 1 of each product is sold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber

# Example usage
productOne = Product(sale=None, inventory=10)
productTwo = Product(sale=None, inventory=5)

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"Product One Last Sale: {productOne.getLastSale.getSaleNumber}, Remaining Inventory: {productOne.inventory}")
print(f"Product Two Last Sale: {productTwo.getLastSale.getSaleNumber}, Remaining Inventory: {productTwo.inventory}")
