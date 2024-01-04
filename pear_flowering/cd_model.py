import requests
import pandas as pd
from io import StringIO


def cd(year, loc):
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
    filtered_df = df[(df.index >= start_date)]

    Tc = 5.4
    Hr = 272

    df_acd = filtered_df.copy()
    df_acd['acd'] = df_acd.apply(lambda col:
                         col['tavg'] - Tc if 0 <= Tc <= col['tmin'] <= col['tmax']
                         else ((col['tmax'] - Tc) / 2 if 0 <= col['tmin'] <= Tc <= col['tmax']
                               else (0 if 0 <= col['tmin'] <= col['tmax'] <= Tc
                                     else (0 if col['tmin'] <= 0 <= col['tmax'] <= Tc
                                           else ((col['tmax'] - Tc) / 2) if col['tmin'] <= 0 <= Tc <= col[
                             'tmax'] else 0))), axis=1)

    df_acd['cumsum_acd'] = df_acd['acd'].cumsum()
    result = df_acd[df_acd['cumsum_acd'] >= Hr].iloc[0]
    flowering_date = f'{int(result["year"])}-{int(result["month"])}-{int(result["day"])}'

    return flowering_date
