
class BotLongPoll:
    def __init__(self, parent, group_id):
        self.parent = parent
        self.group_id = group_id
        self.vk = self.parent.vk

    def get_server(self): #  group_id={0}
        r = self.vk._vkApi_call('groups.getLongPollServer', {'group_id':self.group_id})
        return r.get('server'), r.get('key'), r.get('ts')

    def set_server(self):
        server, key, self.ts = self.get_server()
        self.get_event_url = '{0}?act=a_check&key={1}{2}'.format(server, key, '&ts={0}&wait=20')

    def listen(self):
        result = self.vk.client.load_info(self.get_event_url.format(self.ts))
        ts = result.get('ts')
        if ts == None: 
            print("get_event: ", result)
            self.set_server()
            return ()
        self.ts = ts
        return result['updates']
    
    def run(self):
        self.set_server()
        while True:
            events = self.listen()
            while events:
                event = events.pop()
                yield event
