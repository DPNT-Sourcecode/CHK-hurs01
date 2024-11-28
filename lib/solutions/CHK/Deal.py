import re
from .price_table_and_offers import price_table


# Represents a 'buy n of item x for the price of y' deal
class DealNForY:

    regex = r"(?P<n>\d+)(?P<item>\w) for (?P<price>\d+)"

    def __init__(self, n, item, price):
        self.n = int(n)
        self.item = item
        self.price = int(price)

    def __repr__(self):
        return f"{self.n}{self.item} for {self.price}"

    def can_apply_deal(self, basket):
        if basket.get(self.item, 0) >= self.n:
            return True
        else:
            return False

    def apply_deal(self, basket):
        basket[self.item] = basket[self.item] - self.n
        return self.price

    def calculate_saving(self):
        return self.n * price_table[self.item] - self.price


# Represents a 'buy n of item x to get item y free' deal
class DealBuyXGetY:

    regex = r"(?P<n>\d+)(?P<itemx>\w) get one (?P<itemy>\w) free"

    def __init__(self, n, itemx, itemy):
        self.n = int(n)
        self.itemx = itemx
        self.itemy = itemy

    def __repr__(self):
        return f"{self.n}{self.itemx} get one {self.itemy} free"

    def can_apply_deal(self, basket):
        if (self.itemx == self.itemy and basket.get(self.itemx, 0) >= self.n + 1) or (
            self.itemx != self.itemy
            and basket.get(self.itemx, 0) >= self.n
            and basket.get(self.itemy, 0) > 0
        ):
            return True
        else:
            return False

    def apply_deal(self, basket):
        basket[self.itemx] -= self.n
        basket[self.itemy] -= 1
        return price_table[self.itemx] * self.n

    def calculate_saving(self):
        return price_table[self.itemy]


# Represents a 'buy any n of [items] for y' deal
class DealGroupDiscount:

    regex = r"buy any (?P<n>\d+) of \((?P<items>\w(?:,\w)*)\) for (?P<price>\d+)"

    def __init__(self, n, items, price):
        self.n = int(n)
        self.items = items
        self.price = int(price)

    def __repr__(self):
        return f"buy any {self.n} of {self.items} for {self.price}"

    def can_apply_deal(self, basket):
        if sum([basket[i] for i in self.items]) >= self.n:
            return True
        else:
            return False

    # Deal always tries to use the most expensive items
    def apply_deal(self, basket):
        order = sorted(self.items, key=lambda i: price_table[i], reverse=True)
        basket[self.itemy] -= 1
        return price_table[self.itemx] * self.n


# Generate a Deal object from the offer wording
def get_deal(offer):
    if match := re.fullmatch(DealNForY.regex, offer):
        return DealNForY(match["n"], match["item"], match["price"])
    elif match := re.fullmatch(DealBuyXGetY.regex, offer):
        return DealBuyXGetY(match["n"], match["itemx"], match["itemy"])
    elif match := re.fullmatch(DealGroupDiscount.regex, offer):
        return DealGroupDiscount(match["n"], match["items"].split(","), match["price"])



