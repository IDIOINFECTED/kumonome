from bs4 import BeautifulSoup
import logwriting
import re
import requests
from threading import Thread
#Video parser classes// TODO: add some hostings excepting YouTube
class Yt_Parser:
    #TODO: make playlists/channels modes
    def __init__(self, mode, max_views):
        self.mode = mode
        self.max_views = max_views

    def raw_search(self, query):
        url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"
        rpage = requests.get(url)
        soup = BeautifulSoup(rpage.text, "html.parser")
        s = soup.find_all("script")
        if self.mode == "vid":
            key = '"videoRenderer":'
            m = re.findall(key + r'(.*?)\{"playlistId":"WL","actions":\[\{"action":"', str(s))
        return m

    def get_params_vid(self, text):
        params = []
        # video id
        id_key = '"videoId":"'
        vidid = re.search(id_key + r'([^*]{11})', text)
        string_id = vidid[0]
        url = "https://www.youtube.com/watch?v=" + string_id[11:]
        params.append(url)
        # view_chk
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        views = re.findall(r'"viewCount":"(.*?)"', str(soup))
        vcnt = views[0]
        if int(vcnt) > self.max_views:
            pass
        else:
            params.append(int(vcnt))
            date_raw = re.findall(r'itemprop="datePublished"/><meta content="(.*?)" itemprop="uploadDate"', str(soup))
            dt = date_raw[0]
            params.append(dt.replace('T', ' at '))
            # video title
            t_text = re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"}],"accessibility":', text)
            title = t_text[0]
            params.append(title)
            # author
            p_text = re.findall(r'"webCommandMetadata":\{"url":"(.*?)","webPageType"', text)
            author = f"https://www.youtube.com{p_text[0]}"
            params.append(author)
            #preview
            try:
                thumbn = re.findall(r'"thumbnail":\{"thumbnails":\[\{"url":"(.*?)\?', text)
                thumblink = thumbn[0]
            except:
                thumblink = "<ThumbnailError>"
            params.append(thumblink)
            return params

    def search(self, query, log_mode):
        m = self.raw_search(query)
        if log_mode == 1:
            document = logwriting.Docx_log('logs.docx')
        for i in range(len(m)):
            l = str(m[i])
            params = self.get_params_vid(l)
            print(params)
            if params is None:
                pass
            try:
                if log_mode == 1:
                    document.add_pict(params[5], 'lastpreview.jpg')
            except:
                pass
            else:
                with open('logs.txt', 'a+', encoding='utf-8') as l:
                    try:
                        l.write(f'--{params[3]}--\nlink: {params[0]}\nuploaded by: {params[4]}\nupload date: {params[2]}\n{params[1]} views\n\n\n')
                    except TypeError:
                        pass
                if log_mode == 1:
                    document.logwrite(f'--{params[3]}--\nlink: {params[0]}\nuploaded by: {params[4]}\nupload date: {params[2]}\n{params[1]} views\n')


#test = Yt_Parser("vid", 999999999)
#test.search(".mkv", 'test.docx')
