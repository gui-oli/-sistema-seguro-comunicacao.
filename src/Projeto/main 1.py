from user import User
from messaging import Message


def cadastrar_usuario():
    """Função para cadastrar um novo usuário."""
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    # Cria um novo usuário
    usuario = User(username, password)
    print(f"Usuário '{username}' cadastrado com sucesso!")
    return usuario

def login_usuario(usuario):
    """Função para realizar o login do usuário."""
    login_username = input("Digite seu nome de usuário para login: ")
    login_password = input("Digite sua senha: ")

    if login_username == usuario.username and usuario.check_password(login_password):
        token = usuario.generate_token(login_username)
        print(f"Login bem-sucedido! Seu token: {token}")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

def enviar_mensagem(usuario):
    """Função para enviar uma mensagem criptografada."""
    message_system = Message()
    private_key, public_key = message_system.generate_keys()

    recipient_username = input("Digite o nome de usuário do destinatário: ")
    message_text = input("Digite a mensagem a ser enviada: ")

    encrypted_aes_key, encrypted_message = message_system.encrypt_message(message_text, public_key)
    print("Mensagem criptografada e enviada com sucesso!")

    # Descriptografando a mensagem (apenas para demonstração)
    decrypted_message = message_system.decrypt_message(encrypted_aes_key, encrypted_message)
    print(f"Mensagem recebida (descriptografada): {decrypted_message}")


def main():
    """Função principal do programa."""
    usuario = cadastrar_usuario()

    if login_usuario(usuario):
        enviar_mensagem(usuario)


if __name__ == "__main__":
    main()