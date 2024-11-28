

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

    basket = {}
    try:
        for s in list(skus):


