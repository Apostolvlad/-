import requests

# from client import Client
class Client:
    def __init__(self, user_agent = None): # 
        #print("Создание сессии ", end = '')
        self.session = requests.Session() 
        #print("- УСПЕШНО!", date = False)
        if user_agent != None:
         #   _print("Установка user agent: ", user_agent, end = '')
            self.session.headers.update({'User-Agent': user_agent})
          #  _print("- УСПЕШНО!", date = False)
    '''
    text, json
    '''
    def load_info(self, url, mode = 'json', dicts = {}):
        #_print("Получаем данные ", end = '')
        if dicts == {}:
            try:
                request = self.session.get(url, timeout=123, verify = True)
            except Exception as e:
                return {}
        else:
            try:
                request = self.session.post(url, dicts, timeout=123, verify = True)
            except Exception as e:
                return {}
        #_print("- УСПЕШНО!", date = False)
        if mode == 'json':
            try: 
                return request.json()
            except:
                return {}
        elif mode == 'text':
            try: 
                return request.text
            except:
                return {}
        return {}

    def load_headers(self, url, mode_stream = True):
        #_print("Получаем данные ", end = '')
        request = self.session.head(url)#, stream = mode_stream) 
        #request.raise_for_status()
        #_print("- УСПЕШНО!", date = False)
        return request.headers
    
    def save_picture(self, url, path):
        p = self.session.get(url)
        out = open(path, "wb")
        out.write(p.content)
        out.close()