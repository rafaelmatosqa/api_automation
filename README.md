# API Automation

## Estrutura do Projeto

Este projeto contém testes automatizados para APIs utilizando pytest, seguindo práticas de SOLID, Clean Code e orientação a objetos.

## Configuração de Ambientes

Os arquivos de configuração para diferentes ambientes estão localizados na pasta `config`. 

## Execução dos Testes

Para executar os testes, defina o ambiente utilizando a variável de ambiente `ENV` (padrão é `dev`):

```sh
export ENV=uat
pytest
