# testepraticoPython


Tentei ser mais direto aqui pois perdi bastante tempo no Laravel. 
Aqui eu basicamente fiz uma automação para testar vários logins e retornar um csv com quais funcionanram e quais não 


## Funcionamento
1. O script carrega uma lista de emails e senhas a partir de um arquivo CSV.
2. Para cada credencial, o script tenta realizar o login na aplicação.
3. Se o login for bem-sucedido, o script realiza o logout e tenta a próxima credencial.
4. Caso o login falhe, ele passa para a próxima tentativa.
5. O resultado de cada tentativa (sucesso ou falha) é registrado em um novo arquivo CSV.

## Como executar o projeto
1. Instale as dependências necessárias:
   pip install selenium pandas
2. ChromeDriver compativel com a verão do seu browser instalado na mesma pasta do python
4. Execute o script
   python main.py
