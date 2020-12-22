# Importar pacotes necessários
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd

# Inicializar o WhatsApp
wp = WhatsApp()

#Esperar o Enter ser pressionado
input("Pressione enter apos escanear o QR code")

# Lista de nomes ou numeoros de telefone a serem pesquisados
# IMPORTANTE: O nome ou numero devem ser únicos!!!!
df = pd.read_excel('C:/Users/vsert/Documents/Curso Awari Data Science/Bot WhatsApp/whatsapp_api-master/numlist.xlsx')

#Lista de contatos da planilha
nomes_palavras_chaves = list(df['Contato'])

#Lista de mensagens da planilha
lista_mensagens = list(df['Mensagem'])

# Loop para enviar mensagens para os clientes
for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, lista_mensagens):
    
    # Pesquisar pelo contato e espear 2 segundos
    wp.search_contact(nome_pesquisar)
    sleep(2)
         
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar o navegador
sleep(10)
wp.driver.close()