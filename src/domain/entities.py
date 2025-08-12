from dataclasses import dataclass

@dataclass
class Operation:
    operation: str
    unit_cost: float
    quantity: int