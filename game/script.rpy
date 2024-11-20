# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define g = Character('Мустанг', color="#57100e")
define o = Character('Оливер', color="#57100e")
define w = Character('Мура', color="#57100e")

define gui.text_font = "KoskoRegular-Regular.ttf"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene aiiii: # для создания следующей страницы в игре просто копируем код выи вставляем в нужном порядке
        size(1920, 1080)

    show orange_cat:
        xalign -0.2 yalign -0.1

    o "Вы...наверное, хотите узнать моё имя? Тогда, послушайте... Я Оливер. Хотите знать, о чём я думаю? Я... думаю о еде, тепле и о подарках."

    scene aiiii:
        size(1920, 1080)

    show grey_cat:
        xalign -0.1 yalign -0.3

    g "Привет! Меня зовут Мустанг!"

    scene aiiii:
        size(1920, 1080)

    show white_cat:
        xalign -0.1 yalign -0.3

    w "Привет! Меня зовут Мура!"


    return
