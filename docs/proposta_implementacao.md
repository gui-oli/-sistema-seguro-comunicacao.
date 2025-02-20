- Detalhamento referente as tecnologias aplicadas na implementação do sistema:

- Principais etapas de implementação, incluindo:

1. Cadastro de usuário → Hash de senha com bcrypt.
2. Login → Geração e verificação de Token JWT.
3. Criptografia de mensagens → Uso de AES (CBC).
4. Proteção da chave AES → Uso de RSA para criptografar a chave antes de armazená-la.
