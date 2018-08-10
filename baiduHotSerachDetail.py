'''
Created on 2018年6月1日

@author: big_song
'''
# https://www.baidu.com/baidu?cl=3&tn=SE_baiduhomet8_jmjb7mjw&rsv_dl=fyb_top&fr=top1000&wd=%C1%E8%B3%BF3%B5%E3%B2%BB%BB%D8%BC%D2
import selenium.webdriver
from selenium.webdriver.common.by import By 
import time

def getHotSerachDetail(word):
    driver = selenium.webdriver.Firefox();
    url = "https://www.baidu.com/baidu?cl=3&tn=SE_baiduhomet8_jmjb7mjw&rsv_dl=fyb_top&fr=top1000&wd=" + word
    driver.get(url)
    time.sleep(2)
    divs = driver.find_element(By.ID, "container").find_element(By.ID, "content_left").find_elements(By.TAG_NAME, "div");
    for div in divs:
        h3_title = div.find_element(By.TAG_NAME, "h3");
        if "的最新相关信息" in h3_title.text:
            print(h3_title.text);
            valueDiv = div.find_element(By.CLASS_NAME, "c-offset").find_elements(By.TAG_NAME, "div");
            for value in valueDiv[0:1]:
                print("----------------------", value.text)
        break;   
if __name__ == "__main__":
    getHotSerachDetail("迪士尼偶遇江疏影");