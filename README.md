#save-kfc-addr
保存肯德基每个城市分店地址<br>

#代码思路
    网站数据内容来源
    1.确定一下目标要求
        找到内容一个来源 确定url地址 
        只需请求 url地址 附参数 获取它网页源代码 即可获取内容
        怎么找到数据来源
            1.查看导航栏中url返回的数据内容<判断网页类型 静态/动态网页>
            2.f12-网络

    代码实现：
        1.对http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword实现post请求
        2.分析结果
        3.json 切片
        4.保存.csv文件

#文件功能
    city.py：
        输入城市名，保存{city}市kfc分布.csv

    demo.py
        自动下载全国kfc分布.csv

#已知问题
    存在重复地址（这问题找肯德基解决，或自行写去重代码）
