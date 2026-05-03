from main import build_status_message


def test_build_status_message_for_n8n():
    assert build_status_message("n8n") == "OmniHack iniciado. Versao 0.2.0. Ambiente: n8n."
