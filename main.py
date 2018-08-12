import time
import sys
import wget
from prettytable import PrettyTable
from termcolor import colored
def main():
    true=0
    formats=["22","18","43"]
    a = input("введите id видео:  ")
    if a=="" :
        print(colored("Вы ничего неввели!Закрытие...", 'yellow'))
        time.sleep(2)
        sys.exit()
    b = input("Ведите id качества:  ")
    for i in range(len(formats)):
        if b==formats[i]:
            true+=1
    if true==0:
        print(colored("Неверный формат!Закрытие...", 'yellow'))
        time.sleep(2)
        sys.exit()
    else:
        url = "http://saveyoutube.ru/download/?video=" + a + "&format=" + b
        print(colored("Загрузка началась", 'green'))
        file = wget.download(url)
        print(colored("Загрузка закончалась. "
                      "Файл сохранён в папке со скриптом!", 'green'))
answer=None
table = PrettyTable(["!ВНИМАНИЕ!"])
table.add_row(['ВЫ скачиваете файл на свой страх и риск!'])
table.add_row(['Автор не несёт ответсвенность'])
table.add_row(['Если ВЫ согласны,то нажмите y,если нет то n,затем ENTER'])
table.add_row(['Пример id видео:https://youtu.be/T7K0pZ9tGi4,T7K0pZ9tGi4-это id'])
table.add_row(['Список id качеств видео:'
               '720p=22;'
               '360p=18;'
               'webm360p=43'])
table.reversesort = True
print(colored(table, 'red'))
answer=input("Ответ:")
if answer=='y':
    main()
elif answer=='n':
    print(colored("Закрытие...", 'yellow'))
    time.sleep(2)
    sys.exit()
else:
    print(colored("ВЫ ввели неправильно или ничего", 'green'))
    time.sleep(2)
    sys.exit()




