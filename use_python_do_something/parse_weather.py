#!/usr/bin/env python

from xml.parsers.expat import ParserCreate
from datetime import datetime, timedelta

class WeatherSaxHandle(object):
    """WeatherSaxHandle handler"""
    def __init__(self):
        self._weather = {}

    def start_elements(self, name, attrs):
        """start_elements"""
        if name == 'yweather:location':
            self._weather['city']=attrs['city']
            self._weather['country']=attrs['country']
        elif name == 'yweather:condition':
            selt._weather['condition']=attrs
        elif name == 'yweather:forecast':
            self._weather[attrs['date']]=attrs

    def end_elements(self, name):
        pass
    def char_data(self, text):
        pass


def parse_weather(data):
    handler = WeatherSaxHandle()
    parse = ParserCreate()
    parse.StartElementHandler = handler.start_elements
    parse.EndElementHandler = handler.end_elements
    parse.CharacterDataHandler = handler.char_data
    parse.Parse(data)

    Dweaher = {}
    Dweaher['today'] = {}
    Dweaher['tomorrow'] = {}

    condition = handler._weather['condition']['date'].split(',')[1].srip().split(' ')
    today = condition[0] + ' ' + condition[1] + ' ' + condition[2]
    tomorrow=datetime.strptime(today, '%d %b %Y') + timedelta(days=1)
    Dweather['city'] = handler._weather['city']
    Dweather['country'] = handler._weather['country']
    Dweather['today']['text'] = handler._weather[today]['text']
    Dweather['today']['low'] = handler._weather[today]['low']
    Dweather['today']['high'] = handler._weather[today]['high']

    Dweather['tomorrow']['text'] = handler._weather[tomorrow.strftime('%d %b %Y')]['text']
    Dweather['tomorrow']['low'] = handler._weather[tomorrow.strftime('%d %b %Y')]['low']
    Dweather['tomorrow']['high'] = handler._weather[tomorrow.strftime('%d %b %Y')]['high']

    return Dweather

if __name__ == '__main__':
    data = input('input xml')
    print(parse_weather(data))

