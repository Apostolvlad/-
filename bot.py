#from logger import _print
from bd.bd_connect import Bd
from vk.longpoll import BotLongPoll
from vk.vk import Vk

from player.manager_player import ManagerPlayer
from location.manager_location import ManagerLocation

import time


class Bot:
    def __init__(self, token, group_id):
        self.vk = Vk(token)
        self.bd = Bd()
        self.longpoll = BotLongPoll(self, group_id)
        self.manager_player = ManagerPlayer(self)
        self.manager_location = ManagerLocation(self)

        self.messages = list()
        
    def process_event(self, updates):
        for obj in updates: 
            message = obj.get('object').get('message')
            user_id = message.get('peer_id')
            command = message.get('text')
            self.manager_player.select_player(user_id)
            self.add_message(self.manager_location.process_word(command), self.manager_player.user_id, self.manager_location.keyboard, self.manager_location.attachment) #
            self.manager_player.update_player()
            self.send()
        self.send(0)
        self.bd.commit()
        # пока думаю можем не заморачиваться, и чтобы всё корректно завершалось, можно применять применение в бд, сразу после обработки пака событий...
    
    def add_message(self, message, user_id, keyboard, attachment = None):
        self.messages.append({"message":message, "user_id":user_id, "keyboard":keyboard, "attachment":attachment, 'random_id':0})

    def send(self, count = 23):
        if len(self.messages) > count:
            self.vk.execute_send(self.messages)
            self.messages.clear()

    def run(self):
        self.longpoll.set_server()
        while 1:
            print('get update')
            updates = self.longpoll.listen()
            print('process_event')
            self.process_event(updates)
            #self.manager_player.check_save()
    

