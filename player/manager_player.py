from player.player import Player

class ManagerPlayer:
    def __init__(self, parent, bd = None):
        self.parent = parent
        self.bd = bd if parent == None else self.parent.bd
        self.__players = dict()
        self.__index_user_id = -1

    @property
    def player(self):
        return self.__players.get(self.__index_user_id)

    @property
    def user_id(self):
        return self.player.user_id
    
    @property
    def battle_id(self):
        return self.player.battle_id

    def new_player(self, user_id):
        p = Player(self.parent, user_id)
        self.__players.update({user_id:p})
        return p

    def select_player(self, user_id):
        self.__index_user_id = user_id
        if self.player == None: self.new_player(user_id)

    def update_player(self):
        self.player.update_player()


