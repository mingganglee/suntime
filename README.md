# sunrise and sunset by gps

- [Calculate sunrise and sunset times for a given GPS](https://stackoverflow.com/a/39867990)
- [Sunrise/Sunset Algorithm](https://edwilliams.org/sunrise_sunset_algorithm.htm)

## Example

run.py 是使用 sun.py 进行计算并返回结果

- 不同时区修改 timezone 来使用

```bash
python3 run.py

Output:
sunrize 06:58:51
sunset  17:57:32
```

astral_run.py 是使用 astral 库, 进行计算并返回结果

```bash
python3 astral_run.py

Output:
Information for Beijing/China
Timezone: Asia/Harbin
Latitude: 39.79; Longitude: 116.44

Sunrise: 2023-02-22 06:58:43.725918+08:00
Sunset:  2023-02-22 17:57:26.458738+08:00
```
