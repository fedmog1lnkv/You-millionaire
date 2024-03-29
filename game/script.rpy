﻿init python:
    open_eyes = ImageDissolve("eye.png", 2.0, 20, reverse=False)
    close_eyes = ImageDissolve("eye.png", 2.0, 20, reverse=True)

# Начало игры
label start:
    scene room_day with open_eyes

    play music "<loop 0.1>sound/1/out.mp3"

    show Igor think with dissolve

    Igor "Сколько я спал?"
    Igor "Чем я занимался вчера?"

    Narrator "Игорь находит чемодан возле кровати"

    Igor "Кажется, я где-то его видел, как будто еще со школы, я носил его каждый день."
    hide Igor

    scene black

    Narrator "Игорь открыл чемодан, в нём лежала огромная сумма денег."

    scene suitcase with fade

    Mind "Я еще сплю?{w} Откуда это?{w} У кого я мог украсть такую сумму денег? Но я всю жизнь был честным..."

    Mind "Уже 19:40. Я ничего не понимаю, но мне пора к друзьям на встречу."

    scene black with fade

    FullScreen 'На просторах интернета давно не было занимательных историй, которые смогли бы заинтересовать искушенного читателя.'
    FullScreen 'Наверное, и наша команда не сможет этого сделать, но мы постарались.'
    FullScreen 'Для начала увлекательного приключения нужно выбрать персонажа, глазами которого мы расскажем о том, что произошло в городе Н.'

    nvl clear


label person_menu:
    scene choose_person with fade

    menu:
        "Выберите судьбу"
        "Вова":
            FullScreen "Постоянно занятый работой, он изредка находит время для посиделок с друзьями."
            FullScreen "В студенчестве он был достаточно амбициозным. Мысли и разговоры о новых проектах занимали большую часть его времени и часто окружающие"
            FullScreen "пророчили ему хорошее будущее в какой-нибудь крупной кампании."

            nvl clear

            menu:
                "Выбрать историю Вовы":
                    jump scene_2
                "Назад":
                    jump person_menu
        "Игорь":
            FullScreen "Молодой парень, который работает в Маке. В целом его жизнь не отличается от жизни миллионов других людей."
            FullScreen "Каждое утро он просыпается, ворчит на свою работу и проводит свой день ровно так же, как проводил тысячи и тысячи дней до этого."
            FullScreen "Он рос совершенно обычным парнем и старался особо ничем не выделяться, ведь именно так его и воспитали."

            nvl clear

            menu:
                "Выбрать историю Игоря":
                    jump scene_4
                "Назад":
                    jump person_menu
        "Маша":
            FullScreen "Молодая девушка, всерьез увлекающаяся живописью, мечтающая найти себя."
            FullScreen "Живопись она полюбила с детства. И вообще, она чем-то до сих пор похожа на ребенка: наивная, эмоциональная и очень открытая, она часто пленяла своим характером окружающих."
            FullScreen "Маша очень много времени провела в своем родном городе, потому что была очень привязана к матери."

            nvl clear

            menu:
                "Выбрать историю Маши":
                    jump scene_3
                "Назад":
                    jump person_menu

# Выбор Вовы
label scene_2:
    scene office_evening with fade

    play music "<loop 0.1>sound/6/out.mp3"

    Mind "Боже, как я устал...{w} Еще 10 минут, и я оторвусь по полной."

    show Boss norm at right with dissolve

    Boss "Владимир!{w} Ты сделал за сегодня все отчёты?"
    Mind "Какой же он ублюдок!{w} Каждый день видеть его лицо, да лучше бы я остался у себя в городе и работал всю жизнь на заводе!"

    show Vova norm at left with dissolve

    Vova "Да, я все сделал."

    hide Boss
    show Boss happy at right with dissolve

    Boss "Ха-ха-ха,{w} ну вот и отлично, вижу ты хорошо выполняешь свою работу, еще немного и получишь премию."

    hide Boss

    show Vova angry
    Mind "Не дождёшься, урод!{w} С сегодняшнего дня я начинаю стартап умных чехлов!{w} Вы все увидите мою мощь!"

    show Vova norm
    Mind "Только... {w}где найти деньги?"

    hide Vova

    jump scene_5

# Выбор Маши
label scene_3:
    scene black

    play music "<loop 0.1>sound/4/out.mp3"

    Narrator "Маша сидит и ждёт результата врачей. Напряженность в воздухе означает что-то неладное."

    scene hospital with fade

    show Masha norm at left with dissolve

    Masha "С ней всё будет хорошо?"

    show Doctor norm at right with dissolve

    Doctor "Да...{w} С ней все будет хорошо, не беспокойтесь..."
    Doctor "Но, есть один нюанс...{w} Это дорогостоящая операция. Вам нужно будет заплатить миллион рублей."
    Masha "Что?{w} А как же обещанные государством деньги?"
    Doctor "Послушайте... {w}К сожалению, я ничего не могу Вам обещать, у нас очень большая очередь."
    Doctor "Вы понемногу продвигаетесь, но скорее всего мы можем не успеть..."

    hide Doctor
    hide Masha

    Mind "Почему у меня нет денег?.. Я могла бы работать в большом городе и дать все своей матери."
    Mind "А теперь...{w} теперь я работаю уборщицей на этом гребанном заводе."

    jump scene_6

# Клуб
label scene_4:
    scene club with fade
    play music "<loop 0.1>sound/3/out.mp3"

    show Masha norm at left with dissolve
    Masha "Ну что, как прошли ваши будние дни?"

    show Vova norm reverse at right with dissolve
    Vova "Да-а, как всегда.{w} Босс орёт, постоянно трясет с меня эти долбанные отчеты..."
    Vova "А, знаете{w}, я еще в студенчестве думал о создании собственного стартапа."
    Vova "Мы же всегда хотели это сделать, Игорь.{w} Помнишь, как мы мечтали стать богатыми?"
    Vova "Каждый день, просыпаясь с утра в своей комнате в общаге..."

    hide Masha
    show Igor norm at left with dissolve

    Igor "Да...{w} Хорошее было время..."
    Vova "Но мы можем это сделать сейчас!{w} Только нам нужны деньги..."
    Vova "Эти чертовы деньги, которых никогда обычно нет!{w} Вот проснуться бы с миллионом под подушкой!"
    Igor "Да..."

    hide Vova

    show Masha norm reverse at right with dissolve

    Masha "Эх...{w} Я бы тоже хотела миллион."
    Masha "Моя мама лежит сейчас в больнице. Врачи говорят, что ей станет лучше только после операции"
    Masha "Я не знаю где мне найти столько денег."

    show Masha cryed reverse at right with dissolve

    Masha "Я боюсь я ее не вылечу..."
    Igor "Эй...{w} Я надеюсь, с ней все будет хорошо..."
    Masha "Не знаю!{w} Ей нужны деньги на операцию, а у меня...{w} у меня..."

    hide Igor
    show Vova angry at left with dissolve

    Vova "Ну успокойся, что ты так реагируешь?!"

    hide Masha
    show Igor norm reverse at right with dissolve

    Igor "У нее действительно проблема."
    Vova "Не знаю, как у нее, а у меня точно проблемы!"

    hide Vova
    show Masha norm at left with dissolve

    Masha "Ну что мы все о себе да о себе?!"
    Masha "Игорь, как у тебя дела с девушкой?"
    Igor "Никак...{w} она меня динамит."
    Igor "Она сказала, что я ничтожество.{w} Что мне никогда не добиться того, чего добились уже все мои друзья."
    Igor "Но, я думаю, завтра она возьмёт свои слова обратно!"

    hide Masha
    show Vova norm at left with dissolve

    Vova "О чём ты?"

    hide Igor
    hide Vova

    Mind "Боже...{w} Может, им и правда эти деньги нужнее..."

    menu:
        "Отдать деньги Вове":
            Igor "Выйдем на улицу, что-то мне не хорошо..."

            scene entry_club with fade
            play music "<loop 0.1>sound/7/out.mp3"

            show Vova norm at left with dissolve
            Vova "Игорь, тебе в какую сторону?"

            show Igor norm reverse at right with dissolve
            Igor "Мне нужно в центр. Я на метро."

            hide Igor

            show Masha norm reverse at right with dissolve
            Masha "Пока..."

            hide Masha

            show Igor norm reverse at right with dissolve
            Vova "Ладно. И мне, наверное, пора."
            Igor "Постой!{w} Вова!"
            Vova "М?"
            Igor "Знаешь, я тут подумал над твоим проектом...{w} У меня есть для тебя предложение..."

            nvl clear
            FullScreen "Вы решаете отдать деньги Вове в надежде на то, что эти вложения когда-то смогут окупиться"

            jump scene_9

        "Оставить деньги себе":
            Igor "Выйдем на улицу, что-то мне не хорошо..."

            scene entry_club with fade
            play music "<loop 0.1>sound/7/out.mp3"

            show Vova norm reverse at right with dissolve
            Vova "Тебе в какую сторону?"

            show Igor norm at left with dissolve
            Igor "Прости, дружище. Я хочу побыть один, хочу обдумать все, прогуляться."
            Igor "Пока, ребята."
            Vova "Счастливо..."

            hide Vova

            show Masha norm reverse at right with dissolve
            Masha "Пока..."

            hide Masha
            hide Igor

            Mind "Я не знаю, правилен ли мой выбор...{w} Но, в любом случае, я его уже сделал."

            nvl clear
            FullScreen "Вы решаете оставить деньги себе. Игорь с противоричивыми мыслями уходит"

            jump scene_11

        "Отдать деньги Маше":
            Igor "Выйдем на улицу, что-то мне не хорошо..."

            scene entry_club with fade
            play music "<loop 0.1>sound/7/out.mp3"

            show Masha norm reverse at right with dissolve
            Masha "Тебе в какую сторону?"

            show Igor norm at left with dissolve
            Igor "Я хотел поехать на такси. Мне в сторону центра, тебе тоже?"
            Masha "Да, нам по пути.{w} Я поеду с тобой."
            Masha "Пока, Вова."

            hide Igor

            show Vova norm at left with dissolve
            Vova "До встерчи..."

            hide Vova

            show Igor norm at left with dissolve
            Igor "Мне действительно жаль твою маму, и я хочу тебе помочь..."

            jump scene_10


label scene_5:
    scene club with fade
    play music "<loop 0.1>sound/3/out.mp3"

    show Masha norm reverse at right with dissolve
    Masha "Ну что, как прошли ваши трудовые будни?"

    show Vova angry at left with dissolve
    Vova "Этот босс действует мне на нервы, но скоро это буду делать я..."
    show Vova norm at left with dissolve
    Vova "Решил, да ну его, начну делать стартап."
    Vova "Мы же всегда хотели это сделать, братан, помнишь как мы хотели покорять вершины и быть супер богатыми."

    hide Masha

    show Igor norm reverse at right with dissolve
    Igor "Да...{w} это именно то что мне нужно!"

    Vova "Но мы можем это сделать сейчас!"
    Vova "Нам только нужны деньги, и мне кажется, что мы сейчас их сможем получить."
    Igor "Да..."

    hide Vova

    show Masha norm at left with dissolve
    Masha "Эх...{w} Я бы тоже хотела миллион. Моя мама лежит сейчас в больнице, одна."
    Masha "И...{w} Я не знаю, что мне делать. Мне нужны деньги."
    Igor "Эй...{w} Я думаю с ней все будет хорошо..."
    show Masha cryed at left with dissolve
    Masha "Я не знаю!{w} Ей нужны деньги на операцию, а у меня...{w} у меня..."

    hide Igor

    show Vova angry reverse at right with dissolve
    Vova "Да сдай ты ее уже куда-нибудь, мне эти деньги для бизнеса, а тебе для какой-то чепухи."
    Igor "..."
    Vova "Не знаю, как у нее, а у меня очень важные планы."

    show Masha norm at left with dissolve
    Masha "Ну что мы все о себе."
    Masha "Игорь, как у тебя дела с девушкой?"

    hide Vova

    show Igor norm reverse at right with dissolve
    Igor "Никак, она меня динамит."
    Igor "Сказала, что я нищеброд, работаю в маке и в жизни не заработаю нормальных денег."
    Igor "Но я думаю завтра она возьмёт свои слова обратно."

    hide Masha

    show Vova norm at left with dissolve
    Vova "О чём ты?"
    Masha "..."

    hide Vova
    hide Igor

    scene entry_club with fade

    play music "<loop 0.1>sound/7/out.mp3"

    show Vova norm at left with dissolve
    Vova "Тебе в какую сторону?"

    show Igor norm reverse at right with dissolve
    Igor "В сторону центра. Сегодня я на метро"
    Vova "Мне туда же,{w} пока Маша"

    hide Igor

    show Masha norm reverse at right with dissolve
    Masha "Пока..."

    hide Masha

    show Igor norm reverse at right with dissolve
    Igor "Знаешь, я тут подумал над твоим проектом...{w} Мне есть что тебе рассказать!"
    Igor "У меня есть миллион..."
    Vova "Что?{w} Откуда?"
    Igor "Я не знаю, как так вышло, не спрашивай..."
    Igor "но я могу отдать его тебе..."

    menu:
        "но я могу отдать его тебе..."
        "Взять деньги":
            show Vova happy at left with dissolve
            Vova "Конечно брат!{w} Мы так долго об этом мечтали"
            Vova "Завтра же начнём работу на проектом!"

            jump scene_8
        "Отказаться":
            Vova "Спасибо, но, думаю, я сам смогу найти деньги, не хочу влезать в долги."
            Mind "Я что-нибудь придумаю..."

            jump scene_7


label scene_6:
    scene club with fade

    play music "<loop 0.1>sound/3/out.mp3"

    show Masha happy at left with dissolve
    Masha "Ну что, парни, как ваши дела? Есть что-нибудь новенькое?"

    show Vova norm reverse at right with dissolve
    Vova "Никак...{w} все так же тускло."
    Vova "Подумываю над стартапом{w}, но не знаю даже с чего начать."

    hide Vova

    show Masha norm at left with dissolve
    show Igor norm reverse at right with dissolve
    Igor "Эх..."
    Masha "Эх...{w} Я бы тоже хотела миллион."
    Masha "Моя мама лежит сейчас в больнице, одна. Я не знаю что мне делать."
    show Masha cryed at left with dissolve
    Masha "Я боюсь я ее не вылечу..."
    Igor "Эй...\nЯ думаю с ней все будет хорошо..."
    Masha "Я не знаю!"
    Masha "Ей нужны деньги на операцию, а у меня..."
    Masha "У меня..."

    hide Masha

    show Vova norm at left with dissolve
    Vova "Мне очень жаль..."
    Igor "У нее действительно проблема."
    Vova "Что бы могло произойти, что бы ей стало лучше."

    hide Vova

    show Masha cryed at left with dissolve
    Masha "Я не знаю, мне очень плохо в последние дни, но думаю я как-нибудь справлюсь."
    show Masha norm at left with dissolve
    Masha "Игорь, как у тебя дела с девушкой?"
    Igor "Никак, она меня динамит."
    Igor "Она сказала, что я нищеброд и работаю в маке."
    Igor "Но я думаю завтра она возьмёт свои слова обратно."

    hide Masha

    show Vova norm at left with dissolve
    Vova "О чём ты?"
    Masha "..."

    hide Vova
    hide Igor

    Igor "Выйдем на улицу, что-то мне не хорошо..."

    scene entry_club with fade

    play music "<loop 0.1>sound/7/out.mp3"

    show Masha norm at left with dissolve
    Masha "Тебе в какую сторону?"

    show Igor norm reverse at right with dissolve
    Igor "Думаю таксу заказать."

    Masha "Я поеду с тобой, нам по пути."
    Masha "Пока, Вова"

    hide Igor

    show Vova norm reverse at right with dissolve
    Vova "Пока..."

    hide Vova

    show Igor think reverse at right with dissolve
    Igor "Мне действительно жаль твою маму, и я хочу тебе помочь..."
    Igor "И я могу пожертвовать этот миллион ей на лечение"
    Masha "Я не могу, это же..."
    Igor "Послушай, сейчас не спрашивай, просто возьми их."

    menu:
        "Игорь предлагает тебе деньги."
        "Взять деньги":
            show Masha happy at left with dissolve
            Masha "Спасибо тебе большое, ты мой герой!"

            jump scene_13
        "Отказаться":
            Masha "Я не могу это сделать, я дождусь бесплатного лечения..."

            jump scene_12


label scene_7:
    scene office_evening with fade

    play music "<loop 0.1>sound/6/out.mp3"

    show Vova angry at left with dissolve

    Mind "Опять он идёт сюда...{w} Что ему от меня надо?.."

    show Boss norm at right with dissolve

    Boss "Ну что, ватокат, как работа продвигается?"
    show Vova norm at left with dissolve
    Vova "..."
    show Boss happy at right with dissolve
    Boss "Слушай, я вчера задержался немного, посмотрел твои наметки на столе, мне понравилась твоя идея с чехлами."
    Vova "Это здорово, а к чему это?"
    Boss "Наша компания решила запустить эту линию, а тебе дать надбавку в виде премии."
    Boss "Ты проделал большую работу."
    Vova "Но...{w} Но, это же моя работа."
    show Boss norm at right with dissolve
    Boss "А нас...{w} нас это не волнует."

    hide Boss
    hide Vova

    jump scene_15


label scene_8:
    scene office_evening with fade

    play music "<loop 0.1>sound/6/out.mp3"

    show Vova angry at left with dissolve

    Mind "Опять он идёт сюда...{w} Что ему от меня надо?.."

    show Boss norm at right with dissolve

    Boss "Владимир, как идет работа?"
    show Vova norm at left with dissolve
    Vova "..."
    Boss "Слушай, я вчера задержался немного, посмотрел твои записи на своем столе.{w} Я оценил идею с чехлами."
    Vova "Хм...{w} Спасибо!{w} Но Вы это к чему?"
    show Boss happy at right with dissolve
    Boss "Наша компания решила запустить эту линию, а тебе дать надбавку в виде премии."
    Boss "Ты проделал большую работу"
    Vova "Но...{w} Но, это же моя работа."
    show Boss norm at right with dissolve
    Boss "А нам...{w} Наплевать."


    show Vova angry at left with dissolve
    Mind "Урод...{w} Неужели он всерьез думает, что сможет в кой то веке сделать что-то лучше меня?"
    Mind "Да я сделаю в 100 раз больше и лучше!"
    show Boss happy at right with dissolve
    Boss "И да, кстати, твои идеи принесли нам огромный оборот, в следующем квартале планируется достигнуть оборота в полмиллиарда рублей."

    hide Boss
    hide Vova

    Mind "Сколько я спал?"

    jump scene_14


label scene_9:
    scene restaurant with fade

    play music "<loop 0.1>sound/5/out.mp3"

    show Igor norm at left with dissolve
    Igor "Как приятно пригласить тебя в этот вечер"

    show Girlfriend angry at right with dissolve
    Girlfriend "Ну давай без этой ванили, ты мне хотел что-то рассказать"
    Igor "..."
    Igor "Мы с моим другом открываем стартап"
    Girlfriend "И что вы делать собираетесь?"
    Igor "Огромный проект, умные чехлы для телефона, я уверен он выстрелит"

    show Girlfriend norm at right with dissolve
    Girlfriend "Понятненько, но я все равно в этом ничего не понимаю, мне важен результат."
    Igor "Я сделаю это, и ты увидишь, как мы ездим по дорогим отелям, и едим вкуснейшую еду."
    Girlfriend "Ну ну..."
    Girlfriend "Ха-ха"

    hide Girlfriend

    hide Igor

    jump scene_14


label scene_10:
    scene restaurant with fade

    play music "<loop 0.1>sound/5/out.mp3"

    show Igor norm at left with dissolve

    Igor "Как приятно снова встретиться с тобой.{w} Мы так давно не виделись"

    show Girlfriend angry at right with dissolve
    Girlfriend "Игорь, прошу тебя!{w} Давай без этой занудной романтики.{w} Ты хотел мне что-то рассказать?"
    Igor "..."
    Igor "Я сделал доброе дело.{w} Сегодня я спас жизнь..."
    show Girlfriend norm at right with dissolve
    Girlfriend "Как?"
    Igor "У моей подруги была трудная ситуация. Ее мама была в больнице, и ей срочно нужна была операция."
    Igor "Я оплатил её, и я так рад что я спас ей жизнь. Ничто в жизни так не важно, как делать добрые дела."
    Girlfriend "Понятненько, но я все равно в этом ничего не понимаю, мне важен результат."
    show Girlfriend angry at right with dissolve
    Girlfriend "Тем более ты сам еще ничего не добился в этой жизни."
    Igor "Но я же хотел помочь ей."
    Girlfriend "Но, ты сам то чего добился?"
    show Girlfriend norm at right with dissolve
    Girlfriend "Ха-ха"
    Igor "Не знаю..."

    hide Girlfriend

    hide Igor

    jump scene_16


label scene_11:
    scene restaurant with fade

    play music "<loop 0.1>sound/5/out.mp3"

    show Igor norm at left with dissolve


    Igor "Как приятно пригласить тебя в этот вечер"

    show Girlfriend angry at right with dissolve
    Girlfriend "Ну давай без этой ванили, ты мне хотел что-то рассказать"
    Igor "..."
    Igor "А хочешь я завтра увезу тебя в кругосветное путешествие?"
    Girlfriend "И в какое же?"
    Igor "Мы можем объехать всю Европу, побывать в Америке в дорогих отелях."
    Igor "На лучших пляжах, есть вкусную еду."
    show Girlfriend norm at right with dissolve
    Girlfriend "Я не против, только я хочу еще личную машину, чтобы мы могли ездить из города в город."
    Girlfriend "Хочу нашу личную яхту, там мы пригласим гостей и сделаем большую вечеринку, чтобы все офигели."
    Girlfriend "А еще я хочу.."

    Igor "Я не смогу сейчас это сделать..."
    show Girlfriend angry at right with dissolve
    Girlfriend "Почему? А я хочу! Сделай это! Игорь, мы же любим друг друга, тебе жалко ради меня?"
    Igor "Мне нужно идти"

    hide Igor

    show Girlfriend norm at right with dissolve
    Girlfriend "Постой Игорь, почему ты уходишь? А кто же будет платить! Тебе не стыдно, так оставлять девушку?"
    Girlfriend "Кабель..."

    hide Girlfriend

    jump scene_15


label scene_12:
    scene hospital with fade

    play music "<loop 0.1>sound/4/out.mp3"

    show Masha cryed at left with dissolve

    Masha "Доктор, я не смогла найти деньги, я беспомощна, я ненавижу себя, я..."

    show Doctor norm at right with dissolve

    Doctor "Постойте, нам не нужны ваши деньги, местный фонд заинтересовался вашей матерью и оплатил полную сумму."
    Doctor "С ней все будет хорошо!"

    show Masha happy at left with dissolve
    Masha "Боже, это какое-то чудо! Мама!"
    Doctor "Ей нужен покой приходите через неделю."
    Masha "Спасибо доктор!"
    Doctor "До свидания"

    hide Doctor
    hide Masha

    Mind "Я не знаю почему я не испытала такую бурную радость от этих слов"

    jump scene_15


label scene_13:
    scene hospital with fade
    play music "<loop 0.1>sound/4/out.mp3"

    show Masha happy at left with dissolve

    Masha "Доктор, как она? Я принесла деньги, вот они!"

    show Doctor norm at right with dissolve

    Doctor "Постойте, нам не нужны ваши деньги, местный фонд заинтересовался вашей матерью и оплатил полную сумму."
    Doctor "С ней все будет хорошо!"
    Masha "Боже, я так рада, спасибо огромное!"
    Doctor "Ей нужен покой приходите через неделю."
    Masha "Спасибо доктор!"
    Masha "Но...{w} Что мне делать с этими деньгами?"
    Doctor "Этот вопрос уже к вам. До свидания"

    hide Doctor
    hide Masha

    Mind "Зачем я взяла эти деньги? Дура, надо было отдать им на проект!"
    Mind "Они мои друзья, а теперь...Теперь у них ничего не получится! Нужно скорее вернуть им эти деньги."

    jump scene_16


label scene_14:
    scene club with fade
    play music "<loop 0.1>sound/2/out.mp3"

    show Igor norm at left with dissolve
    show Vova norm reverse at right with dissolve

    Igor "Вован!{w} Ну что, как там с проектом? Мы должны подняться!"
    Igor "Я был сегодня с девушкой на свидании и..."
    Vova "Нету у нас больше проекта...{w} Забирай деньги."
    Igor "ЧТО?!"

    hide Igor
    show Masha norm at left with dissolve
    Masha "Что случилось?"
    Vova "Босс спалил все наши планы и сам запустил эту линейку..."
    hide Masha

    show Igor think at left with dissolve
    Igor "..."
    Igor "Я не знаю, что даже сказать...{w} Значит не получится осуществить наш стартап, который мы так хотели сделать?"
    Vova "Получается, что так."

    hide Vova

    show Masha norm reverse at right with dissolve
    Masha "Не расстраивайся!{w} Значит так нужно было, в любом случае все будет хорошо!"
    Masha "Кстати... {w} Моя мама идет на поправку!"
    Igor "Правда?{w} Я рад этому..."
    hide Masha

    show Vova happy reverse at right with dissolve
    Vova "Ага{w} и я..."

    jump scene_17


label scene_15:
    scene club with fade

    play music "<loop 0.1>sound/2/out.mp3"

    show Igor norm at left with dissolve

    show Vova norm reverse at right with dissolve

    Vova "Ну что, Игорь, как свидание?"
    Igor "Да никак!{w} Я ее послал к чертям она еще та *****"
    Vova "Ха-ха, ну я сразу видел в ней это"
    Igor "Ага..."
    Mind "Как же мне стыдно и неловко, что я не отдал им эти деньги..."

    hide Vova
    show Masha norm reverse at right with dissolve
    Masha "Ну ладно, и такое бывает."
    hide Masha
    Igor "Ладно, я пойду, еще дел куча, пожалуй надо выспаться."
    hide Igor
    Mind "Какой позор...{w} Опять..."

    Vova "Давай."
    Masha "Пока."

    jump scene_17


label scene_16:
    scene club with fade
    play music "<loop 0.1>sound/2/out.mp3"

    show Masha norm at left with dissolve

    Masha "Парни, простите меня!{w} Я взяла деньги и не подумала о вас, мне так стыдно."

    show Vova norm reverse at right with dissolve
    Vova "Какие деньги?"

    hide Vova
    show Igor norm reverse at right with dissolve
    Igor "Неважно, главное, что с мамой все хорошо!"
    Masha "С ней и так все хорошо, я верну деньги тебе Игорь, для вашего проекта, спасибо, что помог."

    hide Masha
    show Vova angry at left with dissolve
    Vova "Игорь?{w} Они у тебя были?"
    Igor "..."
    Igor "Я хотел помочь ей!"
    Vova "Ясно друг, я пошёл, всего хорошего."

    hide Vova
    show Masha norm at left with dissolve
    Masha "Не расстраивайся значит так нужно было, в любом случае все хорошо"
    show Igor think reverse at right with dissolve
    hide Masha
    show Vova angry at left with dissolve
    Igor "Да Вова, ты чего?"
    Vova "Ни-че-го,{w} чао."

    jump scene_17


label scene_17:
    scene room_evening with fade

    play music "<loop 0.1>sound/2/out.mp3"

    show Igor think with dissolve

    Igor "Я не знаю, что я опять сделал не так..."
    Igor "ЧТО Я ОПЯТЬ СДЕЛАЛ НЕ ТАК?!"
    Igor "Этот чемодан опять остался со мной.{w} Напьюсь, и станет легче, надоело мучаться..."

    hide Igor
    scene black with close_eyes

    Mind "И опять в моей жизни ничего не изменилось..."

    jump start
