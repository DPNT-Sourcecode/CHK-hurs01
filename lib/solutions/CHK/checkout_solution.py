

price_table = {
    "A":50,
    "B":30,
    "C":20,
    "D":15,
    "E":40,
}

# Represents a 'buy n of item x for the price of y' deal
class DealNForY:
    def __init__(self, n, item, price):
        self.n = n
        self.item = item
        self.price = price
    
    def can_apply_deal(self, basket):
        if basket[self.item]>=self.n:
            return True
        else:
            return False
        
    def apply_deal(self, basket):
        basket[self.item] = basket[self.item]-self.n
        return self.price


# Represents a 'buy n of item x to get item y free' deal
class DealBuyXGetY:
    def __init__(self, n, itemx, itemy):
        self.n = n
        self.itemx = itemx
        self.itemy = itemy
    
    def can_apply_deal(self, basket):
        if basket[self.itemx]>=self.n and basket[self.itemy]>0:
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
    DealNForY(3, "A", 130)
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
            total += deal.apply(basket)

    try:
        for item, count in basket.items:
            total += count * price_table[item]
    except KeyError:
        return -1
    
    return total

checkout("AAAAAAAAAABBBBBBBCCCDDDEE")


