from bs4 import BeautifulSoup
import requests

search = input("Search: ")

html_text = requests.get(
    f"https://www.thingbits.in/products?keywords={search}").text
soup = BeautifulSoup(html_text, 'lxml')

# use select for tags with multiple class names
productTitle = soup.select(".card.w-100.shadow-sm")
productLink = soup.select(
    '.card-footer.bg-transparent.d-flex.align-items-center.justify-content-between')
productPrice = soup.select('.h5.mb-0.text-primary')

for i in range(len(productPrice)):
    print(productTitle[i].a['title'])
    print(productPrice[i].text)
    print('https://www.thingbits.in'+productLink[i].a['href'])
    print('\n')
