import requests

url="https://official-joke-api.appspot.com/random_joke"
json_data=requests.get(url). json()

arr= ["",""]
arr[0]=json_data["setup"]
arr[1] = json_data["punchline"]
def joke():
    return arr

""" arr = joke()
print(arr[0])
#speak(arr[0])
print(arr[1])
#speak(arr[1]) """