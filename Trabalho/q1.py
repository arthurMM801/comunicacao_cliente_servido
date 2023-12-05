import threading
import requests

url = "https://belmondojr.dev/comunicacao.php?"
updatedUrl = url
dadosSensor = [36, 35, 34, 37, 38]
values = []

def addValuestoUrl(url, data, arr):
    url += f"sensors[]={data}&"
    arr.append(url)

for i in range(len(dadosSensor)):
    thread = threading.Thread(target=addValuestoUrl, args=("", dadosSensor[i], values))
    thread.start()
    thread.join()

def updateUrl(url, arr):
    arr[-1] = (arr[-1])[:-1]
    for i in range(len(arr)):
        url += arr[i]
    return url

res = updateUrl(updatedUrl, values)
post = requests.get(res)
response = post.content
print(response)