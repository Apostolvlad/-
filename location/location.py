import json
from random import randint

class Location:
    locations = dict()
    def __init__(self, parent):
        self.parent = parent
        self.manager_location = self.parent.manager_location
        self.manager_player = self.parent.manager_player
        self.manager_location.add(self.class_name, self)
        
        self.labels = dict()
        self.buttons = list()
        
        self.name = '' # название локи
        self.attachment = ''
        self.keyboard = {"one_time":True, "buttons":self.buttons}

        self.init()
        self.keyboard = json.dumps(self.keyboard, ensure_ascii=False)
        
    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def player(self):
        return self.manager_player.player

    def init(self):
        pass
    # функция позволяет проверить условие нахождения в перейдённую локацию. и вернутся на предыдущую, если условия не выполнены.
    def check_access(self, location_back):
        pass

    def add_button(self, str_num, text, func, color):
        self.labels.update({text:func})
        if len(self.buttons) <= str_num: self.buttons.append(list())
        self.buttons[str_num].append({"action": {"type": "text", "label": text},"color": color})

    # всегда вызывается
    def msg(self):
        return '-'
        
    def not_func(self, word):
        pass
    
    def process_word(self, word):
        self.labels.get(word, self.not_func)(word)

class LocationLocations(Location):
    def __init__(self, parent):
        self.msgs = list()
        super().__init__(parent)
        self.msgs_max = len(self.msgs) - 1
        
    @property
    def msg_random(self):
        return self.msgs[randint(0, self.msgs_max)]# if self.msgs_max > -1 else ''
    
    def msg(self):
        return f'{self.player.name}[{self.name}]\n{self.msg_random}'
    
