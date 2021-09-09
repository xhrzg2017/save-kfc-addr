import requests
import pprint
import time
import csv


def get_page(kw):
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
                'cname': '',
                'pid': '',
                'keyword': f'{kw}',
                'pageIndex': '1',
                'pageSize': '10'
            }
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42' }
    try:
        r = requests.post(post_url,data,headers)
        # print(r)
        json_data = r.json()
        # pprint.pprint(json_data)
        page = json_data['Table'][0]['rowcount']
        # print(page)
        if page % 10 > 0:
            page_num = page//10+1
        else:
            page_num =page//10
        return page_num
    except Exception as e:
        print(e)

def send_rquests(kw):
    page_num = get_page(kw)
    for page in range(1,page_num+1):
        print("=" * 20 + '正在爬取 {}'.format(kw)+'市 第{}页'.format(page) + "=" * 20)
        post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

        data = {
            'cname': '',
            'pid': '',
            'keyword': f'{kw}',
            'pageIndex': f'{page}',
            'pageSize': '10'
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42'}
        try:
            r = requests.post(post_url, data, headers)
            # print(r)
            json_data = r.json()
            # pprint.pprint(json_data)

            json_list = json_data['Table1']
            #print(json_list)

            for json_1 in json_list:
                storeName = json_1['storeName'] + '门店'
                cityName = json_1['cityName']
                addressDetail = json_1['addressDetail']
                pro = json_1['pro']
                print(storeName, cityName, addressDetail, pro, sep='|')

                with open(f'{kw}市kfc分布.csv', mode='a', newline="")as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow([storeName, cityName, addressDetail, pro])
        except Exception as e:
            print(e)
    time.sleep(0.2)

if __name__ == '__main__':
    city = input('请输入查询城市：')
    send_rquests(city)
