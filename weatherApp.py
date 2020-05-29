from urllib.request import urlopen
from threadsafe_tkinter import *

def get_weather(city):
    page = urlopen('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    text = page.read().decode('euckr')
    text = text[text.find(">"+city+"</a>"):]
    for i in range(5):
        text = text[text.find("<td>")+1:]
    start = 3
    end = text.find("</td>")
    tempV.set(u'온도 : '+text[start:end])
    print(text[start:end])

def refresh(*args):
    get_weather(cities.get())

root = Tk()
root.title('기상청 현재기온')
root.geometry('300x280+200+200')
Label(root, text = '도시 : ').pack(side = 'left')
city_list = ['서울', '부산','대구','울산','광주','포항','대전']
cities = StringVar()
cities.set(city_list[0])
cities.trace('w',refresh)
OptionMenu(root,cities,*city_list).pack(side='left')
tempV = StringVar()
tempV.set('온도: ')
Label(root, textvariable=tempV).pack(padx = 10,side='left')
Button(root, text='refresh', command = refresh).pack(pady=40,side = 'bottom')
root.mainloop()
