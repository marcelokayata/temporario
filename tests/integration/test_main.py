import json
import pytest
from io import StringIO
from src.main import main
from src.infra.io_handler import process_input_line
from src.domain.use_cases.tax_calculator import TaxCalculator

@pytest.fixture
def mock_stdin(monkeypatch):
    def _mock_stdin(input_data):
        monkeypatch.setattr('sys.stdin', StringIO(input_data))
    return _mock_stdin

def test_process_multiple_lines(capsys, mock_stdin):
    input_data = (
        '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]\n'
        '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000},{"operation":"sell", "unit-cost":5.00, "quantity": 5000}]\n'
        '\n'
    )
    mock_stdin(input_data)
    main()
    captured = capsys.readouterr()
    # Filter out non-JSON lines (e.g., "rodou")
    outputs = [line for line in captured.out.strip().split('\n') if line.startswith('[')]
    expected = [
        '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}]',
        '[{"tax": 0.0}, {"tax": 10000.0}, {"tax": 0.0}]'
    ]
    assert outputs == expected

def test_empty_line_stops():
    calculator = TaxCalculator()
    assert process_input_line('', calculator) == ''