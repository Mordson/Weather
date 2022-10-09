import requests

url = 'https://api.openweathermap.org/data/2.5/weather?lat=52.23&lon=21.01&appid=f96032cf675ea0097f776d08a25c4819&units=metric&lang=pl&wind.direction.value'.format()

def GetJson(url): #this function returns requests from API
    res = requests.get(url)
    response = res.json()
    return response

def Temp(respone): #this function returns temperature and speed of wind in Warsaw
    temp = respone['main']['temp']
    return temp

def WindSpeed(response):
    WindSpeed = response['wind']['speed']
    return WindSpeed

def WindDegree(response):
    Winddeg = response['wind']['deg']
    return Winddeg

Temperature = Temp(GetJson(url)) #temperature in Warsaw
SpeedOfWind = WindSpeed(GetJson(url)) #speed of wind in Warsaw
DegreeOfWind = WindDegree(GetJson(url)) #degree of wind