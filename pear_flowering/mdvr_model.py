import requests
import pandas as pd
import numpy as np
from io import StringIO


def mdvr(year, loc):
    month = 2
    day = 15

    url = f'https://api.taegon.kr/station/{loc}/?sy={year}&ey={year + 1}&format=csv'
    response = requests.get(url)
    csv_data = response.content.decode('utf-8')
    df = pd.read_csv(StringIO(csv_data), skipinitialspace=True)

    df = df[['year', 'month', 'day', 'tavg', 'tmax', 'tmin']]
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    df.set_index('date', inplace=True)
    start_date = pd.Timestamp(year, month, day)
    df = df[(df.index >= start_date)]

    for hour in range(0, 24):
        if 0 <= hour <= 3:
            df[f'temp_{hour}h'] = (df['tmax'].shift(1) - df['tmin']) * (np.sin((4 - hour) * 3.14 / 30) ** 2) + df[
                'tmin']

        elif 4 <= hour <= 13:
            df[f'temp_{hour}h'] = (df['tmax'] - df['tmin']) * (np.sin((hour - 4) * 3.14 / 18) ** 2) + df['tmin']

        elif 14 <= hour <= 23:
            df[f'temp_{hour}h'] = (df['tmax'] - df['tmin'].shift(-1)) * (np.sin((28 - hour) * 3.14 / 30) ** 2) + df[
                'tmin'].shift(-1)

    for i in range(0, 24):
        df[f'temp_{i}h'] = df[f'temp_{i}h'].apply(
            lambda x: np.exp(35.27 - 12094 * (x + 273) ** -1) if x < 20 else np.exp(5.82 - 3474 * (x + 273) ** -1))

    df['cumsum_temp'] = df.loc[:, 'temp_0h':'temp_23h'].sum(axis=1)
    df['cumsum_dvr2'] = df['cumsum_temp'].cumsum()

    result = df[df['cumsum_dvr2'] >= 0.9593].iloc[0]
    flowering_date = f'{int(result["year"])}-{int(result["month"])}-{int(result["day"])}'

    return flowering_date
