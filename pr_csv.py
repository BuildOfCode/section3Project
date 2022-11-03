import requests
import pandas as pd

f = open('./After_gameslist.txt','r')
lines = f.readlines()
f.close()

df = pd.DataFrame()
df['name'] = []
df['price'] = []
df['average_forever'] = []
df['median_forever'] = []

for c, i in enumerate(lines):
    main_api = f"http://steamspy.com/api.php?request=appdetails&appid={i}"
    json_data = requests.get(main_api).json()
    li = [json_data['name'], json_data['price'], json_data['average_forever'], json_data['median_forever']]
    df.loc[c+1] = li

df = df.astype({'price':'float'})
df = df.astype({'average_forever':'float'})
df = df.astype({'median_forever':'float'})
df['price'] = df['price']*0.01
df['average_forever'] = round(df['average_forever']/60,1)
df['median_forever'] = round(df['median_forever']/60,1)
print(df.head())

df.to_csv("df.csv", mode='w')