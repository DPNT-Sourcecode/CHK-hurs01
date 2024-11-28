import re
from .Deal import *
from .price_table_and_offers import price_table, deals_raw

# Generate the list of deals as given in the offers
deals = [get_deal(d) for d in deals_raw]
# Sort deals in order of saving to decide order to apply them
deals = sorted(deals, key=lambda d: d.calculate_saving(), reverse=True)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Count items in basket - to be optimised for larger price tables (i.e. more items) using Counter
    basket = {s: skus.count(s) for s in skus}
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
