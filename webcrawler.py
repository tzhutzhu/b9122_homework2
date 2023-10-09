import requests
from lxml import etree


# cookies = {
#     '_gid': 'GA1.2.125191735.1696816534',
#     '_ga': 'GA1.1.455469201.1696816534',
#     '_ga_DHNWEVCZW6': 'GS1.1.1696816533.1.1.1696817876.0.0.0',
#     '_ga_TK9BQL5X7Z': 'GS1.1.1696816533.1.1.1696817876.0.0.0',
# }


def task1():
    headers = {
        'authority': 'press.un.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gid=GA1.2.125191735.1696816534; _ga=GA1.1.455469201.1696816534; _ga_DHNWEVCZW6=GS1.1.1696816533.1.1.1696817876.0.0.0; _ga_TK9BQL5X7Z=GS1.1.1696816533.1.1.1696817876.0.0.0',
        'pragma': 'no-cache',
        'referer': 'https://press.un.org/en/sitesearch?search_api_fulltext=crisis&sort_by=field_dated',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'search_api_fulltext': 'crisis',
        'sort_by': 'field_dated',
    }

    response = requests.get('https://press.un.org/en/sitesearch', params=params, headers=headers)
    links = etree.HTML(response.text).xpath("//span[@class='field-content']/a/@href")
    print("question1:task1")
    for link in links:
        url = f"https://press.un.org{link}"
        print(url)


def task2():
    # import requests
    #
    # cookies = {
    #     'JSESSIONID': '54B04E2B5CC4530835976DFD6554EE69',
    #     'engnewsroomroute': 'node1',
    # }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'JSESSIONID=54B04E2B5CC4530835976DFD6554EE69; engnewsroomroute=node1',
        'Pragma': 'no-cache',
        'Referer': 'https://www.europarl.europa.eu/news/en/press-room?searchQuery=crisis',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'searchQuery': 'crisis',
    }

    response = requests.get('https://www.europarl.europa.eu/news/en/press-room', params=params,
                            headers=headers)
    links = etree.HTML(response.text).xpath("//div[@class='ep_title']/a/@href")
    print("question1 task2")
    for link in links:
        url = link
        print(url)


if __name__ == '__main__':
    task1()
    task2()
