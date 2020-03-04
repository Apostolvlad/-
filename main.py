from bot import Bot
from location.locations import *# manager_location

def main():
    #Location() # прописывать все импортируемые в папках локациях, либо так..., ибо он её цыпляет из них, и выдает предупреждение.. раздражает
    g = Bot('', '') # токен группы для работы с сообщениями, и ид группы.

    Register(g)
    Register1(g)
    Crossroad(g)
    House(g)
    Hero(g)
    
    g.run()




if __name__ == "__main__":
    main()
    
