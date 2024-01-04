import requests
import pandas as pd
from io import StringIO


def dvr(year, loc):
    month = 1
    day = 30

    url = f'https://api.taegon.kr/station/{loc}/?sy={year}&ey={year + 1}&format=csv'
    response = requests.get(url)
    csv_data = response.content.decode('utf-8')
    df = pd.read_csv(StringIO(csv_data), skipinitialspace=True)

    df = df[['year', 'month', 'day', 'tavg', 'tmax', 'tmin']]
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    df.set_index('date', inplace=True)
    start_date = pd.Timestamp(year, month, day)
    filtered_df = df[(df.index >= start_date)]

    dvri_df = filtered_df.copy()
    dvri_df['dvri'] = dvri_df['tavg'].apply(lambda x: (1 / (107.94 * (0.9 ** x))) * 100 if x >= 5 else 0)
    dvri_df['dvs'] = dvri_df['dvri'].cumsum()

    result = dvri_df[dvri_df['dvs'] >= 100].iloc[0]
    flowering_date = f'{int(result["year"])}-{int(result["month"])}-{int(result["day"])}'

    return flowering_date
