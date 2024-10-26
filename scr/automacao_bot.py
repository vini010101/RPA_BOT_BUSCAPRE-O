import pyautogui
import os
import time
import json
import keyboard
from PIL import ImageGrab  # Import necessário para captura de tela
import pytesseract  # OCR para verificar se o campo de usuário está preenchido

# Função para carregar a configuração a partir de um arquivo JSON
def carregar_configuracao(caminho_config):
    with open(caminho_config, 'r') as f:
        return json.load(f)

# Função para carregar as coordenadas a partir de um arquivo JSON
def carregar_coordenadas(caminho_coordenadas):
    with open(caminho_coordenadas, 'r') as f:
        return json.load(f)

# Função para verificar se o campo de usuário já está preenchido
def verificar_campo_usuario(coords):
    # Captura uma imagem da área do campo de usuário
    screenshot = ImageGrab.grab(bbox=(coords["usuario_sankhya"]["x"] - 50,
                                      coords["usuario_sankhya"]["y"] - 10,
                                      coords["usuario_sankhya"]["x"] + 50,
                                      coords["usuario_sankhya"]["y"] + 10))
    texto_campo = pytesseract.image_to_string(screenshot).strip()
    return texto_campo == ""  # Retorna True se o campo estiver vazio

# Função principal do BOT para automação de tarefas
def buscar_precos(config, coords):
    # Acessa os valores de configuração para caminhos
    erp_executable_path = config["erp_path"]
    server_executable_path = config["server_path"]

    # Passo 1: Abrir o Explorador de Arquivos
    os.startfile("explorer.exe")
    time.sleep(6)

    # Passo 2: Clicar em "Este Computador"
    pyautogui.click(coords["este_computador"]["x"], coords["este_computador"]["y"])
    time.sleep(6)

    # Passo 3: Duplo clique em "Disco Local (C:)"
    pyautogui.doubleClick(coords["disco_local_c"]["x"], coords["disco_local_c"]["y"])
    time.sleep(6)

    # Passo 4: Duplo clique na pasta "Navegador Sankhya"
    pyautogui.doubleClick(coords["pasta_navegador_sankhya"]["x"], coords["pasta_navegador_sankhya"]["y"])
    time.sleep(6)

    # Passo 5: Duplo clique no arquivo .exe do ERP
    pyautogui.doubleClick(coords["exe_sankhya"]["x"], coords["exe_sankhya"]["y"])
    time.sleep(20)

    # Passo 6: Login no ERP
    if verificar_campo_usuario(coords):
        pyautogui.click(coords["usuario_sankhya"]["x"], coords["usuario_sankhya"]["y"])
        pyautogui.write(config["usuario_sankhya"])
        pyautogui.press("enter")
        time.sleep(6)
    
    pyautogui.click(coords["senha_sankhya"]["x"], coords["senha_sankhya"]["y"])
    pyautogui.write(config["senha_sankhya"])
    pyautogui.press("enter")
    time.sleep(25)

    # Passo 7: Pesquisar a tela
    pyautogui.click(coords["pesquisar"]["x"], coords["pesquisar"]["y"])
    pyautogui.write(config["busca_preco"])
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(20)
    
    #passo 8 baixar o arquivo 
    pyautogui.click(coords["mostra_grade"]["x"], coords["mostra_grade"]["y"])
    pyautogui.sleep(3)
    pyautogui.click(coords["atualizar"]["x"], coords["atualizar"]["y"])
    pyautogui.sleep(3)
    pyautogui.doubleClick(coords["dh_processamento"]["x"], coords["dh_processamento"]["y"])
    pyautogui.sleep(3)
    pyautogui.click(coords["price_tab"]["x"], coords["price_tab"]["y"])
    pyautogui.sleep(3)
    pyautogui.click(coords["local_salvamento"]["x"], coords["local_salvamento"]["y"])
    pyautogui.sleep(3)
    pyautogui.click(coords["salvar"]["x"], coords["salvar"]["y"])
    pyautogui.sleep(2)

# Função para lidar com a caixa de diálogo de confirmação
def lidar_caixa_dialogo(coords):
    # Clica no botão "Sim" se a caixa de diálogo aparecer
    pyautogui.click(coords["sim"]["x"], coords["sim"]["y"])  # Coordenadas do botão "Sim"
    time.sleep(3)  # Espera tres segundo após clicar


# Definindo os caminhos dos arquivos de configuração
caminho_config = os.path.join(os.path.dirname(__file__), 'config.json')
caminho_coordenadas = os.path.join(os.path.dirname(__file__), 'coordenadas.json')



# Carregar configurações e coordenadas
config = carregar_configuracao(caminho_config)

# Verifique se o arquivo de coordenadas existe antes de carregá-lo
if os.path.exists(caminho_coordenadas):
    coords = carregar_coordenadas(caminho_coordenadas)
else:
    print("Arquivo de coordenadas não encontrado. Certifique-se de capturar as coordenadas primeiro.")

# Executar a busca de preços
try:
    buscar_precos(config, coords)
except KeyboardInterrupt:
    print("Programa interrompido com Ctrl+C.")