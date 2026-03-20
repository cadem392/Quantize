"""
Price Level data structure
"""
from collections import deque
from queue import Queue
from __future__ import annotations

from orders import Order


class PriceLevel:
    """
    Price Level data structure, contains price + FIFO Queue to assign the best price to the best buyers +
    volume of buyers at this level.

    Each Price Level instance represents a single node in the book_tree, storing volume, price, and the
    buyer Queue.
    """

    price: float
    orders: Queue
    volume: float
    left: PriceLevel | None
    right: PriceLevel | None

    def __init__(self, price: float, orders: Queue = Queue, volume: float = 0.0):
        self.price = price
        self.orders = orders
        self.volume = volume

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} price={self.price} orders={self.orders}>"

    def is_empty(self) -> bool:
        """
        Returns True if this instance is empty, False otherwise. self.volume should also be 0 if empty.
        """

        return self.orders is None

    def update_volume(self, delta: float) -> None:
        """
        Mutates the volume of this instance by delta; keeps volume consistent across queue mutations.
        """

        self.volume += delta

    def add_order(self, order: Order) -> None:
        """
        Mutates the queue to add the specified order to the queue.
        """

        self.orders.put(order)
        self.update_volume(delta=order.quantity)

    def pop_order(self):
        """
        Mutates the queue to remove the first order and return it.
        """

        return self.orders.get()
