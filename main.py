APP_NAME = "OmniHack"
APP_VERSION = "0.2.1"


def build_status_message(environment="teste"):
    return f"{APP_NAME} iniciado. Versao {APP_VERSION}. Ambiente: {environment}."


def build_pull_request_marker():
    return "PR de teste criado alterando apenas main.py."


def main():
    print(build_status_message())
    print(build_pull_request_marker())


if __name__ == "__main__":
    main()
