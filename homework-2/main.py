from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.ch_name)  # MoscowPython
    print(moscowpython.ch_vives_amount)  # 685 (может уже больше)
    print(moscowpython.ch_url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')
