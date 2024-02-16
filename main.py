PURCHASE_PRICE = 111
PAYMENT = 1000

NOTES = (5000, 2000, 1000, 500, 200, 100, 50)
COINS = (50, 20, 10, 5, 2, 1)


class InvalidPurchasePrice(Exception):
    """Purchase price is lower than zero!"""

    def __init__(self, purchase_price):
        message = f"Purchase price: '{purchase_price}' is lower than zero!"
        super().__init__(message)


class InvalidPayment(Exception):
    """Payment is lower than zero!"""

    def __init__(self, payment):
        message = f"Payment: '{payment}' is lower than zero!"
        super().__init__(message)


class PurchasePriceHigherThanPayment(Exception):
    """Purchase price is higher than payment!"""

    def __init__(self, purchase_price, payment):
        message = f"Purchase price: '{purchase_price}' is higher than payment: '{payment}'!"
        super().__init__(message)


def cashToChange(purchase_price: int | float, payment: int):
    change = []

    # input validation
    if purchase_price < 0:
        raise InvalidPurchasePrice(purchase_price)
    elif payment < 0:
        raise InvalidPayment(payment)
    elif purchase_price > payment:
        raise PurchasePriceHigherThanPayment(purchase_price, payment)

    # computation of amount of cash
    payment = int(round(payment))
    excess_money = payment - purchase_price

    # computation of list of tenders
    for tender in (NOTES + COINS):
        if excess_money == 0:
            break

        while True:
            if excess_money >= tender:
                change.append(tender)
                excess_money -= tender
            else:
                break

    return change


if __name__ == '__main__':
    try:
        change_money = cashToChange(PURCHASE_PRICE, PAYMENT)
        print(str(change_money))

    except Exception as exception:
        print(f"Exception: {exception}\r\nCheck input!")
