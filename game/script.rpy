# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Кошко', color="#57100e")

define gui.text_font = "Bimbo-Regular.ttf"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene aiiii:
        size(1920, 1080)

    show kitty:
        xalign -0.1 yalign -0.3

    e "Я кот, всех с новай годай"

    return
