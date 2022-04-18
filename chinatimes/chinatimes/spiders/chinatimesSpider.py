import scrapy
import requests
from bs4 import BeautifulSoup
# from chinatimes.items import ChinatimesItem

###########################################################################################################################
# 中國時報搜尋 url 格式
# 關鍵字（不給不行、一定要給)
# page 頁數
# 排序為降冪
# Week1：20220224 ~ 20220302
# Week5：20220324 ~ 20220330

class ChinatimesspiderSpider(scrapy.Spider):
    name = 'chinatimesSpider'
    allowed_domains = ['chinatimes.com']
    #start_urls = ['https://www.chinatimes.com/search/烏克蘭?page=1&chdtv']
    page_temp_url = "https://www.chinatimes.com/search/烏克蘭?page=%d&chdtv"
    cur_page = 127     # week1 startpage
    #cur_page = 23     # week5 startpage
    max_page = 186     # week1 endpage
    #max_page = 41     # week5 endpage
    start_urls = [page_temp_url % (cur_page)]
    ### after properties
    #start_urls = ['https://www.chinatimes.com/search/烏克蘭?page=106&chdtv']
    #cur_page = 106
    #max_page = 164    # result after survey

    def parse(self, response):
        print( '[ChinatimesspiderSpider] Enter parse:', response, type(response), dir(response) )
        # 如果想查看網頁內容，就打開以下的 print
        #print( '-'*120, '\n[LibnewsspiderSpider:parse] body:\n', response.body)
        # xpath: /html/body/div[2]/div/div[2]/div/section/div/ul
        #level_1_list = response.xpath('//*[@class="vertical-list list-style-none"]')
        level_1_list = response.xpath('/html/body/div[2]/div/div[2]/div/section/div/ul/li')
        for sublink in level_1_list:
            #print('===>', sublink.xpath('div/div/div[2]').get())

            #/html/body/div[2]/div/div[2]/div/section/div/ul/li[4]/div/div/div[2]/h3/a
            #/html/body/div[2]/div/div[2]/div/section/div/ul/li[9]/div/div/div/h3/a
            URL = sublink.xpath('div/div/div/h3/a/@href' ).get()       # 此選擇節點下，找到的第一個 <a href=""...> tag 
            title = sublink.xpath('div/div/div/h3/a/text()' ).get()    # 此選擇節點下，找到的第一個 <a title=""...> tag
            #/html/body/div[2]/div/div[2]/div/section/div/ul/li[4]/div/div/div[2]/div/div/a
            category = sublink.xpath('div/div/div/div/div/a/text()' ).get()    # 此選擇節點下，找到的第一個 <div...> tag
            # /html/body/div[2]/div/div[2]/div/section/div/ul/li[4]/div/div/div[2]/div/time
            up_datetime = sublink.xpath('div/div/div/div/time/@datetime' ).get()  # 此選擇節點下，找到的第一個 <div...><time ...> tag

            # 目前頁面只能收集到這四個欄位
            #print('Got a record(L1) ===>', URL, title, category, up_datetime )
            # create a item object
            a_item = { 'url': URL, 'title': title, 'category': category, 'up_datetime': up_datetime }

            if a_item['url'] is not None:
                yield scrapy.Request(response.urljoin(a_item['url']), meta={'item_1': a_item}, callback=self.parse_newscontent) #, dont_filter=True
            else:
                print("[Level-1 parse] sublink is invalid.\n")

        # 下一頁就是 cur page + 1
        self.cur_page += 1
        level_1_next = self.page_temp_url % (self.cur_page)
        if self.cur_page <= self.max_page:
            # Send the next-page request, and use THIS function as callback handler
            print('Next page ====> ', level_1_next)
            yield scrapy.Request(response.urljoin(level_1_next), callback=self.parse)
        else:
            print("[Level-1 parse] no next button.\n")


    def parse_newscontent(self, response):
        '''這是在搜尋頁面，按進某則新聞的處理函式
        '''
        print( '[ChinatimesspiderSpider] Enter parse_newscontent' )

        dict_item = response.meta['item_1']
        #print( '在 (L1) 取得的資料：', dict_item )

        # 再來要怎麼拿到最後的 content 呢？
        #//*[@id="page-top"]/div/div[2]/div/div/article/div/div[1]/div[2]
        # //*[@id="page-top"]/div/div[2]/div/div/article/div/div[1]/div[2]/div[2]/div[2]
        #level_2_root = response.xpath('//*[contains(@class, "article-body")]')
        
        #level_2_root = response.xpath('//*[@id="page-top"]')
        level_2_root = response.xpath('//*[contains(@class, "article-body")]')
        level_2_content = level_2_root.xpath('p/text()')
        dict_item['content'] = ''
        for i in level_2_content:
            #print(i.get())
            dict_item['content'] += i.get()
            #print(content)
        #print(dict_item)                
        yield  dict_item