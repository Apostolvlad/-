from location.location import LocationLocations
class House(LocationLocations):
    def init(self):
        self.name = 'Моя халупа'
        self.attachment = 'photo-179475703_457239041' #'photo-179475703_457239039'
        #self.add_button(0, 'Склад', self.open_shop, 'negative')
        self.add_button(0, 'Статус', self.open_hero, 'negative')
        self.add_button(0, 'Перекрёсток', self.back, 'negative')

        self.msgs = (
            'Воот, это моя крепость, моя твердыня, моя лачуга... мда.',
            'А в этот раз не заплутал, добрался таки до дома.',
            'Я рад что ты у меня есть, хоть и такой убогий и грязный..., но мой.'
            )

    # send_msg должен быть вне класса!!!!, в manager_loc, ибо, кнопки текущей локации, могут менять саму локацию!!!!, а значит и keyboard сменится.
    def back(self, word):
        self.player.set_location('Crossroad') #self.parent.api.send_msg(self.parent.info_user.name, self.parent.info_user.user_id, self.keyboard)
    
    def open_hero(self, word):
        self.player.set_location('Hero')
    
    def open_shop(self, word):
        pass