#import
import socket
import gc
import threading
import os
from colorama import Fore, Back, Style
from colorama import init
init()
# загруска клиента
print(Back.GREEN)
print("loanding")
port = 1024  # порт подключения
print("1:конект по ip")
print("2:выбор ip из фаила")
com = input("выбор конекта:")
# ввод ip сервера
if com == "1":
        ser = input("server:")
if com == "2":
        t = open('server.txt')
        ser = t.read()
        print(ser)
server = ser, + port
print(server)
def read_sok():
    while 1:
        data = sor.recv(8128)
        print(data.decode('utf-8'))
        gc.collect()
nic = 0
if os.path.isfile("niсk.txt"):
        nic = 1
print(Back.YELLOW)
if nic == 0:
        file = open("niсk.txt", "w+")
        alias = input("ваш ник:")  # Вводим наш ник
        file.write(alias)
        file.close()
if nic == 1:
        file = open("niсk.txt")
        alias = file.read()
        print("Сохранённый ник:" + alias)
        file.close()

sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'), server)  # Уведомляем
print(Back.GREEN)
print("connect to serwer")
poto = threading.Thread(target=read_sok)
poto.start()
while 1 :
        print(Back.CYAN)
        mensahe = input() # пользовательский ввод
        sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server) # отправака покетов данных
print(Back.RED)
print("critical error")
input()
