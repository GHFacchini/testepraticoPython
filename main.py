import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd




df = pd.read_csv('input.csv')
output_data = []
navegador = webdriver.Chrome()


for index, row in df.iterrows():
    email = row['email']
    senha = row['senha']
    result = False

    try:
        navegador.get('http://localhost/testepratico/public/login')

        email_input = navegador.find_element(By.NAME, 'email')
        password_input = navegador.find_element(By.NAME, 'password')


        email_input.send_keys(email)
        password_input.send_keys(senha)
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # logout
        navegador.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[3]/a').click()
        result = True

    except Exception as e:
        print(f'Não foi possível logar email: {email} e senha: {senha}: {e}')

    output_data.append([email, senha, result])


time.sleep(3)
navegador.quit()


output_df = pd.DataFrame(output_data, columns=['Email', 'Senha', 'Resultado'])
output_df.to_csv('output.csv', index=False)