# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint
num = 2021

print('Введите 1, если хотите играть с человеком, 2 если с глупым ботом и 3 если с умным: ')
UserOption= int(input())


if UserOption == 1:
    while num > 0:
        print(f' Всего конфет {num }.Игрок 1 введите количество конфет:')
        player_1 = int(input())
        if player_1 > 28:
            player_1 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_1:
            num -= player_1
        else:
            print('Игрок 1 победитель')
            num = 0
            break
            
        print(f' Всего конфет {num }.Игрок 2 введите количество конфет:')
        player_2 = int(input())
        if player_2 > 28:
            player_2 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_2:
            num -= player_2
        else:
            print('Игрок 2 победитель')
            num = 0
            break
        print('Игрок 1 у вас осталось конфет:', num)

elif UserOption == 2:
    print('Игра с глупым ботом началась, пристегните ремни!')
    while num > 0:
        print(f' Всего конфет {num }.Игрок 1 введите количество конфет:')
        player_1 = int(input())
        if player_1 > 28:
            player_1 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_1:
            num -= player_1
        else:
            print('Игрок 1 победитель')
            num = 0
            break
            
        print(f' Всего конфет {num }.Глупый бот введите количество конфет:')
        player_2 = randint(1, 35) #бот
        print('Глупый Бот ввел конфет', player_2)
        if player_2 > 28:
            player_2 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_2:
            num -= player_2
        else:
            print('Глупый бот - победитель')
            num = 0
            break
        print('Игрок 1 у вас осталось конфет:', num)
else:
    print('Игра с умным ботом началась. Держите меня семеро!')

    while num > 0:
        print(f' Всего конфет {num }.Игрок 1 введите количество конфет:')
        player_1 = int(input())
        if player_1 > 28:
            player_1 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_1:
            num -= player_1
        else:
            print('Игрок 1 победитель')
            num = 0
            break
            
        print(f' Всего конфет {num }.Умный бот введите количество конфет:')
        SmartChoise = (num % 28) -1

        if SmartChoise<1:
            SmartChoise=1
        player_2 = SmartChoise #бот
        print('Умный Бот ввел конфет', player_2)
        if player_2 > 28:
            player_2 = 28
            print('Будет вычтено 28 конфет')
        
        if num > player_2:
            num -= player_2
        else:
            print('Умный бот - победитель')
            num = 0
            break
        print('Игрок 1 у вас осталось конфет:', num)
