from location.location import LocationLocations
class Crossroad(LocationLocations):
    def init(self):
        self.name = 'Перекрёсток'
        self.attachment = 'photo-179475703_457239042%2F'#'photo-179475703_457239036'
        self.add_button(0, 'Арена', self.open_arena, 'negative')
        self.add_button(0, 'Лачуга', self.open_house, 'negative')
        #self.add_button(0, 'Магазин', self.open_shop, 'negative')
        
        self.msgs = (
            'Бреду, бреду, куда бреду, я сам не понимаю... Возможно я в плену...',
            'Опа..., что это у нас тут? Это перекрёсток, и куда теперь направит он меня?',
            'Я забыл куда мне нужно...'
            )

    # send_msg должен быть вне класса!!!!, в manager_loc, ибо, кнопки текущей локации, могут менять саму локацию!!!!, а значит и keyboard сменится.
    def open_arena(self, word):
        self.player.set_location('Arena')
            
    def open_house(self, word):
        self.player.set_location('House')
    
    def open_shop(self, word):
        pass