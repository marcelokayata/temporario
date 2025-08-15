Um aviso importante (para ser transparente)
Neste teste eu utilizei IA do Grok, tive que adiar a entrega do teste duas vezes, pois estou no meio de uma entrega grande onde trabalho.

Eu tive que guiar a IA, fazer ajustes no código, mas acabou dando certo, podendo rodar os testes e a cobertura utilizando somente o docker, como costumo fazer onde trabalho.

Rodar com docker
remover orphans:
docker-compose down --remove-orphans

Remover warning:
image.png

Configurar aplicação:
docker-compose build

ROdar aplicação:
docker-compose run app

Rodar teste:
docker-compose run test

Rodar cobertura:
docker-compose run coverage

Isso só são intruções usadas quando não tinha docker
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
Ruuning the application without docker:
 python src/main.py < input.txt

Caminho do pythonPath
Run test: PYTHONPATH=/root/teste_nubank venv/bin/pytest tests/


