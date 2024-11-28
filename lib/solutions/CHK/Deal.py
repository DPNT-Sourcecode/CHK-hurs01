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