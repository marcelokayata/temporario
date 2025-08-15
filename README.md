-----

## Aviso Importante

Para ser transparente, utilizei a IA do Grok neste teste. Tive que adiar a entrega duas vezes devido a um projeto grande no meu trabalho atual. Embora a IA tenha auxiliado, eu a guiei e fiz ajustes no código, o que resultou em um produto final que permite rodar testes e verificar a cobertura usando apenas o Docker, como estou acostumado a fazer.

-----

## Como Rodar com Docker

Para começar, você pode seguir estas instruções:

  * **Remover containers antigos:**

    ```bash
    docker-compose down --remove-orphans
    ```

  * **Construir a imagem da aplicação:**

    ```bash
    docker-compose build
    ```

  * **Rodar a aplicação:**

    ```bash
    docker-compose run app
    ```

    (Se quiser usar valores diferentes, basta editá-los em **`input.txt`**.)

  * **Rodar os testes:**

    ```bash
    docker-compose run test
    ```

  * **Rodar a cobertura de testes:**

    ```bash
    docker-compose run coverage
    ```

-----

## Instruções sem Docker (Apenas para referência)

Caso não tenha o Docker disponível, estes passos também podem ser úteis:

  * **Criar e ativar o ambiente virtual:**

    ```bash
    python -m venv venv
    source ./venv/bin/activate
    ```

  * **Instalar as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

  * **Rodar a aplicação:**

    ```bash
    python src/main.py < input.txt
    ```

  * **Rodar os testes:**

    ```bash
    PYTHONPATH=/root/teste_nubank venv/bin/pytest tests/
    ```