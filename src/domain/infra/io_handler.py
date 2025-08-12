import json
import sys
from domain.entities import Operation
from ..use_cases.tax_calculator import TaxCalculator

def process_input_line(line: str, calculator: TaxCalculator) -> str:
    # Strip whitespace and newlines to ensure clean JSON
    line = json.dumps(json.loads(line))
    line = line.strip()
    if not line:
        return ""
    # Debug: Print the exact input for inspection
    # print(f"DEBUG: Raw input (len={len(line)}): {repr(line)}", file=sys.stderr)
    try:
        ops_data = json.loads(line)
        if not isinstance(ops_data, list):
            print(f"Error: Input JSON is not a list: {ops_data}", file=sys.stderr)
            return ""
        operations = [Operation(o["operation"], o["unit-cost"], o["quantity"]) for o in ops_data]
        result = calculator.calculate_taxes(operations)
        return json.dumps(result, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e} at position {e.pos} in input: {repr(line)}", file=sys.stderr)
        return ""
    except KeyError as e:
        print(f"Error: Missing key in operation data: {e}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return ""