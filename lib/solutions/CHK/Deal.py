import re
from price_table_and_offers import price_table

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
    
    def calculate_saving(self):
        return self.n*price_table[self.item] - self.price


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
    
    def calculate_saving(self):
        return price_table["itemy"]


# Generate a Deal object from the offer wording
def get_deal(offer):
    if match := re.fullmatch(DealNForY.regex, offer):
        return DealNForY(match['n'],match['item'],match['price'])
    elif match:= re.fullmatch(DealBuyXGetY.regex, offer):
        return DealBuyXGetY(match['n'], match['itemx'], match['itemy'])


# Comparison operation to sort deals
def compare_deals(deal1, deal2):
    if type(deal1) == DealNForY and type(deal1) == type(deal2):
        return 0
    if type(deal1) == DealNForY and type(deal2) == DealBuyXGetY:
        costofitem1 = deal1.price/deal1.n
        cost