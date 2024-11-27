# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Кошко', color="#57100e")

define gui.text_font = "MADE TheArtist Sans PERSONAL USE.otf"

define gui.text_size = 50

define gui.name_text_size = 60

default gifts = 0

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

    show kitty:
        xalign -0.1 yalign -0.3

    e "Я кот, всех с новай годай"

    jump kitchen

    return


label kitchen:
    scene kitchen:
        size(1920, 1080)
    
    menu:
        'Посмотреть под столом':
            e 'Ура! Кастрюльки для бабушки, первый подарок найден!'
            $ gift_kitchen = True
            jump kitchen_end
        'Посмотреть на камоде':
            e 'Салаты... Вкусно, но на подарок не пойдет'
            $ gift_kitchen = False
            jump kitchen_wrong
        'Посмотреть на подоконнике':
            e 'Бабушкины кактусы. Красивые, но кусать их не стоит. Знаю не понаслышке'
            $ gift_kitchen = False
            jump kitchen_wrong

    return

label kitchen_wrong:
    scene kitchen:
        size(1920, 1080)
    
    menu:
        'Посмотреть под столом':
            e 'Ура! Кастрюльки для бабушки, первый подарок найден!'
            jump kitchen_end
        'Посмотреть на камоде':
            e 'Салаты... Вкусно, но на подарок не пойдет'
            jump kitchen_wrong
        'Посмотреть на подоконнике':
            e 'Бабушкины кактусы. Красивые, но кусать их не стоит. Знаю не понаслышке'
            jump kitchen_wrong

    return

label kitchen_end:
    scene kitchen:
        size(1920, 1080)
    
    if gift_kitchen == True:
        e 'Подарок найден с первой попытки!'
        $ gifts = gifts + 1

    return