import requests

url = "https://saitama-premium-search.com/_nuxt/66b3f16.js"

r = requests.get(url)
print(r.status_code)
print(r.text)