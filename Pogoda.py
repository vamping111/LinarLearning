import pyowm
city = input('Какой город вас интересует? ')
owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75',language='ru')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print ("В городе " + city+ " сейчас температура: "+ str(temperature) + " по Цельсию.")
print ("Так же, в указанном городе: " + w.get_detailed_status())
