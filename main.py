import sys
import requests

from pdf import extract_kinmu_model_json

try:
    pdf = sys.argv[1]
except:
    print("Missing kinmu pdf")
    sys.exit()

kinmu_model: str = extract_kinmu_model_json(pdf)

with open('input.js', 'r') as c:
    js = c.read()

js = js.replace('KINMU_MODELS', kinmu_model)

payload = {'input': js}
url = 'https://javascript-minifier.com/raw'
r = requests.post(url, payload)

print(f"Just paste it into your browser js console and run it🔥\n↓\n{r.text}")
