# Выводы по датасету  **[Sleep_health_and_lifestyle](Sleep_health_and_lifestyle_dataset.csv)**

> Предварительный просмотр:

```
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
df = df.rename(columns={'Occupation': 'Job'})
df.head(3)

```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Job</th>
      <th>Sleep Duration</th>
      <th>Quality of Sleep</th>
      <th>Physical Activity Level</th>
      <th>Stress Level</th>
      <th>BMI Category</th>
      <th>Blood Pressure</th>
      <th>Heart Rate</th>
      <th>Daily Steps</th>
      <th>Sleep Disorder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>27</td>
      <td>Software Engineer</td>
      <td>6.1</td>
      <td>6</td>
      <td>42</td>
      <td>6</td>
      <td>Overweight</td>
      <td>126/83</td>
      <td>77</td>
      <td>4200</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>28</td>
      <td>Doctor</td>
      <td>6.2</td>
      <td>6</td>
      <td>60</td>
      <td>8</td>
      <td>Normal</td>
      <td>125/80</td>
      <td>75</td>
      <td>10000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Male</td>
      <td>28</td>
      <td>Doctor</td>
      <td>6.2</td>
      <td>6</td>
      <td>60</td>
      <td>8</td>
      <td>Normal</td>
      <td>125/80</td>
      <td>75</td>
      <td>10000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Проверка корреляции уровная стресса со сном по профессиям

```
df = df[(df['Age'] >= 27) & (df['Age'] <= 40)]
df_grouped = df.groupby('Job').aggregate({'Stress Level' : 'mean', 'Sleep Duration' : 'mean'})
df_grouped.head(11)

```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Stress Level</th>
      <th>Sleep Duration</th>
    </tr>
    <tr>
      <th>Job</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Accountant</th>
      <td>4.129032</td>
      <td>7.219355</td>
    </tr>
    <tr>
      <th>Doctor</th>
      <td>7.015385</td>
      <td>6.887692</td>
    </tr>
    <tr>
      <th>Engineer</th>
      <td>4.090909</td>
      <td>7.336364</td>
    </tr>
    <tr>
      <th>Lawyer</th>
      <td>5.033333</td>
      <td>7.280000</td>
    </tr>
    <tr>
      <th>Nurse</th>
      <td>6.000000</td>
      <td>6.757143</td>
    </tr>
    <tr>
      <th>Sales Representative</th>
      <td>8.000000</td>
      <td>5.900000</td>
    </tr>
    <tr>
      <th>Scientist</th>
      <td>7.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>Software Engineer</th>
      <td>6.000000</td>
      <td>6.750000</td>
    </tr>
    <tr>
      <th>Teacher</th>
      <td>5.000000</td>
      <td>6.900000</td>
    </tr>
  </tbody>
</table>
</div>

---------

### Визуализация


```
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.bar(df_grouped.index, df_grouped['Sleep Duration'], color='blue', alpha=0.7)
plt.bar(df_grouped.index, df_grouped['Stress Level'], color='red', alpha=0.5)
plt.title('Средняя продолжительность сна по профессиям и уровень стресса')
plt.xlabel('Профессия')
plt.ylabel('Средняя продолжительность сна (часов)')
plt.xticks(rotation=45, ha='right')

plt.show()
```
---


![alt text](image.png)

>> Можно сделать вывод, что наболее подвержены стрессу торговые, представители, а наименее инженеры и бухгалтеры. 

> Можно предположить, что это связано с тем, что данные профессии имеют наименьшую среднюю продолжительность сна.


# Проверим этот вывод и по другим параметрам



 