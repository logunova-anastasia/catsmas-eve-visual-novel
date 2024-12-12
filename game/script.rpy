# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
init python:
    import markovchain

    text = open(renpy.loader.transfn('shakespeare.txt'))

    text_model = markovchain.Markov(text)

    like = 0

define e = Character('Кошко', color="#57100e", image='orange_cat')

image side cat = 'images/orange_cat.png'  

define m = Character('Безумная мышьо', color="#57100e", image='rat')

image side rat = 'images/rat.png'  

define gui.text_size = 40

define gui.name_text_size = 60

default gifts = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

label Msay: # Make NPC say something.
    $ mString = text_model.generate_markov_text(4)
    m "%(mString)s"
    return

label MenuTwo: #two menu choices
    $ mStringA = text_model.generate_markov_text(5)
    menu:
        "%(mStringA)s":
            $ choice = 1
            $ like += 1
            return
        "Э-э, наверное?...":
            $ choice = 2
            return

# Игра начинается здесь:
label start:

    scene aiiii:
        size(1920, 1080)

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

    jump first_mouse

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
            e 'Бабушкины кактусы. Красивые, но кусать их не стоит..'
            jump kitchen_wrong

    return

label kitchen_end:
    scene kitchen:
        size(1920, 1080)

    if gift_kitchen == True:
        e 'Подарок найден с первой попытки!'
        $ gifts = gifts + 1
    
    jump first_mouse

    return

label first_mouse:
    scene kitchen:
        size(1920, 1080)

    m 'uiuheirh'
    
    call Msay

    call MenuTwo

    return