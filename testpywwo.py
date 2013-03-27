from pywwo import *

if __name__ == "__main__":
    if internet_on() :
        #you need to change this to your own key.
        #you can get your own key from registering on WWO website
        if setKey("xkq544hkar4m69qujdgujn7w", "free"):
            weather = LocalWeather("shanghai")
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl

            print
            weather = LocalWeather("london", num_of_days=3)
            print len(weather.data.weather)
            today = weather.data.weather[0]
            tomorrow = weather.data.weather[1]
            twodayslater = weather.data.weather[2]
            print u"Today: %s, Max \u2103: %d, Min \u2103: %d, %s" %\
                (today.date, today.tempMaxC, today.tempMinC, today.weatherDesc)

            print
            for w in weather.data.weather:
                print u"Date: %s, Max \u2103: %d, Min \u2103: %d, %s" %\
                    (w.date, w.tempMaxC, w.tempMinC, w.weatherDesc)

            print
            print objectify.dump(tomorrow)

            print
        #you need to change this to your own key.
        #you can get your own key from registering on WWO website
        if setKey("w9ve379xdu8etugm7e2ftxd6", "premium"):
            weather = LocalWeather("new york")
            print
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl

            setKeyType("free")
            weather = LocalWeather("san francisco")
            print
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl
