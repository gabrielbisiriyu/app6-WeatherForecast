import requests
key="MY_KEY"



def Get_Data(place="london",days=1): 

    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}&units=metric&cnt={8*days}"

    response=requests.get(url) 
    data=response.json() 

    LISTS=data["list"][:]  
    temps=[]
    dates=[] 
    clouds=[] 
    for LIST in LISTS:
        temp=LIST["main"]["temp"] 
        cloud=LIST["weather"][0]["main"] 
        date=LIST["dt_txt"]
        temps.append(temp)
        dates.append(date)
        clouds.append(cloud)
         
    weather_data=[temps,dates,clouds]
    return weather_data

if __name__=="__main__":
    data=Get_Data("ijebu-igbo",days=1)
    print(data[1])


