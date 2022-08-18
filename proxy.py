import json
import csv
import mitmproxy
import time

class Modify:
    def response(self, flow:mitmproxy.http.HTTPFlow):
        str = '/aweme/v1/web/aweme/favorite/'
        if flow.request.url.startswith('https://www.douyin.com/aweme/v1/web/aweme/favorite/'):

            csvfile = open('love.csv', 'a',encoding='utf-8-sig')
            csv_wri = csv.writer(csvfile)

            fp = open('keyword.txt', 'a',encoding='utf-8-sig')


            text = flow.response.text
            res_json = json.loads(text)
            datas = res_json['aweme_list']

            for data in datas:
                try:
                    desc = data['desc']
                except Exception as e:
                    desc = ''
                
                try:
                    create_time = time.localtime(int(data['create_time']))
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S",create_time)
                except Exception as e:
                    create_time = ''
                
                try:
                    author = data['author']['nickname']
                except Exception as e:
                    author = ''

                try:
                    short_id = data['author']['short_id']
                except Exception as e:
                    short_id = ''
                
                try:
                    uid = data['author']['uid']
                except Exception as e:
                    uid = ''

                try:
                    music_url = data['music']['play_url']['uri']
                except Exception as e:
                    music_url = ''
                
                try:
                    suggest_words1 = data['suggest_words']['suggest_words'][0]['words'][0]['word']
                except Exception as e:
                    suggest_words1 = ''

                try:
                    suggest_words2 = data['suggest_words']['suggest_words'][1]['words'][0]['word']
                except Exception as e:
                    suggest_words2 = ''
                
                try:
                    suggest_words3 = data['suggest_words']['suggest_words'][2]['words'][0]['word']
                except Exception as e:
                    suggest_words3 = ''

                try:
                    video_tag1 = data['video_tag'][0]['tag_name']
                except Exception as e:
                    video_tag1 = ''
                
                try:
                    video_tag2 = data['video_tag'][1]['tag_name']
                except Exception as e:
                    video_tag2 = ''
                
                try:
                    video_tag3 = data['video_tag'][2]['tag_name']
                except Exception as e:
                    video_tag3 = ''
                
                try:
                    video_url = 'https://www.douyin.com/video/' + data['aweme_id']
                except Exception as e:
                    video_url = ''

                keywords = desc #+ video_tag1 + video_tag2 + video_tag3 +suggest_words1 +suggest_words2 +suggest_words3
                keywords = keywords.replace('抖音','').replace('DOU','').replace('小助手','').replace('拍生活记录日常vlog','')

                csvItem = [desc,create_time,author,short_id,video_url,music_url,video_tag1,video_tag2,video_tag3,suggest_words1,suggest_words2,suggest_words3]
                csv_wri.writerow(csvItem)

                fp.write(keywords+'\n')

                
            fp.close()
            csvfile.close()

addons = [
	Modify()
]
