# Data Project Structure

## Sobre

Esse repositório é para estudos de boas práticas de engenharia de dados, incluindo automação, testes e documentação.

### Objetivos

- Estruturação de projetos de dados.
- Uso de ferramentas de desenvolvimento, testes e versionamento.
- Documentação com MKDocs e automação com CI/CD.

## Início Rápido

### Pré-requisitos
- **Pyenv**: [Instalação do Pyenv](https://github.com/pyenv/pyenv#installation) (Python 3.11.3 recomendado)
- **Poetry**: [Instalação do Poetry](https://python-poetry.org/docs/#installation)

### Configuração

1. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

2. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
poetry env use 3.11.5
poetry shell
```

3. Instale as dependencias do projeto:

```bash
poetry install
```

4. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
task test
```

5. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

6. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```
