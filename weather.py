import requests

url = "https://open-weather13.p.rapidapi.com/city/Cork/IE"

headers = {
	"X-RapidAPI-Key": "0f691b6eb9msh7d6ed086222f885p181ae7jsna136bb33eda2",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
