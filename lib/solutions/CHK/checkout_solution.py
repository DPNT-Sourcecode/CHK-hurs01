import re

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

deals = []

# Generate a Deal object from the offer wording
def get_deal(offer):
    if match := re.fullmatch(DealNForY.regex, offer):
        return DealNForY(match['n'],match['item'],match['price'])
    elif match:= re.fullmatch(DealBuyXGetY.regex, offer):
        return DealBuyXGetY(match['n'], match['itemx'], match['itemy'])

    
# Represents a 'buy n of item x for the price of y' deal
class DealNForY:

    regex = r'(?P<n>\d+)(?P<item>\w) for (?P<price>\d+)'

    def __init__(self, n, item, price):
        self.n = n
        self.item = item
        self.price = price
    
    def __repr__(self):
        return f"{self.n}{self.item} for {self.price}"
    
    def can_apply_deal(self, basket):
        if basket.get(self.item,0)>=self.n:
            return True
        else:
            return False
        
    def apply_deal(self, basket):
        basket[self.item] = basket[self.item]-self.n
        return self.price


# Represents a 'buy n of item x to get item y free' deal
class DealBuyXGetY:
    
    regex = r'(?P<n>\d+)(?P<itemx>\w) get one (?P<itemy>\w) free'

    def __init__(self, n, itemx, itemy):
        self.n = n
        self.itemx = itemx
        self.itemy = itemy
    
    def __repr__(self):
        return f"{self.n}{self.itemx} get one {self.itemy} free"
    
    def can_apply_deal(self, basket):
        if (self.itemx == self.itemy and basket.get(self.itemx,0)>=self.n+1) \
        or (self.itemx != self.itemy and basket.get(self.itemx,0)>=self.n and basket.get(self.itemy,0)>0):
            return True
        else:
            return False
    
    def apply_deal(self, basket):
        basket[self.itemx]-=self.n
        basket[self.itemy]-=1
        return price_table[self.itemx]*self.n



# List of deals that can be applied. Deals should be listed in order in which they should be applied.
deals = [
    DealBuyXGetY(2, "E", "B"),
    DealNForY(2, "B", 45),
    DealNForY(5, "A", 200),
    DealNForY(3, "A", 130),
    DealBuyXGetY(2,"F","F")
]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Count items in basket - to be optimised for larger price tables (i.e. more items) using Counter
    basket = {s:skus.count(s) for s in skus}
    total = 0

    # Iteratively apply deals until no more apply
    for deal in deals:
        while deal.can_apply_deal(basket):
            total += deal.apply_deal(basket)

    try:
        for item, count in basket.items():
            total += count * price_table[item]
            basket[item] = 0
    except KeyError:
        return -1
    
    return total



