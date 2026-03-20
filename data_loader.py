from orders import Event
import numpy as np

class DataLoader:
    """Loads and generates Event streams."""

    filepath: str | None 
    events: list[Event] 
    schema: dict 

    def __init__(self, filepath: str | None = None) -> None:
        """Initializes the DataLoader with an optional file path."""
        pass

    def load_csv(self, row: dict) -> Event:
        """Reads training data from a CSV file."""
        pass

    def _row_to_event(self, row: dict) -> Event:
        """Converts a CSV row to an Event instance."""
        pass

    def generate_synthetic(scenario: str, n: int = 1000) -> list[Event]:
        """Generates synthetic Event data based on a specified scenario."""
        pass

    def _balanced_flow(n: int) -> list[Event]:
        """Generates a balanced flow of buy and sell events."""
        pass

    def _low_liquidity(n: int) -> list[Event]:
        """Generates a scenario with low liquidity."""
        pass

    def _high_volatility(n: int) -> list[Event]:
        """Generates a scenario with high price volatility."""
        pass

    def validate(self) -> list[str]:
        """Validates the loaded data."""
        pass

    def to_feature_matrix(self) -> np.ndarray:
        """Converts the Event data into a feature matrix for model training."""
        pass
