# DYML-wordcloud
## 项目全名Douyin_My_Love_WORLDCLOUD(抖音喜欢词云图)


# 使用方法

1. 微软应用商店安装mitmproxy
2. 安装相关依赖 `pip install -r requirements.txt`
3. 运行 main.py
4. 根据提示另开power shell或者cmd启动代理
5. 根据提示到浏览器打开主页喜欢列表并滑动至最低端
6. 回到main.py进行相关输入

# 项目原理

利用mitmproxy进行抓包获取抖音喜欢的json数据,使用wordcloud等库对数据进行处理

问:为什么使用mitmproxy而不是直接使用selenium和browsermobproxy进行便捷操作?
答:抖音反爬虫技术强悍,会对selenium的操作进行屏蔽,使用browsermobproxy无法捕获到目的json(可能是我的配置有问题)

使用mitmproxy的优点:无需对抖音的各类加密值进行逆向破解


# 项目灵感来源于 暑假在家无聊
