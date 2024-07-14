from time import sleep
from datetime import datetime
from threading import Thread


time_start = datetime.now()


def wite_words(word_count, file_name):
    for i in range(word_count):
        a = i + 1
        my_file = open(file_name, "a+", encoding='utf8')
        my_file.write(f'Какое-то слово № {a}\n'), sleep(0.1)
        my_file.close()


wite_words(10, 'example1.txt')
print('Завершилась запись в файл example1.txt')
wite_words(30, 'example2.txt')
print('Завершилась запись в файл example2.txt')
wite_words(200, 'example3.txt')
print('Завершилась запись в файл example3.txt')
wite_words(100, 'example4.txt')
print('Завершилась запись в файл example4.txt')
time_end = datetime.now()
time_file = time_end - time_start
print('Работа потоков ', time_file)


time_start = datetime.now()


def func(word_count, file_name):
    for i in range(word_count):
        a = i + 1
        my_file = open(file_name, 'a+', encoding='utf8')
        my_file.write(f'Какое-то слово № {a}\n'), sleep(0.1)
        my_file.close()


thr_odin = Thread(target=func(10, 'example5.txt'))
thr_dva = Thread(target=func(30, 'example6.txt'))
thr_tri = Thread(target=func(200, 'example7.txt'))
thr_hetyre = Thread(target=func(100, 'example8.txt'))

thr_odin.start()
thr_dva.start()
thr_tri.start()
thr_hetyre.start()

thr_odin.join()
print('Завершилась запись в файл example5.txt')
thr_dva.join()
print('Завершилась запись в файл example6.txt')
thr_tri.join()
print('Завершилась запись в файл example7.txt')
thr_hetyre.join()
print('Завершилась запись в файл example8.txt')

time_end = datetime.now()
time_file = time_end - time_start
print('Работа потоков ', time_file)


# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
#
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt,
# т.к. потоки работали почти одновременно.
