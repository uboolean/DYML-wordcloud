from asyncio.windows_events import NULL
import os
import wordc
import pandas
from selenium import webdriver

path = os.getcwd()

def startChrome():
    #配置浏览器
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=127.0.0.1:8080')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.get('https://www.douyin.com/')
    # tool.judge(driver)
    # tool.gotoMyIndex(driver)
    # tool.gotoLove(driver)
    return driver

    

def addtitle():
        add = pandas.read_csv('love.csv',header=None,names=['文案','发布时间','作者','作者抖音号','视频链接','视频音乐链接','视频标签1','视频标签2','视频标签3','抖音建议关键词1','抖音建议关键词2','抖音建议关键词3'])
        add.to_csv('love.csv',index=False,encoding='utf-8-sig')

if __name__ == '__main__':
    print('请启动mitmdump代理\n命令:mitmdump -s proxy.py')
    driver = NULL
    while True:
        print('1.已经完成代理\n2.浏览器已经处于喜欢界面最底端\n3.退出')
        i = input()
        if i=='1':
            driver = startChrome()
            print('请登录并滑动喜欢页面至最底端')
        elif i == '2':
            addtitle()
            wordc.makewc()
            driver.close()
            print('词云生成完成,相关生成文件说明:\nkeyword.txt为所有喜欢视频文案\nlove.csv为喜欢视频数据包括视频文案,作者昵称,视频标签,官方建议关键词等等')
            break
        elif i =='3':
            driver.close()
            break
        else:
            print('输入有误')
