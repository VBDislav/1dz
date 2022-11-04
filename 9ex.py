import urllib.request
import requests

opener = urllib.requests.build_opener()
response = opener.open ("https://httpbin.org/get")
print(response.read())
response = requests.get("https://httpbin.org/get")
print(response.content)






import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatype - {type(response.content)}")
print(response.text)
print(f"Datatype - {type(response.text)}")





import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
print(response.text)
response.text = response.text
response_parse = response_text.split("</span>")
for parse_elem_1 in 
    if parse_elem_1.starswith("$")
        for parse_elem_2 in parse_elem_1.split("/span")
             if parse_elem_2.starwith("$") and parse_elem_2[1].isdigit():
                 print(parse_elem_2)
                 res_parse_list.append(parse_elem_2)
btc = res_parse_list[0]
print(btc)





from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
for elem in soup_list:
    print(elem)
    res = soup_list[0].find("span")
    print(res.text)
