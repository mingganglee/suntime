from astral import LocationInfo
import datetime
from astral.sun import sun

city = LocationInfo("Beijing", "China", "Asia/Harbin", longitude=116.43802043961463, latitude=39.79066082241891)
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))

s = sun(city.observer, date=datetime.datetime.now(), tzinfo=city.timezone)
print((
    # f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {(s["sunrise"])}\n'
    # f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    # f'Dusk:    {s["dusk"]}\n'
))
