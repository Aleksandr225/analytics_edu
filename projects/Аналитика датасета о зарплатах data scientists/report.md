```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
```


```python
df = pd.read_csv('salaries.csv')
df.head()

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
      <th>work_year</th>
      <th>experience_level</th>
      <th>employment_type</th>
      <th>job_title</th>
      <th>salary</th>
      <th>salary_currency</th>
      <th>salary_in_usd</th>
      <th>employee_residence</th>
      <th>remote_ratio</th>
      <th>company_location</th>
      <th>company_size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>132600</td>
      <td>USD</td>
      <td>132600</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>102000</td>
      <td>USD</td>
      <td>102000</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>260520</td>
      <td>USD</td>
      <td>260520</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>140280</td>
      <td>USD</td>
      <td>140280</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Machine Learning Engineer</td>
      <td>215000</td>
      <td>USD</td>
      <td>215000</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>



# Analysis of the Data Science, AI & ML Job Salaries in 2025 will be consist of several steps: 
1. Clearing the dataset 
    * Finding  and avoiding the blowouts
    * dropping unneeded columns

2. Experimental analysis 
    * find the least and most paid job, find the median salary
    * find the least and most paid location for DS
    * find the difference between experience_level in salary
    * define the change in salary for DS year by year 
    * define the affect of the employment_type and the salary level
    * find the correlation betweeb the salary and remote ratio

3. Visualise data
    * create dashboards for every result from part 2
4. hypothesis testing
    * h0: salary between exp_level is not very different
    * h1: the difference is significant



```python

df = df.drop(['salary_currency', 'salary'], axis=1)
df = df.drop_duplicates()

```


```python
df.head()
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
      <th>work_year</th>
      <th>experience_level</th>
      <th>employment_type</th>
      <th>job_title</th>
      <th>salary_in_usd</th>
      <th>employee_residence</th>
      <th>remote_ratio</th>
      <th>company_location</th>
      <th>company_size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>132600</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>102000</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>260520</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>140280</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Machine Learning Engineer</td>
      <td>215000</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe().round(2) # Max level of salary in usd looks like a blowout
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
      <th>work_year</th>
      <th>salary_in_usd</th>
      <th>remote_ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>66040.00</td>
      <td>66040.00</td>
      <td>66040.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2024.37</td>
      <td>151164.94</td>
      <td>24.68</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.73</td>
      <td>77440.95</td>
      <td>42.97</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2020.00</td>
      <td>15000.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2024.00</td>
      <td>96000.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2024.00</td>
      <td>138900.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2025.00</td>
      <td>190137.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2025.00</td>
      <td>800000.00</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
q_hi = df['salary_in_usd'].quantile(0.99)

df = df[df['salary_in_usd'] < q_hi] # clearing the blowout
mask = df['job_title'].str.contains('ai|data|ML', case=False)
filtered_df = df[mask]
filtered_df.head() # this is the df after the cleaning

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
      <th>work_year</th>
      <th>experience_level</th>
      <th>employment_type</th>
      <th>job_title</th>
      <th>salary_in_usd</th>
      <th>employee_residence</th>
      <th>remote_ratio</th>
      <th>company_location</th>
      <th>company_size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>132600</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2025</td>
      <td>MI</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>102000</td>
      <td>US</td>
      <td>100</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>260520</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Product Manager</td>
      <td>140280</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2025</td>
      <td>SE</td>
      <td>FT</td>
      <td>Data Scientist</td>
      <td>127000</td>
      <td>US</td>
      <td>0</td>
      <td>US</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>




```python
salary = filtered_df.groupby('job_title').aggregate({'salary_in_usd' : 'mean'})
salary = salary.reset_index()
salary.head(-1)
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
      <th>job_title</th>
      <th>salary_in_usd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AI Architect</td>
      <td>202126.815217</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AI Content Writer</td>
      <td>40506.666667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AI Data Engineer</td>
      <td>94444.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AI Data Scientist</td>
      <td>85704.400000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AI Developer</td>
      <td>138667.154839</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Sales Data Analyst</td>
      <td>60000.000000</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Software Data Engineer</td>
      <td>111627.666667</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Staff Data Analyst</td>
      <td>79917.000000</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Staff Data Scientist</td>
      <td>133000.000000</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Tech Lead Data</td>
      <td>68078.500000</td>
    </tr>
  </tbody>
</table>
<p>192 rows × 2 columns</p>
</div>




```python

min_salary = salary['salary_in_usd'].min()
min_row = salary[salary['salary_in_usd'] == min_salary].iloc[0]


max_salary = salary['salary_in_usd'].max()
max_row = salary[salary['salary_in_usd'] == max_salary].iloc[0]


print(f"Minimal job: {min_row['job_title']}, salary: {min_row['salary_in_usd']}\n")
print(f"Max job: {max_row['job_title']}, salary: {max_row['salary_in_usd']}\n")
print(f"Median salary: {salary['salary_in_usd'].median()}")

```

    Minimal job: AI Engineering Lead, salary: 23649.0
    
    Max job: Data Science Tech Lead, salary: 375000.0
    
    Median salary: 115000.0
    


```python
loc = ds.groupby('company_location').aggregate({'salary_in_usd' : 'mean'})

plt.figure(figsize=(17,5))
plt.bar(loc.index, loc['salary_in_usd'], width=0.3, color='green', alpha=0.7)
plt.grid()
plt.ylabel('Salary in usd')
plt.xlabel('Country')
plt.title('Anual salary by country')
```




    Text(0.5, 1.0, 'Anual salary by country')




    
![png](DS_salary_files/DS_salary_9_1.png)
    



```python
ds = filtered_df[filtered_df['job_title'] == 'Data Scientist']
levels = ds.groupby('experience_level').aggregate({'salary_in_usd': 'mean'}).sort_values('salary_in_usd')

```


```python
import seaborn as sns
EN = ds[ds['experience_level'] == 'EN']['salary_in_usd']
MI = ds[ds['experience_level'] == 'MI']['salary_in_usd']
SE = ds[ds['experience_level'] == 'SE']['salary_in_usd']
EX = ds[ds['experience_level'] == 'EX']['salary_in_usd']

data = [EN, MI, SE, EX]
labels = ['EN', 'MI', 'SE', 'EX']

fig, ax = plt.subplots(figsize=(8,6))
box = ax.boxplot(data, labels=labels, patch_artist=True)

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Annual Salary by Experience Level')
ax.set_ylabel('Annual Salary (USD)')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

```

    C:\Users\HONOR\AppData\Local\Temp\ipykernel_17984\2668633297.py:11: MatplotlibDeprecationWarning: The 'labels' parameter of boxplot() has been renamed 'tick_labels' since Matplotlib 3.9; support for the old name will be dropped in 3.11.
      box = ax.boxplot(data, labels=labels, patch_artist=True)
    


    
![png](DS_salary_files/DS_salary_11_1.png)
    



```python
chang= ds.groupby(['work_year', 'experience_level']).aggregate({'salary_in_usd' : 'mean'})
chang = chang.reset_index()
chang.head(20)
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
      <th>work_year</th>
      <th>experience_level</th>
      <th>salary_in_usd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020</td>
      <td>EN</td>
      <td>54983.333333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020</td>
      <td>EX</td>
      <td>312500.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020</td>
      <td>MI</td>
      <td>73901.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020</td>
      <td>SE</td>
      <td>117466.250000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021</td>
      <td>EN</td>
      <td>65828.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2021</td>
      <td>EX</td>
      <td>138380.000000</td>
    </tr>
    <tr>
      <th>6</th>a
      <td>2021</td>
      <td>MI</td>
      <td>82352.625000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2021</td>
      <td>SE</td>
      <td>115659.375000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2022</td>
      <td>EN</td>
      <td>73392.517241</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2022</td>
      <td>EX</td>
      <td>181931.200000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2022</td>
      <td>MI</td>
      <td>101145.662162</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2022</td>
      <td>SE</td>
      <td>157269.840909</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2023</td>
      <td>EN</td>
      <td>93095.232143</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2023</td>
      <td>EX</td>
      <td>211668.100000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2023</td>
      <td>MI</td>
      <td>127124.965854</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2023</td>
      <td>SE</td>
      <td>173295.564593</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2024</td>
      <td>EN</td>
      <td>103441.508929</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2024</td>
      <td>EX</td>
      <td>199817.878378</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2024</td>
      <td>MI</td>
      <td>138496.654611</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2024</td>
      <td>SE</td>
      <td>168407.442559</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt

# Правильное разделение по уровням опыта
en = chang[chang['experience_level']=='EN']
mi = chang[chang['experience_level']=='MI']
se = chang[chang['experience_level']=='SE']
ex = chang[chang['experience_level']=='EX']

plt.figure(figsize=(8,6))


plt.plot(en['work_year'], en['salary_in_usd'], label='EN')
plt.plot(mi['work_year'], mi['salary_in_usd'], label='MI')
plt.plot(se['work_year'], se['salary_in_usd'], label='SE')
plt.plot(ex['work_year'], ex['salary_in_usd'], label='EX')

plt.xlabel('Work Year')
plt.ylabel('Salary in USD')
plt.title('Salary vs Work Year by Experience Level')
plt.legend()
plt.grid()
plt.show()

```


    
![png](DS_salary_files/DS_salary_13_0.png)
    



```python
et = ds.groupby(['employment_type']).aggregate({'salary_in_usd':'mean'})
et.head()
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
      <th>salary_in_usd</th>
    </tr>
    <tr>
      <th>employment_type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CT</th>
      <td>111009.842105</td>
    </tr>
    <tr>
      <th>FL</th>
      <td>60500.000000</td>
    </tr>
    <tr>
      <th>FT</th>
      <td>150654.270456</td>
    </tr>
    <tr>
      <th>PT</th>
      <td>90011.921053</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(6,7))

plt.bar(et.index, et['salary_in_usd'], width=0.4, color='blue', alpha=0.6)
plt.ylabel('Average salary')
plt.xlabel('Type of employment')
plt.title('avg salary by ET')
plt.grid()
```


    
![png](DS_salary_files/DS_salary_15_0.png)
    



```python

x = np.array(ds['salary_in_usd']) - ds['salary_in_usd'].mean()
y = np.array(ds['remote_ratio']) - ds['remote_ratio'].mean()

cov = (x*y).sum()/(ds.shape[0]-1)
rx = cov/(np.array(ds['salary_in_usd']).std()*np.array(ds['remote_ratio']).std())

print(rx)
```

    0.002701739086308406
    


```python
lev = ds.groupby(['experience_level'])['salary_in_usd'].agg(['mean', 'count', 'std'])
lev = lev.reset_index()
lev.head()

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
      <th>experience_level</th>
      <th>mean</th>
      <th>count</th>
      <th>std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>EN</td>
      <td>98310.986166</td>
      <td>506</td>
      <td>48498.128989</td>
    </tr>
    <tr>
      <th>1</th>
      <td>EX</td>
      <td>195264.584615</td>
      <td>195</td>
      <td>71155.155563</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MI</td>
      <td>130304.380771</td>
      <td>2361</td>
      <td>59515.750335</td>
    </tr>
    <tr>
      <th>3</th>
      <td>SE</td>
      <td>167654.492667</td>
      <td>3682</td>
      <td>64472.654044</td>
    </tr>
  </tbody>
</table>
</div>




```python


lev = ds.groupby(['experience_level'])['salary_in_usd'].agg(['mean', 'count', 'std']).sort_values('mean')
lev = lev.reset_index()
lev.head()

y = np.array(lev['mean'])

se = (np.array(lev['std'])/(np.sqrt(np.array(lev['count']))))*2.58


plt.errorbar(lev['experience_level'], y, yerr=se, fmt='o', capsize=5, label='Data with CI')
plt.xlabel('exp_level')
plt.ylabel('salary')
plt.grid()
plt.show() # H0 is incorrect

```


    
![png](DS_salary_files/DS_salary_18_0.png)
    

