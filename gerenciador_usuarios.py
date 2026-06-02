"""Grupo 8 — Composição e injeção de dependência."""

from __future__ import annotations


class StubRepositorio:
    """Repositório simples em memória para testes."""

    def __init__(self) -> None:
        self.salvos: list[dict] = []

    def salvar(self, obj: dict) -> None:
        """Salva um objeto no repositório."""
        self.salvos.append(obj)

    def buscar(self, identificador: str) -> dict:
        """Busca um objeto pelo identificador."""
        for item in self.salvos:
            if item.get("id") == identificador:
                return item
        raise KeyError(f"Usuário '{identificador}' não encontrado")


class GerenciadorUsuarios:
    """Gerencia a criação e persistência de usuários."""

    def __init__(self, repositorio) -> None:
        self.repositorio = repositorio

    def criar_usuario(
        self,
        identificador: str,
        nome: str,
        email: str
    ) -> dict:
        """Cria um usuário e delega a persistência ao repositório.

        Args:
            identificador: ID único do usuário.
            nome: Nome do usuário.
            email: E-mail do usuário.

        Returns:
            dict: Usuário criado.

        Raises:
            ValueError: Se algum campo obrigatório estiver vazio.
        """
        if not identificador:
            raise ValueError("identificador não pode ser vazio")

        if not nome:
            raise ValueError("nome não pode ser vazio")

        if not email:
            raise ValueError("email não pode ser vazio")

        usuario = {
            "id": identificador,
            "nome": nome,
            "email": email,
        }

        self.repositorio.salvar(usuario)

        return usuario