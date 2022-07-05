import requests

# www.vedantcomputers.com uses CMS OpenCart

url = "https://www.vedantcomputers.com/"

while(True):
    print('\n')
    search = input("Search Product: ")
    print('\n')
    querystring = {"route": "journal3/search", "search": search}

    payload = ""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "X-Requested-With": "XMLHttpRequest",
        "Alt-Used": "www.vedantcomputers.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=querystring)

    data = response.json()

    '''
    for i in range(len(data['response'])):
        try:
            print(data['response'][i]['name'])
            print(data['response'][i]['price'])
            print(data['response'][i]['href'])
            print('\n')
        except:
            pass
    '''
    for i in range(len(data['response'])-1):  # ignoring last value
        print(data['response'][i]['name'])
        print(data['response'][i]['price'])
        print(data['response'][i]['href'])
        print('\n')
