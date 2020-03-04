def test_player():
    from bd.bd_connect import Bd
    bd = Bd()
    from player.player import Player
    p = Player(bd, 9999)
    p.set_name('TEST')
    p.set_class_hero('class_test1')
    p.set_batle_id(9999)
    p.set_location('test_location')
    p.update_player()
    bd.commit()
    print(p.user_id)
    print(p.name)
    print(p.class_hero)
    print(p.batle_id)
    print(p.location)
    p = None
    p = Player(bd, 9999)
    print(p.user_id)
    print(p.name)
    print(p.class_hero)
    print(p.batle_id)
    print(p.location)
    p.del_player()
    bd.commit()
    
















if __name__ == "__main__":
    test_player()