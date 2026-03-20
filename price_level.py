"""
Price Level data structure
"""
from queue import Queue


class PriceLevel:
    """
    Price Level data structure, contains price + FIFO Queue to assign the best price to the best buyers +
    volume of buyers at this level.
    """

    price: float
    orders: Queue
    volume: float

    def __init__(self, price: float, orders: Queue, volume: float):
        self.price = price
        self.orders = orders
        self.volume = volume
