import requests
import secrets

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

Temperature = Temp(GetJson(secrets.url)) #temperature in Warsaw
SpeedOfWind = WindSpeed(GetJson(secrets.url)) #speed of wind in Warsaw
DegreeOfWind = WindDegree(GetJson(secrets.url)) #degree of wind