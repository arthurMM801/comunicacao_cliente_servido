import threading
import requests

# Envio de Tarefas: Projete um sistema distribuído que permite o envio de uma
# ordenação de dados para os servidores disponíveis. Considere fatores como a carga
# de trabalho dos servidores
# (https://belmondojr.dev/ordenacao.php?method=bubbleSort&vector[]={5,2,1}.
# Aqui, o method pode receber bubbleSort e mergeSort e o vector recebe o vetor)

url = "https://belmondojr.dev/ordenacao.php?method=bubbleSort&"

data = [7,8,6,5,4,3,1,2]
urlData = ""
values = []

def addValuestoUrl(url, data, arr):
    url += f"vector[]={data}&"
    arr.append(url)

for i in range(len(data)):
    thread = threading.Thread(target=addValuestoUrl, args=(url, data[i], values))
    thread.start()
    thread.join()


def updateUrl(url, arr):
    arr[-1] = (arr[-1])[:-1]
    for i in range(len(arr)):
        url += arr[i]
    return url

res = updateUrl(urlData, values)
post = requests.get(res)
response = post.content
print(response)