import requests
from bs4 import BeautifulSoup
import time

def news_crawler(url):
    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.text, 'html5lib')

    text = soup.find('div', id='ch_p').p.text
    return text





def check_keywords(input_string):
    # 定義關鍵字清單
    keywords = [
        "军事训练",
        "实弹射击训练",
        "射击训练",
        "实弹射击",
        "火箭残骸坠落",
        "军事任务",
        "实兵演习",
        "残骸坠落"
    ]
    
    # 檢查字串中是否包含任何關鍵字
    for keyword in keywords:
        if keyword in input_string:
            return True  # 如果包含關鍵字，返回 True
    
    return False  # 如果沒有任何關鍵字，返回 False

def nsa_crawler(nsa, url):
    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.text, 'html5lib')

    common_list = soup.find_all('li', class_='common_list')

    for news in common_list:
        title = news.a.span.text.strip()
        keyword = check_keywords(title)
        href = 'https://www.msa.gov.cn' + news.a['href']
        publish_time = news.find('span', class_='time').text.strip()
        if keyword:
            text = news_crawler(href)
            info = {
                'nsa': nsa,
                'title': title,
                'publish_time': publish_time,
                'keyword': keyword,
                # 'href': href,
                'text': text
            }
            print(info)
        

nsa_dict = {
    '上海海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=94DF14CE-1110-415D-A44E-67593E76619F&pageSize=20&pageNo=1&isParent=0',
    '天津海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=BDBA5FAD-6E5D-4867-9F97-0FCF8EFB8636&pageSize=20&pageNo=1&isParent=0',
    '遼寧海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=C8896863-B101-4C43-8705-536A03EB46FF&pageSize=20&pageNo=1&isParent=0',
    '河北海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=93B73989-D220-45F9-BC32-70A6EBA35180&pageSize=20&pageNo=1&isParent=0',
    '山東海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=36EA3354-C8F8-4953-ABA0-82D6D989C750&pageSize=20&pageNo=1&isParent=0',
    '浙江海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=8E10EA74-EB9E-4C96-90F8-F891968ADD80&pageSize=20&pageNo=1&isParent=0',
    '福建海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=7B084057-6038-4570-A0FB-44E9204C4B1D&pageSize=20&pageNo=1&isParent=0',
    '廣東海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=1E478D40-9E85-4918-BF12-478B8A19F4A8&pageSize=20&pageNo=1&isParent=0',
    '廣西海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=86DE2FFF-FF2C-47F9-8359-FD1F20D6508F&pageSize=20&pageNo=1&isParent=0',
    '海南海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=D3340711-057B-494B-8FA0-9EEDC4C5EAD9&pageSize=20&pageNo=1&isParent=0',
    '長江海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=93404234-06CC-4507-B2FB-8AF2492D2A3D&pageSize=20&pageNo=1&isParent=0',
    '江蘇海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=B5B0F3C7-630D-4967-B1E6-B06208575D15&pageSize=20&pageNo=1&isParent=0',
    '深圳海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=325FDC08-92B4-4313-A63E-E5C165BE98EC&pageSize=20&pageNo=1&isParent=0',
    '連雲海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=FA4501F3-DBE4-4F70-BC72-6F27132D4E04&pageSize=20&pageNo=1&isParent=0',
    '江蘇省地方海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=D14ED012-960B-4064-9712-70459A4A0D4D&pageSize=20&pageNo=1&isParent=0',
    '江西省地方海事局': 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=533B3954-E373-4C81-83E9-7D85B76BC9C5&pageSize=20&pageNo=1&isParent=0'
}


for key, value in nsa_dict.items():
    nsa_crawler(key, value)
    time.sleep(0.5)
# nsa_crawler('遼寧海事局', 'https://www.msa.gov.cn/page/openInfo/articleList.do?channelId=C8896863-B101-4C43-8705-536A03EB46FF&pageSize=20&pageNo=1&isParent=0')
# news_crawler('https://www.msa.gov.cn/page/article.do?articleId=6201EE94-CF85-4EC5-83FE-41B2ACD04752&channelId=C8896863-B101-4C43-8705-536A03EB46FF')