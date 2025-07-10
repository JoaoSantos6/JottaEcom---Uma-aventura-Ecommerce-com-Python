# JottaEcom - Uma aventura Ecommerce com Python

## Objetivo

Este projeto tem como objetivo fornecer uma base para um sistema de e-commerce, incluindo backend com FastAPI, integração com banco de dados via SQLAlchemy e testes automatizados.

## Dependências

- Python >= 3.13,<4.0
- [Poetry](https://python-poetry.org/)
- SQLAlchemy >=2.0.41,<3.0.0
- FastAPI[standard] >=0.116.0,<0.117.0
- pytest
- pytest-cov
- taskipy
- ruff


## Testes
Abaixo, exemplos de relatórios de cobertura de testes:

### Caso de sucesso (100% das funções cobertas)

![Cobertura 100%](../Doc/img/coverage_na_web_sucesso.PNG)

### Caso com parte da função não testada

![Cobertura parcial](../Doc/img/coverage_parte_nao_testada.PNG)