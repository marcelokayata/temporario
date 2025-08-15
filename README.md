criar ambiente virtual
```bash
python -m venv venv
```
Ativar o ambiente virtual
```bash
source ./venv/bin/activate
```
para instalar requirements.txt
```bash
pip install -r requirements.txt
```
Para criar requirements.txt
```bash
pip freeze > requirements.txt
```
Ruuning the application:
 python src/main.py < input.txt
Running test:
pytest tests/

Run test: PYTHONPATH=/root/teste_nubank venv/bin/pytest tests/

Example wich works: [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000}]


docker-compose up --build
docker-compose build
docker-compose up

Run application:
docker-compose up --build app

Run test:
docker-compose run test