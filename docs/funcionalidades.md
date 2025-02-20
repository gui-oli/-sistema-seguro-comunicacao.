- Descrição das funcionalidades da aplicação: 

1. Cadastro de usuário → Protege a senha com bcrypt antes de armazenar.
- o sistema ira cadastrar um novo usuario com nome e senha, com a senha sendo criptografada para a segurança do cliente e tudo será salvo e retornado ao destinatario

2. Login → Se a senha estiver correta, gera um Token JWT.
- o usuario ira acessar seu login utilizando sua senha, o siatema ira comparar a senha inserida com o hash armazenado, Se a senha for correta, gere um Token JWT de acesso ao sistema. 

3. Enviar mensagem → A mensagem é criptografada com AES e será retornada para o usuário. 

4. Receber mensagem → O usuário descriptografa com RSA sua chave AES e acessa a mensagem enviada na etapa anterior. 


