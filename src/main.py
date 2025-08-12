import sys
# from domain.use_cases.tax_calculator import TaxCalculator
# from domain.infra.io_handler import process_input_line

from src.domain.use_cases.tax_calculator import TaxCalculator
from src.infra.io_handler import process_input_line

def main():
    calculator = TaxCalculator()
    print("rodou")
    for line in sys.stdin:
        output = process_input_line(line, calculator)
        if output:
            print(output)

if __name__ == "__main__":
    main()