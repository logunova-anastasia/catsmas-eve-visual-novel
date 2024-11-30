# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define e = Character('Кошко', color="#57100e", image='cat')
define cat_1 = Character("Барсик")
define cat_2 = Character("Вася")
define cat_3 = Character("Яшка")


define gui.text_font = "minecraft.ttf"
image side cat = 'images/orange_cat.png'


define gui.text_size = 40
define gui.name_text_size = 60


default gifts = 0
default current_screen = 0
default selected_character = None


screen screen_1():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/orange_cat.png" xalign 0.7 yalign -0.7
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/dialogue_window.png" xalign 0.3 yalign -0.2
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_2():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/grey_cat.png" xalign 0.75 yalign -5.0
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/dialogue_window.png" xalign 0.3 yalign -0.2
    text "Привет, Я Барсик!" xalign 0.3 yalign -0.2 size 30 color "#57100e"
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_3():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/white_cat.png" xalign 0.7 yalign -5.0
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/dialogue_window.png" xalign 0.3 yalign -0.2
    text ' 54323456789'
    imagebutton:
        xalign 1.0 yalign 1.0
        idle Transform("gui/button/combo_button.png", size=(300, 300))
        action SetVariable("current_screen", (current_screen + 1) % 3)


# Главный экран, который показывает текущий экран
screen background():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/aiiii.png" xsize 1920 ysize 1080
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


label kitchen:
    hide screen next_button
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
            e 'Бабушкины кактусы. Красивые, но кусать их не стоит..'
            jump kitchen_wrong

    return

label kitchen_end:
    scene kitchen:
        size(1920, 1080)
    
    if gift_kitchen == True:
        e 'Подарок найден с первой попытки!'
        $ gifts = gifts + 1

    return