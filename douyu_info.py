from selenium import webdriver
import time
import re
import pandas as pd


class Dou_yu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/g_LOL'
        self.driver = webdriver.Chrome("H:\Google\Chrome\Application\chromedriver.exe")
        self.headers = ['房间号', '标题', '主播名', '主播称号', '热度', '分区']
        self.page = 1
    def parse_data(self):
        # 建议加上这个休眠，不然可能会因为网速问题，导致页面未加载完毕，爬取失败
        time.sleep(1)
        # 每一页的所有房间存入列表
        room_list = self.driver.find_elements('xpath', '//*[@id="listAll"]/div[2]/ul/li/div')

        data_list = []
        for room in room_list:
            tmp = []
            tmp.append(re.sub(r'.*/', '', room.find_element('xpath', './a').get_attribute('href')))
            tmp.append(room.find_element('xpath', './a/div[2]/div[1]/h3').get_attribute('textContent'))
            tmp.append(room.find_element('xpath', './a/div[2]/div[2]/h2/div').get_attribute('textContent'))
            tmp.append(room.find_element('xpath', './a/div[2]/span').get_attribute('textContent'))
            tmp.append(room.find_element('xpath', './a/div[2]/div[2]/span').get_attribute('textContent'))
            tmp.append(room.find_element('xpath', './a/div[2]/div[1]/span').get_attribute('textContent'))
            data_list.append(tmp)
        print('爬完了第' + str(self.page) + '页')
        self.page +=1
        return data_list

    def save_data(self, data_list):
        # # 先转换为str，方便写入文件
        # data_list = str(data_list)
        # with open('斗鱼.txt', 'a', encoding='utf-8') as f:
        #     f.write(data_list + '\n')
        df = pd.read_excel('./直播间信息.xlsx')
        for data in data_list:
            df = pd.concat([df, pd.DataFrame([data], columns=self.headers)], ignore_index=True)
        df.to_excel('./直播间信息.xlsx', index=False)
    def run(self):
        df = pd.DataFrame(columns=self.headers)
        df.to_excel('./直播间信息.xlsx', index=False)
        self.driver.get(self.url)
        # url
        # 创建driver
        # 发送get
        # parse-data
        while True:
            data_list = self.parse_data()
            # save-data
            self.save_data(data_list)
            # 翻页
            # 这个time.sleep(1)是一定要写的（休眠时间自己设定），当时我是在这卡了很长的时间，因为发现网页并不下滑，所以也导致“下一页“这个元素点击失败。如果不设置休眠一秒，仔细看会发现，并不是页面不下滑，是页面下滑了之后又回到了顶部，可能这是一种反爬吧。
            time.sleep(1)
            # 直接设置一个比较大的值，下滑到底部
            js = 'scrollTo(0,10000)'
            # 执行js代码
            self.driver.execute_script(js)
            # 仔细观察斗鱼直播的第一页和最后一页，他们所属的li标签内的aria-disabled值不一样，不是尾页为faule，尾页为true，到尾页后跳出循环
            if self.driver.find_element('xpath', '//li[@title="下一页"]').get_attribute('aria-disabled') == 'true':
                break
            # 找到下一页按钮并点击
            self.driver.find_element('xpath', '//span[contains(text(),"下一页")]').click()


if __name__ == '__main__':
    dou_yu = Dou_yu()
    dou_yu.run()