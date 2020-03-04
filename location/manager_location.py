from .location import Location
class ManagerLocation:
    def __init__(self, parent):
        self.parent = parent

        self.__locations = dict()

    @property
    def player(self):
        return self.parent.manager_player.player

    @property
    def location(self):
        return self.__locations.get(self.player.location, self.__locations['Crossroad'])

    @property
    def keyboard(self):
        return self.location.keyboard 
    
    @property
    def attachment(self):
        return self.location.attachment 

    def add(self, name, location):
        self.__locations.update({name:location})

    def process_word(self, word):
        location_back = self.player.location
        self.location.process_word(word)
        save = None
        while save != self.location:
            save = self.location
            self.location.check_access(location_back)
        return self.location.msg()# if status == True else text 

