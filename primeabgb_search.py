from bs4 import BeautifulSoup
import requests

# www.primeabgb.com uses CMS WordPress 5.9.3/ WooCommerce/ WPBakery/ AnsPress

# html_text = requests.get('https://www.amazon.in/s?k=sn550').text
while(True):

    search = input("search: ")

    html_text = requests.get(
        f'https://www.primeabgb.com/?s={search}&post_type=product&dgwt_wcas=1').text
    soup = BeautifulSoup(html_text, 'lxml')

    productName = soup.find_all('h3', class_='product-title')
    productDescription = soup.find_all('div', class_='short-description')
    productPrice = soup.find_all('ins')
    productLink = soup.find_all('h3', class_='product-title')

    for i in range(len(productName)):
        try:
            print(productName[i].text)
            print(productDescription[i].text)
            print(productPrice[i].text)
            print(productLink[i].a['href'])
            print(
                "_______________________________________________________________________\n")
        except:
            pass
    print("\n")
