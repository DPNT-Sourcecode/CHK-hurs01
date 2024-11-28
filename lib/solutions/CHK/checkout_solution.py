

price_table = {
    "A":50,
    "B":30,
    "C":20,
    "D":15,
    "E":40,
}

Deal1 = ""
Deal2 = ""
deals = [Deal1, Deal2]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Count items in basket - to be optimised for larger price tables (i.e. more items) using Counter
    basket = {s:skus.count(s) for s in skus}
    total = 0

    # Iteratively apply deals until no more apply
    for deal in deals:
        while deal.can_apply_deal(basket):
            total, basket = deal.apply(basket)
    
    try:
        for item, count in basket.items:
            total += count * price_table[item]
    except KeyError:
        return -1
    
    return total



