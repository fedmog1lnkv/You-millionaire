# Вы можете расположить сценарий своей игры в этом файле.
init python:
    open_eyes = ImageDissolve("eye.png", 2.0, 20, reverse=False)
    closw_eyes = ImageDissolve("eye.png", 2.0, 20, reverse=True)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene room_evening with open_eyes

    show Igor  with dissolve

    Igor "Сколько я спал?"
    Igor "Чем я занимался вчера?"

    Narrator "Игорь находит чемодан возле кровати"

    Igor "Кажется, я где-то его видел, как будто еще со школы, я носил его каждый день."
    hide Igor

    scene black

    Narrator "Игорь открыл чемодан, в нём лежала огромная сумма денег."

    scene suitcase with fade

    Igor "Я еще сплю? Откуда это? У кого я мог украсть такую сумму денег? Но я всю жизнь был честным…"

    Mind "Уже 19:40. Я ничего не понимаю, но мне пора к друзьям на встречу."



label choose_pers:

    scene black with fade


    Narrator '''На просторах интернета давно не было занимательных историй, которые смогли бы заинтересовать искушенного читателя.'''

    Narrator '''Наверное, и наша команда не сможет этого сделать, но мы постарались.'''

    Narrator '''Для начала увлекательного приключения нужно выбрать персонажа, глазами которого мы расскажем о том, что произошло в городе Н.'''


    menu:
        "Выберите судьбу"
        "Вова":
            jump office_evening_2
        "Игорь":
            jump club_4
        "Маша":
            jump hospital_evening_3


label office_evening_2:

    scene office_evening with fade

    Mind "Боже, как я устал…"
    Mind "Еще 10 минут, и я оторвусь по полной."

    show Boss  at right  with dissolve

    Boss "Владимир, Ты сделал за сегодня все отчёты?"

    Mind "Какой же он ублюдок, каждый день видеть его лицо, да лучше бы я остался у себя в городе и работал всю жизнь на заводе."

    show Vova  at left with dissolve

    Vova "Да, я все сделал."

    hide Boss
    show Boss happy
    Boss "Ха-ха-ха,"
    Boss "ну вот и отлично, вижу ты хорошо выполняешь свою работу, еще немного и получишь премию."
    hide Boss

    Mind "Не дождёшься урод, с сегодняшнего дня я начинаю стартап умных чехлов, вы все увидите мою мощь."
    Mind "Только… где найти деньги?"
    hide Vova

    return

label hospital_evening_3:

    scene black

    Narrator "Маша сидит и ждёт результата врачей. Напряженность в воздухе означает что-то неладное."

    scene hospital with fade

    show Masha  at left with dissolve

    Masha "С ней всё будет хорошо?"

    show Doctor  at right with dissolve

    Doctor "Да…"
    Doctor "С ней все будет хорошо не беспокойтесь…"
    Doctor "Но, есть один нюанс..."
    Doctor "Эта операция будет стоить вам миллион, вы готовы ее оплатить?"

    Masha "Что?"
    Masha "А как же обещанные государством деньги?"

    Doctor "Послушайте, у нас очень большая очередь."
    Doctor "Вы понемногу продвигаетесь, но скорее всего мы уже не успеем…"

    hide Doctor
    hide Masha

    Mind "Почему у меня нет много денег? Я могла работать в большом городе и дать все своей матери."
    Mind "А теперь…"
    Mind "теперь я работаю уборщицей на этом гребанном заводе."

    return

label club_4:

    scene club with fade

    show Masha at left with dissolve
    Masha "Ну что как прошли ваши будние дни?"

    show Vova  reverse at right with dissolve
    Vova "Да как всегда, босс орёт, сижу и делаю эти долбанные отчёты…"
    Vova "Решил да ну его, начну делать стартап."
    Vova "Мы же всегда хотели это сделать братан, помнишь как мы хотели покорять вершины и быть супер богатыми."

    hide Masha

    show Igor at left with dissolve
    Igor "Да…"
    Igor "Это было лучшее время…"

    Vova "Но мы можем это сделать сейчас!"
    Vova "Нам только нужны деньги"
    Vova "Эти чертовы деньги, которых никогда обычно нет. Вот проснуться бы с миллионом и мы бы получили всего что хотели!"

    Igor "Да…"

    hide Vova

    show Masha reverse at right with dissolve

    Masha "Эх… Я бы тоже хотела миллион."
    Masha "Моя мама лежит сейчас в больнице, одна. Я не знаю что мне делать."
    show Masha cryed reverse at right with dissolve
    Masha "Я боюсь я ее не вылечу…"

    Igor "Эй…"
    Igor "Я думаю с ней все будет хорошо…"

    Masha "Я не знаю!"
    Masha "Ей нужны деньги на операцию, а у меня…"
    Masha "у меня…"

    hide Igor

    show Vova at left with dissolve
    Vova "Ну успокойся, что ты так реагируешь"

    hide Masha

    show Igor at right with dissolve
    Igor "У нее действительно проблема."

    Vova "Не знаю, как у нее, а у меня точно проблемы"

    hide Vova

    show Masha at left with dissolve
    Masha "Ну что мы все о себе."
    Masha "Игорь, как у тебя дела с девушкой?"

    Igor "Никак, она меня динамит."
    Igor "Она сказала, что я нищеброд и работаю в маке."
    Igor "Но я думаю завтра она возьмёт свои слова обратно!"

    hide Masha

    show Vova at left with dissolve
    Vova "О чём ты?"

    hide Igor
    hide Vova
