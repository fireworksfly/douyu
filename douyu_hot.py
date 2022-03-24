from selenium import webdriver
import time
import pandas as pd

if __name__ == '__main__':
    url = 'https://www.douyu.com/directory'
    # 网游竞技
    competeGame = '//*[@id="allCate"]/section/div[1]/div/div[2]/div/a[2]/strong'
    # 单机手游
    singleGame = '//*[@id="allCate"]/section/div[1]/div/div[2]/div/a[3]/strong'
    # 手游休闲
    handGame = '//*[@id="allCate"]/section/div[1]/div/div[2]/div/a[4]/strong'
    # 娱乐天地
    entertainment = '//*[@id="allCate"]/section/div[1]/div/div[2]/div/a[5]/strong'
    # 科技文化
    technology = '//*[@id="allCate"]/section/div[1]/div/div[2]/div/a[7]/strong'
    xpath_list = [competeGame, singleGame, handGame, entertainment, technology]
    class_name = ['网游竞技', '单机手游', '手游休闲', '娱乐天地', '科技文化']
    headers = ['分区名', '热度']
    df = pd.DataFrame(columns=headers)
    df.to_excel('./分区热度.xlsx', index=False)
    writer = pd.ExcelWriter('./分区热度.xlsx')
    driver = webdriver.Chrome("H:\Google\Chrome\Application\chromedriver.exe")
    # 先定位到网页
    driver.get(url)
    time.sleep(2)
    i = 0
    for xpath in xpath_list:
        df1 = pd.DataFrame(columns=headers)
        driver.find_element('xpath', xpath).click()
        time.sleep(2)
        channel_list = driver.find_elements('xpath', '//*[@id="allCate"]/section/div[2]/ul/li')
        for channel in channel_list:
            temp = []
            name = channel.find_element('xpath', './a/strong').get_attribute('textContent')
            popularity = channel.find_element('xpath', './a/div/span').get_attribute('textContent')
            temp = [name, popularity]
            df1 = pd.concat([df1, pd.DataFrame([temp], columns=headers)], ignore_index=True)
        df1.to_excel(excel_writer=writer, index=False, sheet_name=class_name[i])
        print(class_name[i])
        i +=1
    writer.save()
    driver.quit()
