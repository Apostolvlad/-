from location.location import LocationLocations
class Hero(LocationLocations):
    def init(self):
        self.name = 'Зеркало'
        self.attachment = 'photo-179475703_457239040'
        self.add_button(0, 'Обратно', self.back, 'negative')
        self.msgs = (
                    'Ну ничего так, хорош, определённо хорош.',
                    'Ну и что, что немного грязный, какая кому разница??',
                    'Хмм, может подкачаться? Да не, бред какой - то...',
                    'Если долго смотреть в бездну, то бездна начнёт смотреть в тебя, поэтому я лучше пойду отсюда...'
                    )

    # send_msg должен быть вне класса!!!!, в manager_loc, ибо, кнопки текущей локации, могут менять саму локацию!!!!, а значит и keyboard сменится.
    def back(self, word):
        self.player.set_location('House') #self.parent.api.send_msg(self.parent.info_user.name, self.parent.info_user.user_id, self.keyboard)


