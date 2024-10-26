import pyautogui
import time
import json

# Instruções para o usuário
print("Pressione Enter para capturar a posição do mouse.")
print("Após capturar a posição, pressione Enter novamente para capturar a próxima.")
print("Pressione Ctrl+C para interromper a captura a qualquer momento.")

# Dicionário para armazenar as coordenadas
coordenadas = {}

try:
    # Loop para capturar coordenadas
    for action in [
        "explorador_arquivos", "este_computador", "disco_local_c", 
        "pasta_navegador_sankhya", "exe_sankhya", "usuario_sankhya", 
        "senha_sankhya", "pesquisar", "busca_preco", "mostra_grade", 
        "atualizar", "dh_processamento", "price_tab", "local_salvamento", 
        "salvar", "sim", "nao"
    ]:
        input(f"Pressione Enter para capturar a posição de '{action}'.")
        
        # Captura a posição do mouse
        x, y = pyautogui.position()
        coordenadas[action] = {"x": x, "y": y}
        print(f"Coordenadas capturadas para '{action}': X={x}, Y={y}")

        # Espera 3 segundos antes da próxima captura
        time.sleep(3)

except KeyboardInterrupt:
    print("\nCaptura interrompida pelo usuário.")

# Atualizar o arquivo coordenadas.json
def atualizar_coordenadas(caminho_json):
    with open(caminho_json, 'w') as f:
        json.dump(coordenadas, f, indent=4)

# Caminho do arquivo coordenadas.json
caminho_json = 'coordenadas.json'
atualizar_coordenadas(caminho_json)

print("Coordenadas salvas no arquivo coordenadas.json.")