import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.domain.use_cases.tax_calculator import TaxCalculator
from src.infra.io_handler import process_input_line

def main():
    calculator = TaxCalculator()
    for line in sys.stdin:
        output = process_input_line(line, calculator)
        if output:
            print(output)

if __name__ == "__main__":
    main()