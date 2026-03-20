from datetime import datetime
from dataclasses import dataclass


class Event:
    """Represents an raw market instruction."""
    timestamp: datetime
    order_id: str
    side: str 
    price: float | None 
    quantity: float

    def __init__(self, timestamp: datetime, order_id: str, side: str, price: float | None, quantity: float):
        self.timestamp = timestamp
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity


        def validate(self) -> None:
            """Validates the order data.
            Raises:
                ValueError: If any of the order attributes are invalid.
            """
            raise NotImplementedError
        
        def __repr__(self) -> str:
            """Returns a string representation of an Event instance."""


        def to_dict(self) -> dict:
            """Converts raw data to JSON format."""


class Order:
    """An order in that sits in a PriceLevel queue."""
    order_id: str
    side: str
    price: float 
    quanity: float
    remaining_qty: float 
    status: str 


    def __init__(self, order_id: str, side: str, price: float, quantity: float):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.remaining_qty = quantity
        self.status = "open"

    def __repr__(self) -> str:
        """Returns a string representation of an Order instance."""
        pass 

    
    def to_dict(self) -> dict:
        """Converts order data to JSON format for log.json entry."""
        pass


    def fill(qty: float) -> float:
        """Fills the order by reducing the remaining quantity and updating the status."""
        pass

    def cancel() -> None:
        """Cancels the order by setting the status to 'cancelled'."""
        pass            

    def is_complete() -> bool:
        """Checks if the order is complete by comparing the remaining quantity to zero or status == 'cancelled'."""
        pass

    