APP_NAME = "OmniHack"
APP_VERSION = "0.2.0"


def build_status_message(environment="teste"):
    return f"{APP_NAME} iniciado. Versao {APP_VERSION}. Ambiente: {environment}."


def main():
    print(build_status_message())


if __name__ == "__main__":
    main()
