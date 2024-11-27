# Вы можете расположить сценарий своей игры в этом файле.
# # Определение персонажей игры.
define g = Character('Мустанг', color="#57100e")
define o = Character('Оливер', color="#57100e")
define w = Character('Мура', color="#57100e")


define gui.text_font = "KoskoRegular-Regular.ttf"

default current_screen = 0

screen screen_1():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/orange_cat.png"
    imagebutton:
        xalign 0.05 yalign 0.05
        idle "gui/button/combo_button.png"
        action SetVariable("current_screen", (current_screen + 1) % 3)

screen screen_2():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/grey_cat.png"
    imagebutton:
        xalign 0.05 yalign 0.05
        idle "gui/button/combo_button.png"
        action SetVariable("current_screen", (current_screen + 1) % 3)

screen screen_3():
    add "D:/RENPY/Christmas_cat_project/christmas-cat/game/images/white_cat.png"
    imagebutton:
        xalign 0.05 yalign 0.05
        idle "gui/button/combo_button.png"
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


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


# Игра начинается здесь:
# label start:
label start:
    # Показать главный экран
    show screen background
    o "Вы...наверное, хотите узнать моё имя? Тогда, послушайте... Я Оливер. Хотите знать, о чём я думаю? Я... думаю о еде, тепле и о подарках."
    g "Привет! Меня зовут Мустанг!"
    w "Привет! Меня зовут Мура!"




    return





