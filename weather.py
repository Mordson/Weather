import requests #importing requests library

url = 'https://api.openweathermap.org/data/2.5/weather?lat=52.23&lon=21.01&appid=f96032cf675ea0097f776d08a25c4819&units=metric&lang=pl&wind.direction.value'.format() #API url

def GetJson(url): #this function returns requests from API
    res = requests.get(url)
    response = res.json()
    return response

def Temp(respone): #this function returns temperature and speed of wind in Warsaw
    temp = respone['main']['temp'] #temperature in Warsaw
    return temp #returns temperature in Warsaw

def WindSpeed(response): #this function returns speed of wind in Warsaw
    WindSpeed = response['wind']['speed'] #speed of wind in Warsaw
    return WindSpeed #returns speed of wind in Warsaw

def WindDegree(response): #this function returns angle of wind in Warsaw
    Winddeg = response['wind']['deg'] #angle of wind in Warsaw
    return Winddeg #returns angle of wind in Warsaw

Temperature = Temp(GetJson(url)) #temperature in Warsaw
SpeedOfWind = WindSpeed(GetJson(url)) #speed of wind in Warsaw
DegreeOfWind = WindDegree(GetJson(url)) #degree of wind