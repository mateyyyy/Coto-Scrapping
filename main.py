import requests
from bs4 import BeautifulSoup

def get_price(url):
    prices = []
    names = []
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    li_items = soup.find_all('li', {"class" : "clearfix"})
    for li in li_items:
        name = li.find("div", {"class": "descrip_full"}).text
        price = li.find("span", {"class" : "atg_store_newPrice"}).text
        price = "".join(price.split())
        price = price.replace('$', '')
        price = price.replace('.', '')
        price = price.replace(',', '.')

        prices.append(float(price))

        names.append(name)

    n = len(prices)
    result = [{'name': names[i], 'price': prices[i]} for i in range(n)]
    print(result)

producto = input('Ingrese el producto a buscar : ')
producturl = f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&Dy=1&Ntt={producto}&Nty=1&Ntk=&siteScope=ok&_D%3AsiteScope=+&atg_store_searchInput={producto}&idSucursal=200&_D%3AidSucursal=+&search=Ir&_D%3Asearch=+&_DARGS=%2Fsitios%2Fcartridges%2FSearchBox%2FSearchBox.jsp"

try:
    get_price(producturl)
except:
    print('Producto no encontrado..')

