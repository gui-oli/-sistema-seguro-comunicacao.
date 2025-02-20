Tecnologias utilizadas:

 bcrypt → Hashing seguro de senhas versão - 25.02
 PyJWT → Autenticação via Tokens JWT - versão - 25.02
 cryptography → Implementação de AES e RSA 25.02

 Fluxo básico do sistema:
 
 Usuário faz cadastro (senha armazenada com bcrypt).
 O sistema deve permitir que usuários se cadastrem informando um nome de usuário e uma senha.
 A senha deve ser armazenada de forma segura utilizando hashing com bcrypt.

 Usuário faz login (autenticado via JWT).
O sistema deve permitir que usuários façam login informando usuário e senha
O login deve validar a senha comparando-a com o hash armazenado
Um Token JWT deve ser gerado após um login bem-sucedido.
 
 Usuário envia uma mensagem criptografada com AES.
As mensagens devem ser criptografadas com AES antes de serem armazenadas.
A criptografia deve utilizar o modo CBC (Cipher Block Chaining) e um IV aleatório para cada mensagem
O usuário autenticado pode solicitar a descriptografia da mensagem
Apenas o destinatário correto pode descriptografar com sua chave RSA.
