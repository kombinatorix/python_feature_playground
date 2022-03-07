from functools import total_ordering


@total_ordering  # only worth it, if one can live with the price of slower execution time
class Price(object):
    def __init__(self, price) -> None:
        self.price = price

    def __eq__(self, __o: object) -> bool:
        return self.price == __o.price

    def __lt__(self, __o: object) -> bool:
        return self.price < __o.price


if __name__ == "__main__":
    p1 = Price(1.99)
    p2 = Price(3.49)
    print(p1 <= p2)
    print(p1 > p2)
    print(p1 >= p2)
