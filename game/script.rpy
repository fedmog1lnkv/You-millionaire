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

    show Igor

    Igor "Сколько я спал?"
    Igor "Чем я занимался вчера?"

    Igor "А что это под кроватью?"

    Narrator "Игорь находит чемодан возле кровати"

    Igor "Кажется, я где-то его видел, как будто еще со школы, я носил его каждый день."
    hide Igor

    scene black

    Narrator "Игорь открыл чемодан, в нём лежала огромная сумма денег."

    scene suitcase

    Igor "Я еще сплю? Откуда это? Может, я украл их у кого-то? Но я всю жизнь был честным…"

    Mind "Уже 19:40. Я ничего не понимаю, но мне пора к друзьям на встречу."



label choose_pers:

    scene black

    show eileen happy

    Narrator '''На просторах интернета давно не было занимательных историй, которые смогли бы заинтересовать искушенного читателя.'''

    Narrator '''Наверное, и наша команда не сможет этого сделать, но мы постарались.'''

    Narrator '''Для начала увлекательного приключения нужно выбрать персонажа, глазами которого мы расскажем о том, что произошло в городе Н.'''


    menu:
        "Выберите судьбу"
        "Вова":
            jump choose_Vova
        "Игорь":
            jump choose_Igor
        "Маша":
            jump choose_Masha
    return

label choose_Vova:

    scene bg black

    Narrator "вы выбрали Вову"

label choose_Igor:

    scene bg black

    Narrator "вы выбрали Игоря"

label choose_Masha:

    scene bg black

    Narrator "вы выбрали Машу"



label club:
    scene bg black

    show eileen

