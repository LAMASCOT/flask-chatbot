import requests

url = "http://127.0.0.1:5000/ask"
question = "Quelle est la solution d'une erreur 500 ?"

payload = {"question": question}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

if response.ok:
    data = response.json()
    print("Réponse du chatbot :", data.get("answer"))
else:
    print(f"Erreur {response.status_code} :", response.text)
