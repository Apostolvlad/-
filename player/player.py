class Player:
    param = ('name', 'location', 'class_hero', 'battle_id')
    z_select = ','.join(param)
    z_update = ' = ?,'.join(param) + ' = ?'
    def __init__(self, parent, user_id, bd = None):
        self.parent = parent
        self.bd = bd if parent == None else self.parent.bd
        self.user_id = user_id
        self.param = dict()
        self.check_player()

    def create_player(self):
        self.bd.insert('players', '(user_id)', '(?)', (self.user_id,))
    
    def select_player(self):
        result = self.bd.select('players', Player.z_select, 'user_id = ?', (self.user_id,))
        if result == None: return False
        self.param = {name:element for name, element in zip(Player.param, result)}
        return True

    def update_player(self):
        self.bd.update('players', Player.z_update, f'user_id = {self.user_id}', tuple(self.param.values()))
        
    def del_player(self):
        self.bd.del_str('players', 'user_id = ?', (self.user_id,))

    def check_player(self):
        if self.select_player() == False:
            self.create_player()
            self.select_player()
    
    @property
    def location(self):
        return self.param.get('location')

    def set_location(self, location):
        return self.param.update({'location': location})

    @property
    def name(self):
        return self.param.get('name')

    def set_name(self, name):
        return self.param.update({'name': name})

    @property
    def class_hero(self):
        return self.param.get('class_hero')

    def set_class_hero(self, class_hero):
        return self.param.update({'class_hero': class_hero})
    
    @property
    def battle_id(self):
        return self.param.get('battle_id')

    def set_battle_id(self, battle_id):
        return self.param.update({'battle_id': battle_id})
