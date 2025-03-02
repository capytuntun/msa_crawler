from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

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
def nsa_crawler(nsa, url, today):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 啟用無頭模式
    chrome_options.add_argument("--disable-gpu")  # 防止某些環境報錯
    driver = webdriver.Chrome(options=chrome_options)  # 如果 chromedriver 在 PATH 中，不需要指定路徑
    driver.get(url=url)  # 打開網頁

    li_elements = driver.find_elements(By.TAG_NAME, "li")

    data_list = []
    for li in li_elements:
        try:
            title = li.find_element(By.TAG_NAME, "a").text
            keyword = check_keywords(title)
            publish_time = li.find_element(By.TAG_NAME, "span").text
            href = li.find_element(By.TAG_NAME, "a").get_attribute("href")
            if publish_time == today:
                if keyword:
                    info = {
                        'nsa': nsa,
                        'title': title,
                        'publish_time': publish_time,
                        'keyword': keyword,
                        'href': href,
                    }
                    data_list.append(info)
        except Exception as e:
            print("跳過無效的 <li>", e)
    driver.quit()
    for item in data_list:
        print(item)

def main(nsa_dict):
    today = datetime.today().strftime('%Y-%m-%d')
    for key, value in nsa_dict.items():
        nsa_crawler(key, value, today)
        time.sleep(0.5)

if __name__ == "__main__":   
    nsa_dict = {
        '厦门海事局': 'https://www.fj.msa.gov.cn/fjmsacms/cms/html/xmhsjwwwz/hxtjg/index.html',
        '漳州海事局': 'https://www.fj.msa.gov.cn/fjmsacms/cms/html/zzhsjwwwz/hxtjg/index.html',
        '莆田海事局': 'https://www.fj.msa.gov.cn/fjmsacms/cms/html/pthsjwwwz1/hxjtg/index.html',
        '宁德海事局': 'https://www.fj.msa.gov.cn/fjmsacms/cms/html/ndhsjwwwz/aqjs/index.html',
        '平潭海事局': 'https://www.fj.msa.gov.cn/fjmsacms/cms/html/pthsjwwwz/hxtjg/index.html'
    }
    main(nsa_dict)