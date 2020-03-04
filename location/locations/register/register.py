from location.location import Location, LocationLocations
class Register(LocationLocations):
    def init(self):
        self.name = 'Регистрация'
        self.attachment = ''
        #self.add_button(0, 'Арена', self.open_arena, 'negative')
        self.add_button(0, 'вспомнить имя', self.new_hero, 'negative')
        #self.add_button(0, 'Магазин', self.open_shop, 'negative')
        
        self.msgs = (
            'Упал, очнулся, ничего не помню...',
            'Моё прошлое имя было убого, поэтому я предпочёл его забыть...',
            'Хороша пьянка вчера была, аж имя своё позабыл...'
            )

    def new_hero(self, word):
        self.player.set_location('Register1')

class Register1(Location):
    def init(self):
        self.name = 'Регистрация' 
        self.attachment = ''
    
    def msg(self):
        return 'Отправьте желаемое имя...'

    def not_func(self, word):
        self.player.set_name(word)
        self.player.set_location('Crossroad')
    
    