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

define cat_1 = Character("Оскар")
define cat_2 = Character("Том")
define cat_3 = Character("Марс")

define chosen_orange_cat = Character("Оскар", image='chosen_orange_cat')
define chosen_grey_cat = Character("Том", image='chosen_grey_cat')
define chosen_white_cat = Character("Марс", image='chosen_white_cat')

define rat = Character('Безумная мышь Стивен', image='rat')
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

define author = Character('')

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

define audio.morning = "music/morning.mp3"
define audio.sad = "music/sad.mp3"
define audio.search = "music/search.mp3"
define audio.happy = "music/happy.mp3"

screen screen_1():
    add "orange_cat.png" xalign 0.7 yalign -0.7
    add "oscar_bubble.png" xalign 0.63 yalign 0.1
    imagebutton:
        xalign 1.0 yalign 0.9
        idle Transform("gui/button/combo_button.png")
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_2():
    add "grey_cat.png" xalign 0.75 yalign -5.0
    add "tom_bubble.png" xalign 0.69 yalign 0.1
    imagebutton:
        xalign 1.0 yalign 0.9
        idle Transform("gui/button/combo_button.png")
        action SetVariable("current_screen", (current_screen + 1) % 3)


screen screen_3():
    add "white_cat.png" xalign 0.7 yalign -5.0
    add "mars_bubble.png" xalign 0.65 yalign 0.1
    imagebutton:
        xalign 1.0 yalign 0.9
        idle Transform("gui/button/combo_button.png")
        action SetVariable("current_screen", (current_screen + 1) % 3)


# Главный экран, который показывает текущий экран
screen background():
    add "opening.png" xsize 1920 ysize 1080
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
    scene opening
    play music search
    author "Ваша история скоро начнется. Для начала выберите персонажа."
    show screen background
    # Показать главный экран

    $ changed_buttons = 1 #эта переменная позволяет применить индивид. стиль к кнопкам выбора.
    # если нужен стандарт, то пишем $ changed_buttons = 0
    menu:
        "Котик Оскар":
            $ selected_character = cat_1

        "Котик Том":
            $ selected_character = cat_2

        "Котик Марс":
            $ selected_character = cat_3

    hide screen background
    show screen next_button

    if selected_character == cat_1:
        show orange_cat:
            xalign 0.05 yalign 0.1
        cat_1 "Привет, я Оскар!"
    elif selected_character == cat_2:
        show grey_cat:
            xalign 0.1 yalign 0.3
        cat_2 "Привет, я Том!"
    elif selected_character == cat_3:
        show white_cat:
            xalign 0.1 yalign 0.3
        cat_3 "Привет, я Марс!"

label morning:
    stop music fadeout 1
    play music morning
    hide screen next_button
    scene living-room

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
    current_character "На втором этаже снова заскрипели кровати - это встали хозяйка с дочерью. К моменту, когда я закончил с едой, все жители дома были либо в гостиной, либо на кухне."
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

    stop music fadeout 1
    play music sad

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

    scene black with off 
    pause 1.0
    scene living-room with onn

    stop music fadeout 1
    play music search

    current_character "Начинать надо прямо сейчас."
    current_character "До вечера осталось совсем мало времени."
    current_character "Я решил начать с кухни: дочь хозяйки как раз дала подсказку, где искать. Спрыгнув со ступеней на пол, я забежал на кухню."


label kitchen:
    scene kitchen

    current_character "Со столешницы ориентироваться будет явно проще."
    current_character "Запрыгнув и обойдя разложенные на поверхности продукты, я осмотрелся."
    current_character "Надо быть внимательным, но быстрым: кто угодно может зайти, если я не угадаю и потеряю время."
    current_character "Где искать подарок?"

    menu:
        'Шкафчик над плитой':
            current_character "Я попытался открыть дверцу, но оттуда на меня чуть не рассыпалась паста."
            current_character "Попытавшись увернуться, я чуть не обжегся об остывающую плиту."
            grandma "[current_character], а ты куда залез? Слезай отсюда, негодник!"
            current_character "В дверном проеме стояла хозяйка и грозно смотрела на меня."
            current_character "Пока я пытался сориентироваться, она подошла и спустила меня на пол."
            grandma "Иди погуляй в другом месте, сюда котику нельзя!"
            current_character "Мне не оставалось ничего, кроме как отправиться дальше."
            $ gift_kitchen = False
            jump kitchen_wrong
        'Тумба около холодильника':
            current_character "По началу дверь не поддалась, но в итоге я смог приоткрыть её так, чтобы суметь пролезть."
            current_character "Многочисленные формы для тортов и кексов были знакомы за годы жизни с хозяйкой."
            current_character "Я хотел было вылезти, но тут в дальнем углу блеснула ручка кастрюли."
            current_character "Такого тут не должно было быть, кастрюли стояли на другой полке."
            current_character "Вспомнилось, что хозяйку отчаянно не пускали к готовке под предлогом помощи."
            current_character "Я протиснулся поближе и увидел набор новых кастрюль."
            scene pots
            current_character "Вот оно! Первый подарок нашелся! Хозяйка будет довольна."
            $ renpy.notify("Вы нашли первый подарок!")
            $ gift_kitchen = True
            jump kitchen_end
        'Тумба под раковиной':
            current_character "Вдруг я услышал приближающиеся голоса хозяйки и её внука."
            current_character "Я не успел убрать хвост и меня заметили."
            grandma "[current_character], а ты куда залез? Выходи отсюда, негодник!"
            current_character "Дверца тумбы полностью открылась, и хозяйка грозно заглянула внутрь."
            current_character "Я не успел выскочить, как меня вытащили наружу и поставили на пол."
            grandma "Иди погуляй в другом месте, сюда котику нельзя!"
            current_character "Мне не оставалось ничего, кроме как отправиться дальше."
            $ gift_kitchen = False
            jump kitchen_wrong
            
label kitchen_wrong:
    scene kitchen
    menu:
        'Шкафчик над плитой':
            current_character "Я попытался открыть дверцу, но оттуда на меня чуть не рассыпалась паста."
            current_character "Попытавшись увернуться, я чуть не обжегся об остывающую плиту."
            grandma "[current_character], а ты куда залез? Слезай отсюда, негодник!"
            current_character "В дверном проеме стояла хозяйка и грозно смотрела на меня."
            current_character "Пока я пытался сориентироваться, она подошла и спустила меня на пол."
            grandma "Иди погуляй в другом месте, сюда котику нельзя!"
            current_character "Мне не оставалось ничего, кроме как выйти из кухни и дождаться, пока хозяйка выйдет."
            current_character "Как только она снова скрылась в коридоре, я вернулся на кухню."
            jump kitchen_wrong
        'Тумба около холодильника':
            current_character "По началу дверь не поддалась, но в итоге я смог приоткрыть её так, чтобы суметь пролезть."
            current_character "Многочисленные формы для тортов и кексов были знакомы за годы жизни с хозяйкой."
            current_character "Я хотел было вылезти, но тут в дальнем углу блеснула ручка кастрюли."
            current_character "Такого тут не должно было быть, кастрюли стояли на другой полке."
            current_character "Вспомнилось, что хозяйку отчаянно не пускали к готовке под предлогом помощи."
            current_character "Я протиснулся поближе и увидел набор новых кастрюль."
            scene pots
            current_character "Вот оно! Первый подарок нашелся! Хозяйка будет довольна."
            current_character "В этот момент я почувствовал, как меня подняли руки хозяйки."
            current_character "Я мявкнул от неожиданности и оказался за порогом кухни."
            grandma "Ну какой неугомонный кот! Иди, [current_character]!"
            $ renpy.notify("Упс! Вы не успели забрать подарок!")

            jump kitchen_end
        'Тумба под раковиной':
            current_character "Вдруг я услышал приближающиеся голоса хозяйки и её внука."
            current_character "Я не успел убрать хвост и меня заметили."
            grandma "[current_character], а ты куда залез? Выходи отсюда, негодник!"
            current_character "Дверца тумбы полностью открылась, и хозяйка грозно заглянула внутрь."
            current_character "Я не успел выскочить, как меня вытащили наружу и поставили на пол."
            grandma "Иди погуляй в другом месте, сюда котику нельзя!"
            current_character "Мне не оставалось ничего, кроме как выйти из кухни и дождаться, пока хозяйка выйдет."
            current_character "Как только она снова скрылась в коридоре, я вернулся на кухню."
            jump kitchen_wrong

label kitchen_end:
    scene kitchen
    
    if gift_kitchen == True:
        $ gifts = gifts + 1

    current_character "После кухни я направился на второй этаж."
    current_character "Вдруг слева сверху что-то звякнуло."
    current_character "Я чуть было не подскочил, но все же решил проверить."
    current_character "Это был телефон хозяйки."
    current_character "На экране светилось новое сообщение: “В прошлый раз оставила его {b}в шкафу у входа{/b}”."
    current_character "Кажется, это был кто-то из ее подруг."
    current_character "Но пока я должен был добраться до детской."


label second_floor:
    scene hallway
    
    current_character "Я помнил секрет, которым поделилась Надя."
    current_character "Детская находилась в самом конце коридора, рядом с лестницей на чердак."
    current_character "По пути я невольно услышал тихие переговоры Катерины и Владимира."

    scene bedroom
    dad 'Мы хорошо отпразднуем и без этого салата.'
    dad 'А завтра я съезжу за продуктами и мы вместе сделаем этот салат.'
    mom "Я знаю, но мы каждый год его делаем! Это такая семейная традиция!..."

    scene hallway
    current_character "Я оставил их разбираться со своей ссорой и пошел дальше."
    current_character "Почему-то у Катерины был пунктик насчет традиций, которые ежегодно становились камнем преткновения в праздники."
    current_character "Вдруг из-за угла, ведущего в конец коридора, послышался писк."
    current_character "Я резко обернулся."
    current_character "Мышей у нас давно не заводилось, они знали, что тут живу я."
    current_character "Я подкрался и заглянул за угол."
    current_character "Там сидела и умывалась серая мышь."
    current_character "Она не выглядела обеспокоенной моим запахом по всему дому."
    current_character "Она даже не замечала моего присутствия, как сделал бы любой приличный грызун."
    current_character "Ну здравствуй, мышка."
    current_character "Я хотел припугнуть обнаглевшего гостя и немного оскалился."
    current_character "Мышь оглянулась на меня, но не выглядела даже взволнованной."

label first_mouse:
    scene hallway
    call Msay
    $ renpy.notify("Мышь запомнит ваш ответ!")
    call MenuTwo
    
label children:
    current_character "Мышь повернула голову на бок, но больше никак не отреагировала."
    current_character "После этого она и вовсе отвернулась и убежала в неприметную дырку в плинтусе, которую я до этого не замечал."

    scene children
    current_character "…В детской оказалась Надя, которая очень усердно что-то рисовала, сидя на кровати."
    current_character "Ее увлеченность дала мне немного времени."
    current_character "Я забрался на стул и осмотрелся."
    current_character "Надо быть внимательным, но быстрым: кто угодно может зайти, если я не угадаю и потеряю время."
    current_character "Где искать подарок?"
    menu:
        'На письменном столе':
            current_character "Я соскочил со стула и добежал до стола."
            current_character "Запрыгнув и оглядевшись, я не заметил ничего примечательного."
            current_character "В этот момент Надя обернулась ко мне. "
            current_character "Видимо, я не успел избежать ее внимания."
            current_character "Цепкие детские ручки обвились вокруг тела и понесли меня в сторону кровати."
            current_character "Пришлось смириться со своим положением пленника."
            current_character "Через некоторое время я выбрался и вернулся к изучению комнаты с высоты стула."

            $ gift_children = False
            jump children_wrong
        'В шкафу с одеждой':
            current_character "Я соскочил со стула и добежал до шкафа."
            current_character "Я заскочил на полку благодаря приоткрытой дверце. "
            current_character "В темноте и бардаке ничего не было видно."
            current_character "В этот момент Надя вытащила меня обратно."
            current_character "Видимо, я не успел избежать ее внимания."
            current_character "Цепкие детские ручки обвились вокруг тела и понесли меня в сторону кровати."
            current_character "Через некоторое время я выбрался и вернулся к изучению комнаты с высоты стула."

            $ gift_children = False
            jump children_wrong
        'Под кроватью':
            current_character "Я соскочил со стула и добежал до кровати."
            scene thermos-and-hat
            $ renpy.notify("Вы нашли второй подарок!")
            current_character 'Подарок найден с первой попытки!'
            current_character "Вот и второй подарок! Это, должно быть, для Владимира."
            current_character "Надеюсь, ему понравится."
            scene children
            current_character "Я вылез из-под кровати Кирилла и взгляд невольно упал на кровать Нади."
            current_character "Она отошла к столу и что-то делала там."
            current_character "Ее дневник же лежал раскрытым на полу, видимо, упав от всех передвижений. "
            current_character "Он блестел от количества блесток и наклеек на страницах."
            current_character "Из любопытства я подошел поближе."
            current_character "На развороте были нарисованы конфеты и елки."
            current_character "Небольшая кривая запись в углу бросилась в глаза из-за отсутствия украшений рядом."
            current_character "Мама не должна найти {b}коробку с фотографиями.{/b}"
            current_character "В этот момент она перевернула страницу, выводя меня из транса, и я стал активно перебирать лапами, чтобы выбраться."
            current_character "К счастью, она быстро отпустила меня и я выскочил из комнаты."
            $ gift_children = True
            jump children_end

label children_wrong:
    scene children
    menu:
        'На письменном столе':
            current_character "Я соскочил со стула и добежал до стола."
            current_character "Запрыгнув и оглядевшись, я не заметил ничего примечательного."
            current_character "В этот момент Надя обернулась ко мне. "
            current_character "Видимо, я не успел избежать ее внимания."
            current_character "Цепкие детские ручки обвились вокруг тела и понесли меня в сторону кровати."
            current_character "Пришлось смириться со своим положением пленника."
            current_character "Через некоторое время я выбрался и вернулся к изучению комнаты с высоты стула."
            jump children_wrong
        'В шкафу с одеждой':
            current_character "Я соскочил со стула и добежал до шкафа."
            current_character "Я заскочил на полку благодаря приоткрытой дверце. "
            current_character "В темноте и бардаке ничего не было видно."
            current_character "В этот момент Надя вытащила меня обратно."
            current_character "Видимо, я не успел избежать ее внимания."
            current_character "Цепкие детские ручки обвились вокруг тела и понесли меня в сторону кровати."
            current_character "Через некоторое время я выбрался и вернулся к изучению комнаты с высоты стула."
            jump children_wrong
        'Под кроватью':
            current_character "Я соскочил со стула и добежал до кровати."
            current_character "Только я хотел дотянуться до подарка, как почувствовал, что меня вытаскивают."
            $ renpy.notify("Упс! Вы не успели забрать подарок!")
            current_character "Я громко мявкнул и попытался отбиться, но тщетно."
            current_character "Было неприятно, но ранить маленькую девочку я тоже не хотел."
            current_character "Я зашипел, но Надя только шикнула на меня и понесла к своей кровати."
            current_character "Там она села, крепко обняв меня, и стала показывать свой дневник."
            current_character "Я был расстроен, что не успел взять подарок."
            current_character "Тем не менее, одна вещь бросилась в глаза."
            current_character "На развороте были нарисованы конфеты и елки."
            current_character "Небольшая кривая запись в углу страницы же совсем не была украшена."
            current_character "Мама не должна найти {b}коробку с фотографиями.{/b}"
            current_character "Больше ничего интересного тут не было, и я выскочил из комнаты."
            jump children_end

    return

label children_end:
    scene children
    if gift_children == True:
        $ gifts = gifts + 1

label hallway_2:
    scene hallway
    current_character "Как подсказывала память, все фотографии хранились либо в гостиной на видном месте, либо на чердаке. "
    current_character "Врядли бы Надя стала рисковать и прятать их на прозрачных полках в самом проходимом месте дома, поэтому я направился на чердак."
    current_character "Стоило мне приблизиться к лестнице, как я тут же заметил знакомый маленький силуэт."
    current_character "Мышь бессовестно сидела на третьей ступени и грызла семечко."
    current_character "Я тихо мяукнул, чтобы привлечь ее внимание."
    current_character "Она обернулась и снова вперилась в меня взглядом."

label second_mouse:
    $ renpy.notify("Мышь запомнит ваш ответ!")
    call Msay
    call MenuTwo

label attic:
    current_character "Мышь закончила жевать свое семечко, спустилась с лестницы."
    current_character "Я подумал, что сейчас-то она отреагирует, как нормальная мышь, но нет."
    current_character "Она немного посидела напротив меня, а потом убежала куда-то под лестницу."
    current_character "Я проводил ее взглядом, но продолжил свой путь."

    scene attic

    current_character "Чердак не был слишком пыльным, но, кроме меня и детей, здесь редко бывали."
    current_character "Только на Рождество Владимир мог залезть сюда, чтобы спустить игрушки."
    current_character "Зимой же здесь хранились садовые инструменты."
    current_character "Я забрался на подоконник и осмотрелся."
    current_character "Надо быть внимательным, но быстрым: кто угодно может зайти, если я не угадаю и потеряю время."
    current_character "Где искать подарок?"

    menu:
        'В коробке с фотографиями':
            current_character "Я спрыгнул на пол и подошел к коробке."
            current_character "Поддеть верх было нетрудно."
            scene postcard-and-candies
            $ renpy.notify("Вы нашли третий подарок!")
            current_character "Между фотоальбомами старательно прятались нарисованная открытка и сладости."
            current_character "Надя очень постаралась для мамы."
            current_character "Кажется, она отложила самые вкусные конфеты из своего сладкого подарка."
            current_character "Собрав все конфеты, я направился к лестнице."

            $ gift_attic = True
            jump attic_end
            
        'Под старым диваном':
            current_character "Я спрыгнул на пол и заглянул в пыльное поддиванье."
            current_character "Ничего, кроме пыли и старых игрушек, тут не нашлось. "
            current_character "Я вернулся на подоконник."

            $ gift_attic = False
            jump attic_wrong

        'В старом серванте':
            current_character "Я спрыгнул на пол и подошел к серванту."
            current_character "Рядом удобно стоял стул, поэтому я запрыгнул на него, а потом стал старательно открывать дверцу."
            current_character "Но, как бы я не поддевал лапой створки, они не поддавались."
            current_character "Пришлось вернуться на подоконник."

            $ gift_attic = False
            jump attic_wrong

label attic_wrong:
    menu:
        'В коробке с фотографиями':
            current_character "Я спрыгнул на пол и подошел к коробке."
            current_character "Поддеть верх было нетрудно."
            current_character "Между фотоальбомами старательно прятались нарисованная открытка и сладости."
            current_character "Надя очень постаралась для мамы."
            current_character "Кажется, она отложила самые вкусные конфеты из своего сладкого подарка."
            $ renpy.notify("Упс! Вы не успели забрать подарок!")
            current_character "Вдруг, скрипнули половицы и в комнату вошла хозяйка."
            current_character "Она всегда дорожила своими альбомами."
            current_character "Увидев меня рядом с ними, она всполошилась."
            grandma "Имя, ну что с тобой сегодня? Брысь!"
            grandma "У тебя же коготочки, ты можешь повредить фото."
            current_character "Она подошла ближе, и я, поджав хвост, побежал на выход."
            jump attic_end
            
        'Под старым диваном':
            current_character "Я спрыгнул на пол и заглянул в пыльное поддиванье."
            current_character "Ничего, кроме пыли и старых игрушек, тут не нашлось. "
            current_character "Я вернулся на подоконник."
            jump attic_wrong

        'В старом серванте':
            current_character "Я спрыгнул на пол и подошел к серванту."
            current_character "Рядом удобно стоял стул, поэтому я запрыгнул на него, а потом стал старательно открывать дверцу."
            current_character "Но, как бы я не поддевал лапой створки, они не поддавались."
            current_character "Пришлось вернуться на подоконник."
            jump attic_wrong

label attic_end:
    if gift_attic == True:
        $ gifts = gifts + 1

label after_attic:
    scene hallway
    current_character "Спускаясь по лестнице, я успел услышать, как Владимир очень тихо вышел из их с Катериной комнаты."
    current_character "Он шел украдкой до лестницы в гостиную."
    current_character "Я тихо подошел к самому верху и прислушался."

    mom "Кирилл еще не вернулся, все хорошо."
    dad "Я как раз успел спрятать. Под кровать, правда, не поместился."
    mom "Ну, не слишком скрытно, но за чемоданами точно искать сразу не будут."

    current_character "От разговора меня отвлек шорох в стене."
    current_character "Обернувшись, я увидел как знакомая мышь выползла из еще одной неприметной дырки в плинтусе."
    current_character "Много она их здесь проела?"
    current_character "И как она их вообще прогрызла?"
    current_character "Тут мышь обернулась на меня, словно только заметила."
    current_character "Она потянула воздух носом, аж усы зашевелились."

label third_mouse:
    $ renpy.notify("Мышь запомнит ваш ответ!")
    call Msay
    call MenuTwo

label bedroom:
    current_character "Мышь еще раз принюхалась, как будто чихнула."
    current_character "После этого она вернулась к своим делам и вовсе убежала обратно в стену."
    current_character "Иногда хозяйка крутила пальцем около головы, когда она сомневалась в чужой разумности."
    current_character "Этот жест пришелся бы здесь как нельзя кстати."
    current_character "Тем не менее, я отмахнулся от этого и вернулся в коридор."
    current_character "Мне надо было зайти в другую спальню - Катерины и Владимира."

    scene bedroom
    current_character "Дверь оказалась не закрыта, поэтому пройти внутрь было не трудно."
    current_character "Хотя мне обычно не разрешали, я забрался на кровать и осмотрелся."
    current_character "Надо быть внимательным, но быстрым: кто угодно может зайти, если я не угадаю и потеряю время."
    current_character "Где искать подарок?"

    menu:
        'Около красного чемодана':
            current_character "Я слез с кровати, подошел к чемоданам и обнюхал их."
            current_character "От них пахло незнакомо, чужим домом, поэтому я не часто заходил в эту комнату."
            current_character "Я обошел чемодан и заметил позади него приставленный к стене сноуборд."
            scene snowboard
            $ renpy.notify("Вы нашли четверый подарок!")
            current_character "Кажется, это для Кирилла."
            current_character "Внук хозяйки очень любил зиму и лыжи."
            current_character "Я не разделяю его желание морозить лапы, но родители поддерживали его интересы."
            current_character "Я невольно чихнул при мыслях о снеге и поскорее вышел из комнаты."

            $ gift_bedroom = True
            jump bedroom_end
            
        'За комнатным растением':
            current_character "Я слез с кровати и подошел к горшку."
            current_character "Большие зеленые кусты завешивали целый угол."
            current_character "Рядом стояли еще горшки с кустами поменьше."
            current_character "Я обошел их со всех сторон, но ничего не нашел."
            current_character "Я вернулся обратно на кровать."

            $ gift_bedroom = False
            jump bedroom_wrong

        'На шкафу':
            current_character "Я слез с кровати и, с помощью комода, забрался на самый верх шкафа."
            current_character "Тут было много пыли, пара мух - но не более."
            current_character "С высоты открывался хороший вид, но не более того."
            current_character "Спустившись тем же путем, я вернулся обратно на кровать."

            $ gift_bedroom = False
            jump bedroom_wrong

    label bedroom_wrong:
        menu:
            'Около красного чемодана':
                current_character "Я слез с кровати, подошел к чемоданам и обнюхал их."
                current_character "От них пахло незнакомо, чужим домом, поэтому я не часто заходил в эту комнату."
                current_character "Я обошел чемодан и заметил позади него приставленный к стене сноуборд."
                current_character "Кажется, это для Кирилла."
                current_character "Внук хозяйки очень любил зиму и лыжи."
                current_character "Я не разделяю его желание морозить лапы, но родители поддерживали его интересы."
                current_character "Я невольно чихнул при мыслях о снеге."
                current_character "В этот момент дверь распахнулась и вошла Катерина."
                mom "[current_character], ты что тут делаешь?"
                current_character "Она посмотрела на меня, потом на чемоданы."
                mom "Что, интересно пахнет? Какой ты любопытный."
                current_character "Ничего не предвещало беды, пока я не заметил за спиной Катерины пылесос."
                current_character "Она подхватила меня на руки и выставила в коридор, зная, что это был мой самый нелюбимый предмет в доме."
                $ renpy.notify("Упс! Вы не успели забрать подарок!")

                jump bedroom_end
                
            'Под старым диваном':
                current_character "Я спрыгнул на пол и заглянул в пыльное поддиванье."
                current_character "Ничего, кроме пыли и старых игрушек, тут не нашлось. "
                current_character "Я вернулся на подоконник."
                jump bedroom_wrong

            'В старом серванте':
                current_character "Я спрыгнул на пол и подошел к серванту."
                current_character "Рядом удобно стоял стул, поэтому я запрыгнул на него, а потом стал старательно открывать дверцу."
                current_character "Но, как бы я не поддевал лапой створки, они не поддавались."
                current_character "Пришлось вернуться на подоконник."
                jump bedroom_wrong

label bedroom_end:
    if gift_bedroom == True:
        $ gifts = gifts + 1

label livingroom:
    scene hallway
    current_character "В коридоре я огляделся, но больше не увидел никого."
    current_character "Тут из кухни раздался плач."
    current_character "Я поспешил вниз, сзади из комнаты вышла и Катерина."
    current_character "Мы пришли почти одновременно."
    scene living-room
    current_character "Это была Надя: она снова что-то не поделила с Кириллом."
    current_character "К моменту, когда мы зашли в комнату, злились уже все: и дети, и Владимир, и даже хозяйка."
    current_character "Кому бы понравилось, что в канун праздника в твоем доме кричат и шумят из-за споров и ругани, а не из-за веселья?"
    current_character "Не желая попасть под горячую руку, я выбежал в гостиную и осмотрелся: здесь прятать подарки было негде, в комнате хозяйки никто, даже она сама, не стала бы прятать подарки."
    current_character "Значит, оставалась прихожая."

label hallway_3:
    scene hallway
    current_character "Я вбежал в коридор у входной двери."
    current_character "Здесь было не очень много мест, но зато здесь вряд ли стали бы искать."
    current_character "Надо быть внимательным, но быстрым: кто угодно может зайти, если я не угадаю и потеряю время."
    current_character "Где искать подарок?"

    menu:
        'На верхней полке':
            current_character "Несмотря на высоту полки, мне удалось забраться на нее. "
            current_character "Кроме шапок и шарфов здесь ничего не оказалось."
            current_character "Пришлось спускаться вниз."

            $ gift_hallway = False
            jump hallway_wrong
            
        'В тумбе около вешалки':
            current_character "Я поскреб дверцу."
            current_character "Она была плотно закрыта."
            current_character "Хозяйка всегда долго возилась с ней."
            current_character "Пришлось отбросить этот вариант."

            $ gift_hallway = False
            jump hallway_wrong

        'В шкафу у входа':
            current_character "Я подошел к приоткрытой дверце шкафа и запрыгнул туда."
            current_character "Сначала я не заметил ничего выделяющегося, но внимание привлекла плетеная корзина."
            current_character "Обычно в ней хранилась пряжа хозяйки."
            current_character "Сейчас она почему-то стояла тут."
            current_character "Заглянув вниз, я увидел белого пушистого коня с рогом изо лба."
            scene unicorn
            $ renpy.notify("Вы нашли пятый подарок!")
            current_character "Грива у него была почему-то розовая и вся блестела."
            current_character "Видимо, это подарок для Нади."
            current_character "Я спрыгнул обратно на пол."
            current_character "Крики нарастали, и я поспешил обратно в гостиную."

            $ gift_hallway = True
            jump hallway_end

label hallway_wrong:
    menu:
        'На верхней полке':
            current_character "Несмотря на высоту полки, мне удалось забраться на нее. "
            current_character "Кроме шапок и шарфов здесь ничего не оказалось."
            current_character "Пришлось спускаться вниз."
            jump hallway_wrong
        
        'В тумбе около вешалки':
            current_character "Я поскреб дверцу."
            current_character "Она была плотно закрыта."
            current_character "Хозяйка всегда долго возилась с ней."
            current_character "Пришлось отбросить этот вариант."
            jump hallway_wrong

        'В шкафу у входа':
            current_character "Я подошел к приоткрытой дверце шкафа и запрыгнул туда."
            current_character "Сначала я не заметил ничего выделяющегося, но внимание привлекла плетеная корзина."
            current_character "Обычно в ней хранилась пряжа хозяйки."
            current_character "Сейчас она почему-то стояла тут."
            current_character "Заглянув вниз, я увидел белого пушистого коня с рогом изо лба."
            current_character "Грива у него была почему-то розовая и вся блестела."
            current_character "Видимо, это подарок для Нади."
            current_character "Я хотел было забрать подарок, но в этот момент меня вытащили из шкафа."
            $ renpy.notify("Упс! Вы не успели забрать подарок!")
            son "Ты сегодня тоже странный, [current_character]."
            son "Ходишь по углам, весь в пыли, где-то лазаешь."
            son "Тебе туда нельзя, хорошо, что я тебя нашел."
            current_character "Кирилл говорил спокойно, но на лице все равно была грусть и обида."
            current_character "В руках мальчика я вернулся в гостиную."
            current_character "Оказавшись в дверном проеме, я соскользнул на пол."
            jump hallway_end

label hallway_end:
    if gift_hallway == True:
        $ gifts = gifts + 1

label living_room_fight:
    stop music fadeout 1
    play music sad
    scene living-room
    current_character "Картина была неприятная и в любой другой день, сейчас же тем более."
    current_character "Больно было смотреть на всех."
    mom "Ты забыл про меню, про подарки, сейчас зачем-то обвиняешь меня?"
    dad "Я думал, мы все решили с этим проклятым меню!"
    dad "И не надо рассказывать мне про подарки, когда ты едва не забыла поздравить мою семью!"
    current_character "Хозяйка недовольно сидела в кресле и не вмешивалась, только успокаивала внучку."
    current_character "Кирилл остался стоять у стены около прихожей, но было видно, что он лучше бы сбежал отсюда."
    current_character "В этот момент я начал отчаянно и громко мяукать, привлекая внимание к себе около елки."

    if gifts+like>=5:
        stop music fadeout 1
        play music happy
        current_character "Все обернулись на меня."
        current_character "Сначала часть взглядов обернулись на меня в недоумении, еще часть - с раздражением."
        current_character "Тем не менее, они тут же сменялись удивлением и радостью."

        if gifts == 5:
            current_character "Я точно знал, что рядом со мной под елкой стояли подарки для каждого члена семьи."
            if like > 0:
                current_character "В углу комнаты сидела довольная Мышь."
        else:
            current_character "Хотя за мной стояли не все подарки, я краем глаза заметил шевеление в тени."
            current_character "Там я с удивлением заметил Мышь, которая тащила оставшиеся подарки."

        current_character "Все собрались вокруг елки, гладили и мяли, но сегодня - только сегодня - я был не против."
        grandma "[current_character], как это?... Что это?..."
        daughter "[current_character] переживал за нас!"
        current_character "Единственные слезы, которые лились сейчас, были слезами радости."
        current_character "Я не совсем понимал, как помог, но было радостно видеть улыбку хозяйки и её семьи."
        current_character "Катерина и Владимир перестали кричать друг на друга."
        current_character "Они спокойно обсуждали что-то чуть в стороне ото всех, а потом крепко обнялись."
        current_character "Дети с восторгом открывали свои подарки."
        current_character "Несмотря на то, что Катерина не сделала, как хотела, хозяйка с дочкой сделали много вкусной еды."
        current_character "Вечерний салют был громким, но мягкая рука хозяйки успокаивала."
        current_character "В ночь на Рождество я уснул, свернувшись у неё на коленях."


    elif gifts+like>=3:
        stop music fadeout 1
        play music happy
        current_character "Все обернулись на меня."
        current_character "Сначала часть взглядов обернулись на меня в недоумении, еще часть - с раздражением."
        current_character "Тем не менее, они тут же сменялись удивлением и радостью."
        if like == 0:
            current_character "Хотя за мной стояли не все подарки, я видел, как обиды стали волновать их меньше, чем праздник."
        else:
            current_character "Хотя за мной стояли не все подарки, я краем глаза заметил шевеление в тени."
            current_character "Там я с удивлением заметил Мышь, которая тащила еще часть подарков."
            current_character "Мы не смогли подарить радость всем, но зато в них горела радость за их семью."
        current_character "Хозяйка взяла меня на руки, и я громко заурчал."
        grandma "[current_character], такой умный котик!"
        grandma "Собрал нас здесь, видел, как мы ругаемся…"
        current_character "Мяв вышел тихим, но хозяйка все равно услышала и всхлипнула."
        current_character "Вечером все собрались вместе."
        current_character "Надя все еще косилась на Кирилла."
        current_character "Их родители беззлобно, но подшучивали друг над другом."
        current_character "И все же, в доме наконец воцарился мир."
        current_character "В Рождественскую ночь я лежал на подоконнике и смотрел, как сияют настоящие звезды и их маленькие копии на елке."

    else: 
        current_character "Все обернулись на меня."
        current_character "Чем дольше, тем больше они раздражались и расстраивались."
        mom "Еще и ты, [current_character]! Ну сколько можно! Мама, воспитывай своего кота, пожалуйста!"
        dad "Даже коту уже нельзя побыть котом, да?"
        current_character "Кажется, эта ремарка была лишней."
        current_character "Катерина ничего не ответила, только молча взяла детей и ушла на второй этаж."
        current_character "Владимир постарался дышать глубоко, но, видимо, это не помогло, и он вышел на улицу."
        current_character "Хозяйка осталась сидеть одна, расстроенная и сердитая."
        current_character "Я попытался ластиться к ней, но она только тяжело вздохнула и продолжила сидеть в кресле."
        current_character "Никогда не видел ее такой разбитой."
        current_character "Через 20 минут через плач и “не хочу”, Катерина спустилась с вещами и одетыми детьми."
        grandma "Катя, вы куда?"
        current_character "Дочь хозяйки лишь громко фыркнула."
        mom "Спасибо за поддержку, мамочка."
        mom "Рождество сами как-нибудь проведем."
        current_character "И она вышла, громко хлопнув дверью."
        current_character "Я попытался помурлыкать, чтобы как-то утешить хозяйку, но она только беззвучно плакала."
        current_character "Она встала с кресла и ушла к себе."
        current_character "Я остался стоять посреди гостиной."
        current_character "Снаружи недолго доносился спор, а потом заревела машина."
        current_character "Владимир зашел обратно, принося с собой запахи: свежий - мороза и неприятный - табака."
        current_character "Он грузно опустился на стул и остался так сидеть, смотря в окно."
        current_character "Я лег под елку: впервые в жизни мне было так плохо."
        current_character "Из тени вдруг вышла Мышь."
        rat "..."
        current_character "Глупое создание подошло прямо к моему носу, как будто я не мог съесть её за один укус."
        if like == 0:
            current_character "Тут я заметил что-то в ее лапках: это был маленький уголек и несколько прутовых веточек."
            current_character "Я проследил, как она положила их около носков, которые оставили люди."
            current_character "Было непонятно, что она хочет сказать, но стало совсем тоскливо."
            current_character "Я свернулся клубком, пытаясь заглушить болезненную пустоту в доме и где-то глубоко во мне."
        else:
            current_character "Тут я заметил что-то в ее лапках: это были семечки и немного моего корма."
            current_character "Мышь свернулась в клубок рядом со мной, словно утешая."
            current_character "Мы остались лежать вдвоем, наблюдая в окно, как на дом опускалась ночь."

label credits:
    current_character "Вы прошли игру! С Новым годом и рождеством!"
    return



    

