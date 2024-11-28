

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # "offer": (n,y) means buy n of item and it costs y pounds
    price_table = {
        "A": {
            "price": 50,
            "offer": (3,130)
        },
        "B": {
            "price": 30,
            "offer": (2,45)
        },
        "C": {
            "price":20
        },
        "D": {
            "price":15
        }
    }

    # Count items in basket - to be optimised for larger price tables (i.e. more items)
    basket_count = {s:skus.count(s) for s in skus}

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


checkout("AAABBBBBCCCCD")
