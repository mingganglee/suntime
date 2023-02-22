from sun import Sun
import math
import datetime

coords = {'longitude' : 116.43802043961463, 'latitude' : 39.79066082241891 }

sun = Sun(date=datetime.date(2023, 2, 22))

timezone = 8
sunrise = (sun.getSunriseTime(coords)['decimal'] + timezone) % 24
sunset = (sun.getSunsetTime(coords)['decimal'] + timezone) % 24

sunrise_hour = math.floor(sunrise)
sunrise_minute = math.floor(60 * (sunrise - sunrise_hour))
sunrise_second = math.floor(60 * (60 * (sunrise - sunrise_hour) - sunrise_minute))

sunset_hour = math.floor(sunset)
sunset_minute = math.floor(60 * (sunset - sunset_hour))
sunset_second = math.floor(60 * (60 * (sunset - sunset_hour) - sunset_minute))


# Sunrise time UTC (decimal, 24 hour format)
print("sunrize {:02d}:{:02d}:{:02d}".format(sunrise_hour, sunrise_minute, sunrise_second))

# Sunset time UTC (decimal, 24 hour format)
print("sunset  {:02d}:{:02d}:{:02d}".format(sunset_hour, sunset_minute, sunset_second))
