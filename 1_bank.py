from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

date = sys.argv[1]
currency = sys.argv[2]
# 货币代号和对应的英文代码映射
currency_dict = {
    "港币": "HKD",
    "美元": "USD",
    "瑞士法郎": "CHF",
    "德国马克": "DEM",
    "法国法郎": "FRF",
    "新加坡元": "SGD",
    "瑞典克朗": "SEK",
    "丹麦克朗": "DKK",
    "挪威克朗": "NOK",
    "日元": "JPY",
    "加拿大元": "CAD",
    "澳大利亚元": "AUD",
    "欧元": "EUR",
    "澳门元": "MOP",
    "菲律宾比索": "PHP",
    "泰国铢": "THB",
    "新西兰元": "NZD",
    "韩元": "KRW",
    "卢布": "RUB",
    "林吉特": "MYR",
    "新台币": "TWD",
    "西班牙比塞塔": "ESP",
    "意大利里拉": "ITL",
    "荷兰盾": "NLG",
    "比利时法郎": "BEF",
    "芬兰马克": "FIM",
    "印度卢比": "INR",
    "印尼卢比": "IDR",
    "巴西里亚尔": "BRL",
    "阿联酋迪拉姆": "AED",
    "南非兰特": "ZAR",
    "沙特里亚尔": "SAR",
    "土耳其里拉": "TRY"
}
new_dict = {v : k for k, v in currency_dict.items()}
currency_code = new_dict.get(currency, "未知货币代号")


driver_path = r"E:\experiments\scrapy_learn\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_path)
driver.get('https://www.boc.cn/sourcedb/whpj/')
# print(driver.page_source)

# 输入日期和货币代号并查询
driver.find_element(By.NAME, "nothing").send_keys(date)
driver.find_element(By.NAME, "pjname").send_keys(currency_code)
driver.find_elements(By.CLASS_NAME, "search_btn")[1].click()


# 获取现汇卖出价
sell_rate_element = driver.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]')
sell_rate = sell_rate_element.text

# 将结果写入result.txt文件
with open('./result.txt', 'w', encoding="utf-8") as f:
    f.write(f"Date: {date}\nCurrency Code: {currency_code}\nSell Rate: {sell_rate}")

# 关闭浏览器
driver.quit()