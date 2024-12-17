# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
init python:
    import markovchain

    text = open(renpy.loader.transfn('shakespeare.txt'))

    text_model = markovchain.Markov(text)

    like = 0

init python:
    onn = ImageDissolve("eye.png", 2.0, 20, reverse=False) 
    off = ImageDissolve("eye.png", 2.0, 20, reverse=True)

define cat_1 = Character("Барсик")
define cat_2 = Character("Вася")
define cat_3 = Character("Яшка")

define chosen_orange_cat = Character("Барсик", image='chosen_orange_cat')
define chosen_grey_cat = Character("Вася", image='chosen_grey_cat')
define chosen_white_cat = Character("Яшка", image='chosen_white_cat')

define rat = Character('Безумная мышь', image='rat')
image side rat = "images/rat.png"

define son = Character('Кирилл', image='son')
image side son = "images/son.png"

define mom = Character('Екатерина', image='mom')
image side mom = "images/mom.png"

define daughter = Character('Надя', image='daughter')
image side daughter = "images/daughter.png"

define dad = Character('Владимир', image='dad')
image side dad = "images/dad.png"

define grandma = Character('Хозяйка', image='grandma')
image side grandma = "images/grandma.png"

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
        xalign 0.65 yalign 0.34
        idle Transform("gui/button/pngwing.com.png", size=(343, 167))
        action [Hide("background"), Jump('morning')]

label Msay: # Make NPC say something.
    $ mString = text_model.generate_markov_text(4)
    rat "%(mString)s"
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

    current_character "Зимнее утро пробивалось сквозь зашторенное окно."
    current_character "Морозные узоры и искрящийся от света снег выглядели завораживающе, почти волшебно."
    current_character "Я смотрел на эту игру лучей прищуренными от сна глазами, ожидая пробуждения остальных жителей дома."
    current_character "Хотелось завтракать, но я люблю есть в компании с кем-то, в конце концов, кто знает, может мне перепадет что-то вкусное со стола."
    current_character "Сегодня же был необычный день - канун Рождества."
    current_character "Люди покупают вещи, которые хотят другие люди, заворачивают в шуршащие бумаги и ленты."
    current_character "На следующий день разворачивают их обратно и очень громко общаются."
    current_character "Потом они все садятся за стол и едят вкусную еду. "
    current_character "В такое время хозяйка даже не ругается на дочь и внуков, когда те дают мне кусочки мяса из своих тарелок."
    current_character "Со второго этажа донеслись скрипы матраса и шлепки шагов. Это встали внуки хозяйки. Кажется, те никогда не оставляли меня в покое."

    son "[current_character], иди сюда! Доброе утро!"
    current_character "О чем и речь. Старший спустился первым и тут же подошел ко мне. Я бы предпочел, чтобы меня вообще не трогали, но уж лучше он, чем его сестра."
    current_character "Хотя бы почесывания за ухом были приятными."
    current_character "Когда мне надоело, я вывернулся, спрыгнул с кресла и пошел на кухню. К счастью, наш парень был из понятливых - миска оказалась полной быстро."
    current_character "На втором этаже снова заскрипели кровать - это встали хозяйка с дочерью. К моменту, когда я закончил с едой, все жители дома были либо в гостиной, либо на кухне."
    current_character "Я забрался на полку повыше, чтобы внучка хозяйки, Надя, не могла дотянуться до меня и наблюдал за утренней возней."
    current_character "Говорливая девчонка обсуждала подарки и все пыталась узнать, где они хранятся и что из себя представляют. Старшие старались держаться под её натиском."

    $ renpy.notify("Обращайте внимание на выделенные реплики в речи героев. Возможно, они будут полезны вам позже…")

    mom "Ты ведь ничего не расскажешь бабушке?"
    current_character "Девочка активно затрясла головой из стороны в сторону. Я тоже прислушался."
    current_character "Может, я не дарил и не получал подарки, но интерес это не уменьшало."
    mom "Я спрятала кое-что {b}в тумбе у холодильника.{/b} Только это наш секрет, хорошо?"

    current_character "Глаза девочки заблестели. В этот момент во входной двери звякнул ключ и кто-то вошел в дом."
    current_character "Ошибки быть не могло - это был Владимир, муж хозяйкиной дочери."
    current_character "Я спустился с полки, чтобы успеть заглянуть в шуршащие пакеты, но тут же оказался в руках Нади."
    current_character "Несмотря на возраст, из её хватки было труднее всего вырваться. Оставалось принять неизбежное и надеяться, что меня быстро отпустят."

    daughter "Ты же тоже слышал мамин секрет? Подслушивать - нечестно!"
    current_character "Девочка развернулась в сторону коридора, где сейчас говорили её родители, а потом наклонилась близко к моему уху."
    daughter "Чтобы не обижать маму, я тебе тоже скажу свой секрет: я видела, как Киря {b}что-то сложил под кровать{/b}, когда думал, что я уснула."
    current_character "Меня, наконец, отпустили, и я решил найти место поукромнее."
    current_character "Несмотря на интересные запахи из коридора, я не был готов к очередным попыткам привести себя в порядок после чужих прикосновений."
    current_character "На втором этаже дверь хозяйки оказалась открытой."
    current_character "Устроившись у неё в кресле, я задремал."
    
    scene black with off 
    pause 1.0
    scene living-room with onn

    current_character "Проснувшись, я не заметил никого в комнате и решил спуститься на первый этаж."
    current_character "Уже на верхней ступени я услышал, как разговаривают на повышенных тонах."
    mom "Я же три раза просила тебя добавить их в список! Сейчас уже нет времени искать по магазинам, как я должна готовить этот салат?!"
    current_character "Кажется, кто-то попал под горячую руку."
    current_character "Каждый год Катерина старается устроить идеальный праздник."
    current_character "Это нервирует и её, и всех в доме."

    dad "Мы вместе составляли список покупок! Все были довольны, откуда тут могли взяться те специи и овощи, которые тебе нужны сейчас?!"
    mom "Я каждый год готовлю эти блюда, я же не могла забыть, что мне нужно!"
    grandma "..."
    current_character "Хозяйка грустно смотрела на спорщиков, но ничего не говорила."
    current_character "Тут со второго этажа раздался еще один крик."
    current_character "Послышался топот и вниз с шумом сбежали Надя и Кирилл."
    daughter "Мам, пап, он меня обижает!"
    current_character "Мда. Эти слезливые глаза разжалобили бы кого угодно, кроме этой семейки."
    current_character "Брат с сестрой часто ссорятся и иногда обвинения с её стороны доходят до абсурдного."
    current_character "Сейчас же для этого было не лучшее время."
    mom "Ну что опять у вас случилось?!"
    son "Она снова лезла в мои вещи!"
    daughter "А он забрал мой дневник!"

    mom "Всем нужно разругаться накануне праздника! Решайте все сами!"
    current_character "Полотенце, которое до этого было у неё в руках, улетело на столешницу."
    current_character "Я инстинктивно прижался к стене, когда она пронеслась мимо на второй этаж."
    current_character "Отец семейства растерянно посмотрел ей вслед, но уже более собранно повернулся к остальным."
    dad "Надя, нельзя в чужие вещи лезть без спроса. Кирилл, верни сестре дневник."
    dad "Елена Викторовна, Вы извините, что так вышло…"
    grandma "Дело житейское, Володь, но вы уж полегче друг с другом."
    current_character "Владимир кивнул и, грозно посмотрев на детей, пошел наверх."
    current_character "Дети же обменялись грозными взглядами."
    son "Я пойду пройдусь, бабуль."
    daughter "Верни мой дневник!"
    son "Да сдался он мне! Посмотри в своем бардаке!"

    current_character "Хозяйка охнула и пошла за внуком в прихожую, а младшая, громко топая и вытирая слезы, убежала наверх."
    current_character "В этой семейке сейчас и сами перессорятся, и хозяйку расстроят. А если ей плохо станет?"
    current_character "Как их помирить?"
    current_character "Я осмотрелся вокруг и невольно засмотрелся на мигающую гирлянду на елке."
    current_character "Точно! Елка и подарки!"
    current_character "Когда они соберутся рядом с елкой и увидят подарки, которые сами туда не клали, они обрадуются."
    current_character "Я сделаю им новогоднее чудо и попробую им помочь!"





label kitchen:
    scene kitchen:
        size(1920, 1080)

    menu:
        'Посмотреть под столом':
            scene pots
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
            scene pots
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

