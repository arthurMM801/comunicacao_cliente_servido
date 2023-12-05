import requests
import json
import threading
import time

def coletar_dados_sensor(url, resultado):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            resultado.append(dados)
        else:
            print(f"Erro ao coletar dados. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição: {e}")

def calcular_media(dados):
    if not dados:
        print("Sem dados para calcular a média.")
        return

    temperatura_total = 0
    umidade_total = 0
    pressao_total = 0

    for leitura in dados:
        temperatura_total += leitura.get("temperature", 0)
        umidade_total += leitura.get("humidity", 0)
        pressao_total += leitura.get("pressure", 0)

    total_leituras = len(dados)
    media_temperatura = temperatura_total / total_leituras
    media_umidade = umidade_total / total_leituras
    media_pressao = pressao_total / total_leituras

    print(f"Média de temperatura: {media_temperatura}°C")
    print(f"Média de umidade: {media_umidade}%")
    print(f"Média de pressão: {media_pressao}hPa")
    print()

url_sensores = "https://belmondojr.dev/sensores.php"
numthreads = 5
resultados = []

while(True):
    threads = []

    for i in range(numthreads):
        thread = threading.Thread(target=coletar_dados_sensor, args=(url_sensores, resultados))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    calcular_media(resultados)
    time.sleep(5)