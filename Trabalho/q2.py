# 2. Transações Distribuídas: Desenvolva um sistema distribuído de e-commerce onde
# usuários podem realizar transações de compra
# (https://belmondojr.dev/compra.php?&products[]=Item1&amounts[]=10.50&products[]=Item2&amounts[]=20.75 
# O item representa o produto comprado e o
# amounts, o preço. Você receberá como retorno o valor total da compra)**
import threading
import requests

url = "https://belmondojr.dev/compra.php?"
updatedUrl = url

products = []
amounts = []
values = []

def addValuestoUrl(url, item, preco, arr):
    url += f"products[]={item}&values[]={preco}&"
    print(url)
    arr.append(url)

def comprar(item, valor):
    products.append(item)
    amounts.append(valor)

def updateUrl(url, arr):
    print(arr)
    arr[-1] = (arr[-1])[:-1]
    for i in range(len(arr)):
        url += arr[i]
    return url

comprar("Sapato", 10)
comprar("Banana", 2)
comprar("Prato", 20)

for i in range(len(products)):
    thread = threading.Thread(target=addValuestoUrl, args=("", products[i], amounts[i], values))
    thread.start()
    thread.join()

res = updateUrl(updatedUrl, values)
post = requests.get(res)
response = post.content
print(response)
