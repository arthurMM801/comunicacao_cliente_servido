import threading
import requests

url = "https://belmondojr.dev/proc_paralelo.php?"
# https://belmondojr.dev/proc_paralelo.php?matrixA=[[1],[2]]&matrixB=[[1,2]]
updatedUrl = url

matrixA = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
]

matrixB = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

resultMatrix = []

def sendReq(line, matrixB):
    auxUrl = f"{url}matrixA=[{line}]&matrixB={matrixB}"
    print(auxUrl)
    
    get = requests.get(auxUrl)
    res = get.content
    resultMatrix.append(res)

for i in range(len(matrixA)):
    thread = threading.Thread(target=sendReq, args=(matrixA[i], matrixB))
    thread.start()
    thread.join()

print(resultMatrix)