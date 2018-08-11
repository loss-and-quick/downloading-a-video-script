import sys
import wget
from prettytable import PrettyTable
from termcolor import colored
answer=None
table = PrettyTable(["!ВНИМАНИЕ!"])
table.add_row(['ВЫ скачиваете файл на свой страх и риск!'])
table.add_row(['Автор не несёт ответсвенность'])
table.add_row(['Если ВЫ согласны,то нажмите y,если нет то n,затем ENTER'])
table.add_row(['Пример id видео:https://youtu.be/T7K0pZ9tGi4,T7K0pZ9tGi4-это id'])
table.add_row(['Список id форматов:'
               '720p=22;'
               '360p=18;'
               'webm360p=43'])
table.reversesort = True
print(colored(table, 'red'))
answer=input("Ответ:")
if answer=='y':
    a=input("введите id видео:  ")
    b=input("Ведите id формата:  ")
    url = "http://saveyoutube.ru/download/?video=" + a + "&format=" + b
    print(colored("Загрузка началась", 'green'))
    filename = wget.download(url)
    print(colored("Загрузка закончалась. "
                  "Файл сохранён в папке со скриптом!", 'green'))
elif answer=='n':
    print(colored("Закрытие...", 'yellow'))
    sys.exit()
else:
    print(colored("ВЫ ввели неправильно или ничего", 'green'))





