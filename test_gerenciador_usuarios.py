from gerenciador_usuarios import GerenciadorUsuarios, StubRepositorio


def test_criar_usuario_chama_salvar():
    repo = StubRepositorio()
    manager = GerenciadorUsuarios(repo)

    usuario = manager.criar_usuario(
        "1",
        "Ana",
        "ana@email.com"
    )

    assert repo.salvos[0] == usuario


def test_buscar_usuario():
    repo = StubRepositorio()
    manager = GerenciadorUsuarios(repo)

    manager.criar_usuario(
        "1",
        "Ana",
        "ana@email.com"
    )

    usuario = repo.buscar("1")

    assert usuario["nome"] == "Ana"
    assert usuario["email"] == "ana@email.com"


def test_identificador_vazio():
    repo = StubRepositorio()
    manager = GerenciadorUsuarios(repo)

    try:
        manager.criar_usuario("", "Ana", "ana@email.com")
        assert False
    except ValueError:
        assert True


def test_nome_vazio():
    repo = StubRepositorio()
    manager = GerenciadorUsuarios(repo)

    try:
        manager.criar_usuario("1", "", "ana@email.com")
        assert False
    except ValueError:
        assert True


def test_email_vazio():
    repo = StubRepositorio()
    manager = GerenciadorUsuarios(repo)

    try:
        manager.criar_usuario("1", "Ana", "")
        assert False
    except ValueError:
        assert True