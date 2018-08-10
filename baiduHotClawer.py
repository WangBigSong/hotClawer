'''
Created on 2018年5月31日

@author: big_song
'''
import selenium.webdriver
from selenium.webdriver.common.by import By 
import time
'''
获取百度热搜关键字
'''
def getBaiduKeyWord(Kword,url):
    keyWordlist = [];
    driver = selenium.webdriver.Firefox();
    driver.get(url);
    # 程序睡眠2秒 等待页面加载完毕
    time.sleep(2);
    # 解析元素
    list_table = driver.find_element(By.CLASS_NAME, "mainBody").find_element(By.CLASS_NAME, "grayborder").find_element(By.CLASS_NAME, "list-table");
    # 获取单元格里所有的tr
    tr_info = list_table.find_elements(By.TAG_NAME, "tr");
    # 循环tr获取每个单元格里的数据 跳过第一行标题行 
    for tr in tr_info[1:]:
        td = tr.find_elements(By.TAG_NAME, "td");
        if(len(td) == 1):continue;
        else :
            for value in td[1:2]:
                # print(value.text)
                keyWordlist.append(value.text);

    # print(keyWordlist)            
    # 将爬取的关键字写入到本地文件中'
    fileUrl="G:/read/baiduHotSerach/keyword_"+Kword+".txt"
    file = open(fileUrl, "a+");
    # 修改定位到文件最开始 
    file.seek(0)
    # 清空文件內容
    file.truncate();
    for word in keyWordlist:
        file.write(word + "\n")
    file.close();    
    driver.quit();

'''
获取热点榜首首页信息以及路径
'''
def clickHotType():
    valueMap = {};
    foxDriver = selenium.webdriver.Firefox();
    foxDriver.get("http://top.baidu.com/category?c=513&fr=topcategory_c513");
    time.sleep(2)
    liList = foxDriver.find_element(By.CLASS_NAME, "wrapper").find_element(By.ID, "main").find_element(By.ID, "flist").find_elements(By.TAG_NAME, "li");
    for li in liList[1:]:
        li_href = li.find_element(By.TAG_NAME, "a").get_attribute("href");
#         print('%s---%s' % (li.text, li_href))
        valueMap[li.text] = li_href;
    foxDriver.quit();    
    return valueMap;     


if __name__ == "__main__":
#     foxDriver = selenium.webdriver.Firefox();
#     foxDriver.get("http://top.baidu.com/category?c=513&fr=topcategory_c513");
    valMap=  clickHotType()
    print(valMap) 
    for k in valMap:
        getBaiduKeyWord(k,valMap[k])