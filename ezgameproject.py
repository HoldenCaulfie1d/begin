def Rock_Paper_Scissor():
    var_list = ['Камень', 'Бумага', 'Ножницы']
    a = 'start'
    while a != 'exit':
        scor = []
        scor2 = []
        var_rnd = random.choice(var_list)
        resp = input('Выберите действие для игры: Камень, Бумага, Ножницы.\n(Если хотите выйти введите - exit)\n')
        a, b, c = 'Ножницы', 'Камень', 'Бумага'
        print('Счет - ', len(scor), len(scor2))
        if resp == 'exit':
            a = 'exit'
            print('Игра окончена...')
            
        elif resp != a and resp!= b and resp!= c: 
            print('Ошибка...\nТаких действий в программе нет.')
        
        else:
            win = True
            while win == True:
                print('Соперник выбрал: ', var_rnd)
                if resp == 'Бумага' and var_rnd == 'Камень':
                    print('Поздравляю, вы выиграли!')
                    scor.append('a')
                    win = False

                elif resp == 'Камень' and var_rnd == 'Ножницы':
                    print('Поздравляю, вы выиграли!')
                    win = False
                elif resp == 'Ножницы' and var_rnd == 'Бумага':
                    print('Поздравляю, вы выиграли!')
                    win = False
                elif resp == 'Бумага' and var_rnd == 'Бумага':
                    print('Ничья!, запустите снова:)')
                    win = False
                elif resp == 'Ножницы' and var_rnd == 'Ножницы':
                    print('Ничья!, запустите снова:)')
                    win = False
                elif resp == 'Камень' and var_rnd == 'Камень':
                    print('Ничья!, запустите снова:)')
                    win = False
                else:
                    print('Вы проиграли:( Попробуйте еще!')
                    win = False