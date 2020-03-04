from vk.client import Client
from json import dumps
class Vk:
    def __init__(self, token):
        self.client = Client()
        self.token = token
        self.version = '5.103'
    
    def _vkApi_call(self, method_name, params, _resp = True):
        params.update({'access_token':self.token, 'v':self.version})
        result = self.client.load_info('https://api.vk.com/method/{0}'.format(method_name), mode = 'json', dicts=params)#'{1}&access_token={2}&v={3}'.format(method_name, params, self.token, self.version))
        if _resp == True: 
            return result.get('response')
        return result
    
    def send(self, message, peer_id, keyboard = None, attachment = None):
        return self._vkApi_call('messages.send', {'attachment':attachment,'message':message, 'peer_id':peer_id, 'keyboard':keyboard, 'random_id':0}) #random.randint(0, 1000000000)
    
    def execute(self, code):
        return self._vkApi_call('execute', {'code':code})
    
    def execute_send(self, msgs):
        code = 'var msgs = {0};{1}'.format(dumps(msgs, ensure_ascii=False), 'var i = 0; while(i < msgs.length){API.messages.send(msgs[i]);i= i+1;}return msgs.length;')
        return self.execute(code)