from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 无界面访问
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://www.piyao.org.cn/2020yqpy/")
time.sleep(3)  # 留出加载时间

links = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/ul/li/a")
length = len(links)

for i in range(0, length):
    links = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/ul/li/a")
    link = links[i]
    url = link.get_attribute('href')  # 提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)  # 不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
    time.sleep(3)  # 留出加载时间
    title = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/h2").text  # .text的意思是指输出这里的纯文本内容
    print(title)
    Time = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/p/span").text
    print(Time)
    # content = driver.find_elements(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div[2]/p")
    content = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]").text
    print(content)
    # contentstr = ''
    # for i in range(len(content)):
    #   contentstr += content[i] + "\n"
    # print(contentstr)
    print("\n")
    driver.back()  # 后退，返回原始页面目录页
    time.sleep(1)
# driver.close()
