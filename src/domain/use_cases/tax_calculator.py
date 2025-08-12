from ..entities import Operation
from typing import List, Dict


class TaxCalculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.total_shares = 0
        self.weighted_avg = 0.0
        self.accumulated_loss = 0.0

    def calculate_taxes(self, operations: List[Operation]) -> List[Dict]:
        self.reset()
        taxes = []
        for op in operations:
            tax = self._process_operation(op)
            taxes.append({"tax": tax})
        return taxes

    def _process_operation(self, op: Operation) -> float:
        if op.operation == "buy":
            if self.total_shares == 0:
                self.weighted_avg = op.unit_cost
            else:
                self.weighted_avg = (
                    (self.total_shares * self.weighted_avg) + (op.quantity * op.unit_cost)
                ) / (self.total_shares + op.quantity)
            self.total_shares += op.quantity
            return 0.0
        elif op.operation == "sell":
            total_value = op.unit_cost * op.quantity
            cost = self.weighted_avg * op.quantity
            profit = total_value - cost

            if profit <= 0:
                tax = 0.0
                self.accumulated_loss += -profit
            else:
                if total_value > 20000:
                    effective_profit = profit - self.accumulated_loss
                    if effective_profit > 0:
                        tax = round(effective_profit * 0.2, 2)
                        self.accumulated_loss = 0.0
                    else:
                        tax = 0.0
                        self.accumulated_loss = -effective_profit
                else:
                    tax = 0.0
                    # Do not deduct from accumulated_loss for operations <= 20000
            self.total_shares -= op.quantity
            return tax
        raise ValueError(f"Unknown operation: {op.operation}")