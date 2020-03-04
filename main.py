from bot import Bot
from location.locations import *# manager_location

def main():
    #Location() # прописывать все импортируемые в папках локациях, либо так..., ибо он её цыпляет из них, и выдает предупреждение.. раздражает
    g = Bot('18dc699f66a4d77a5185ea1a474c458c5a8407fcbebc47c90f3ce1139e299aa03042acc56d43e1eb7290e', '179475703')

    Register(g)
    Register1(g)
    Crossroad(g)
    House(g)
    Hero(g)
    
    g.run()




if __name__ == "__main__":
    main()
    