

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

    # Iteratively apply deals until basket is empty

    total = 0
    try:
        for (sku,count) in basket_count.items():
            item = price_table[sku]
            if item.get("offer"):
                # Quotient is the number of times offer is applied; remainder is number of individually priced products
                (n,y) = item.get("offer")
                quot,rem = divmod(count,n)
                total = total + quot*y + rem*item["price"]
            else:
                total = total + count*item["price"]

    except KeyError:
        return -1
    
    return total

