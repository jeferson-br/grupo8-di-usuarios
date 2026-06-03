# Grupo 8 — Composição e Injeção de Dependência

## Descrição

Este projeto demonstra os conceitos de **composição** e **injeção de dependência** em Python. O objetivo é desacoplar a lógica de gerenciamento de usuários da forma como os dados são armazenados, permitindo trocar a implementação do repositório sem modificar a classe principal.

## Conceitos Utilizados

### Composição

A composição ocorre quando uma classe utiliza outra classe para realizar parte de seu trabalho. Neste projeto, `GerenciadorUsuarios` utiliza um repositório para armazenar e buscar usuários.

### Injeção de Dependência

A injeção de dependência consiste em fornecer uma dependência externamente em vez de criá-la dentro da própria classe. O repositório é passado ao construtor de `GerenciadorUsuarios`, permitindo trocar sua implementação facilmente.

## Estrutura do Projeto

* `gerenciador_usuarios.py` — Contém as classes `StubRepositorio` e `GerenciadorUsuarios`.
* `test_gerenciador_usuarios.py` — Contém os testes automatizados do projeto.
* `README.md` — Documentação do projeto.

## API Pública

### Classe `StubRepositorio`

Repositório simples em memória utilizado para testes.

#### Métodos

##### `salvar(obj: dict) -> None`

Salva um objeto no repositório.

##### `buscar(identificador: str) -> dict`

Busca e retorna um objeto pelo identificador.

**Exceções:**

* `KeyError` caso o identificador não seja encontrado.

### Classe `GerenciadorUsuarios`

Responsável pela criação e gerenciamento de usuários.

#### Construtor

```python
GerenciadorUsuarios(repositorio)
```

Recebe uma implementação de repositório por injeção de dependência.

#### Métodos

##### `criar_usuario(identificador: str, nome: str, email: str) -> dict`

Cria um usuário, salva no repositório e retorna o usuário criado.

**Retorno:**

```python
{
    "id": "1",
    "nome": "Jeferson",
    "email": "Jeferson@email.com"
}
```

**Exceções:**

* `ValueError` caso algum campo obrigatório esteja vazio.

## Exemplo de Uso

```python
repo = StubRepositorio()
manager = GerenciadorUsuarios(repo)

usuario = manager.criar_usuario(
    "1",
    "Jeferson",
    "jeferson@email.com"
)

print(usuario)
```

## Executando os Testes

Instale o pytest:

```bash
pip install pytest
```

Execute os testes:

```bash
pytest
```

## Autor

Trabalho desenvolvido para a atividade do Grupo 8 — Composição e Injeção de Dependência.

