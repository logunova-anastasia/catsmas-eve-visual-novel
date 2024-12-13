# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
init python:
    import markovchain

    text = open(renpy.loader.transfn('shakespeare.txt'))

    text_model = markovchain.Markov(text)

    like = 0

define cat_1 = Character("Барсик")
define cat_2 = Character("Вася")
define cat_3 = Character("Яшка")

define chosen_orange_cat = Character("Барсик", image='chosen_orange_cat')
define chosen_grey_cat = Character("Вася", image='chosen_grey_cat')
define chosen_white_cat = Character("Яшка", image='chosen_white_cat')

define m = Character('Безумная мышь', color="#57100e", image='rat')
image side rat = "images/rat.png"

define gui.text_font = "minecraft.ttf"
image side chosen_orange_cat = "images/orange_cat.png"
image side chosen_grey_cat = "images/grey_cat.png"
image side chosen_white_cat = "images/white_cat.png"

default current_image = None

define gui.text_size = 40
define gui.name_text_size = 60


default gifts = 0
default current_screen = 0
default selected_character = None

define audio.morning = "audio/morning.mp3"


screen screen_1():
    add "orange_cat.png" xalign 0.7 yalign -0.7
    add "dialogue_window.png" xalign 0.3 yalign -0.2
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_2():
    add "grey_cat.png" xalign 0.75 yalign -5.0
    add "dialogue_window.png" xalign 0.3 yalign -0.2
    text "Привет, Я Барсик!" xalign 0.3 yalign -0.2 size 30 color "#57100e"
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_3():
    add "white_cat.png" xalign 0.7 yalign -5.0
    add "dialogue_window.png" xalign 0.3 yalign -0.2
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


# Главный экран, который показывает текущий экран
screen background():
    add "aiiii.png" xsize 1920 ysize 1080
    if current_screen == 0:
        use screen_1()
    elif current_screen == 1:
        use screen_2()
    elif current_screen == 2:
        use screen_3()

screen next_button():
    imagebutton:
        xalign 0.9 yalign 0.1
        idle Transform("gui/button/pngwing.com.png", size=(300, 300))
        action [Hide("background"), Jump('kitchen')]

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

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.



# Игра начинается здесь:
label start:
    show screen background
    # Показать главный экран
    scene aiiii:
        size(1920, 1080)

    $ changed_buttons = 1 #эта переменная позволяет применить индивид. стиль к кнопкам выбора.
    # если нужен стандарт, то пишем $ changed_buttons = 0
    menu:
        "Котик Барсик":
            $ selected_character = cat_1

        "Котик Вася":
            $ selected_character = cat_2

        "Котик Яшка":
            $ selected_character = cat_3

    hide screen background
    show screen next_button

    if selected_character == cat_1:
        show orange_cat:
            xalign 0.05 yalign 0.1
        cat_1 "Слова Барсика"
    elif selected_character == cat_2:
        show grey_cat:
            xalign 0.1 yalign 0.3
        cat_2 "Слова Васи"
    elif selected_character == cat_3:
        show white_cat:
            xalign 0.1 yalign 0.3
        cat_3 "Слова Яшки"

label morning:
    play audio morning
    hide screen next_button
    scene living-room:
        size(1920, 1080)

    if selected_character == cat_1:
        $ current_character = chosen_orange_cat
    elif selected_character == cat_2:
        $ current_character = chosen_grey_cat
    elif selected_character == cat_3:
        $ current_character = chosen_white_cat

    current_character "Зимнее утро пробивалось сквозь зашторенное окно. Морозные узоры и искрящийся от света снег выглядели завораживающе, почти волшебно."
    current_character "Я смотрел на эту игру лучей прищуренными от сна глазами, ожидая пробуждения остальных жителей дома."
    current_character "Хотелось завтракать, но я люблю есть в компании с кем-то, в конце концов, кто знает, может мне перепадет что-то вкусное со стола."
    current_character "Сегодня же был необычный день - канун Рождества."
    current_character "Люди покупают вещи, которые хотят другие люди, заворачивают в шуршащие бумаги и ленты, а на следующий день разворачивают их обратно и очень громко общаются."
    current_character "Потом они все садятся за стол и едят вкусную еду. "
    current_character "В такое время хозяйка даже не ругается на дочь и внуков, когда те дают мне кусочки мяса из своих тарелок."
    current_character "Со второго этажа донеслись скрипы матраса и шлепки шагов. Это встали внуки хозяйки. Кажется, те никогда не оставляли меня в покое."

label kitchen:
    scene kitchen:
        size(1920, 1080)

    menu:
        'Посмотреть под столом':
            current_character "Ура! Кастрюльки для бабушки, первый подарок найден!"
            $ gift_kitchen = True
            jump kitchen_end
        'Посмотреть на камоде':
            current_character "Салаты... Вкусно, но на подарок не пойдет"
            $ gift_kitchen = False
            jump kitchen_wrong
        'Посмотреть на подоконнике':
            current_character "Бабушкины кактусы. Красивые, но кусать их не стоит. Знаю не понаслышке"
            $ gift_kitchen = False
            jump kitchen_wrong
    return

label kitchen_wrong:
    scene kitchen:
        size(1920, 1080)
    
    menu:
        'Посмотреть под столом':
            current_character 'Ура! Кастрюльки для бабушки, первый подарок найден!'
            jump kitchen_end
        'Посмотреть на камоде':
            current_character 'Салаты... Вкусно, но на подарок не пойдет'
            jump kitchen_wrong
        'Посмотреть на подоконнике':
            current_character 'Бабушкины кактусы. Красивые, но кусать их не стоит..'
            jump kitchen_wrong

    return

label kitchen_end:
    scene kitchen:
        size(1920, 1080)
    
    if gift_kitchen == True:
        current_character 'Подарок найден с первой попытки!'
        $ gifts = gifts + 1

    jump first_mouse

    return

label first_mouse:
    scene kitchen:
        size(1920, 1080)
    
    call Msay

    call MenuTwo

    return

