# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
# Примечания:
# Можете выбрать не более 3-х библиотек для изучения.
# Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.


import requests
import pandas as pd
import matplotlib.pyplot as plt

###########
print('-----------------------------------------------------------------------')
url = 'https://yandex.ru'  # Указываем URL, на который будем отправлять GET-запрос

response = requests.get(url)

if response.status_code == 200:
    data = response.url
    print(f'Статус ответа: OK [код 200] по URL = {data}')
    response.encoding = 'utf-8'
    content = response.content
    print(f'Содержание : {content}')
    headers = response.headers
    print(f'Заголовки : {headers}')

else:
    print('Ошибка при выполнении запроса')

print('-----------------------------------------------------------------------')

##########
def analysis_data(df, column="0", list_value=None):
    global df_analysis
    if list_value is None:
        list_value = ['']
    len_df = len(df)
    print(df)
    if column == '0':
        print(
            f'Среднее значение зарплаты сотрудников от {list_value[0]} до {list_value[1]} года составляет {df['Salary'].mean():,.2f},\n '
            f'число сотрудников от {list_value[0]} до {list_value[1]} лет - {len_df}')
        print(
            f'Минимальное значение зарплаты сотрудников от {list_value[0]} до {list_value[1]} года составляет {df['Salary'].min():,.2f}, \n'
            f'Мaксимальное значение зарплаты сотрудников от {list_value[0]} до {list_value[1]} года составляет {df['Salary'].max():,.2f}, \n')
    else:
        min_sal = df['Salary'].min()
        mean_sal = df['Salary'].mean()
        max_sal = df['Salary'].max()
        str_df = {'Team': list_value[0], 'Min sal': min_sal, 'Mean sal': mean_sal, 'Max sal': max_sal,
                  'Quantity': len_df}
        df_analysis = df_analysis._append(str_df, ignore_index=True)
        print(
            f'Среднее значение зарплаты сотрудников команды {list_value[0]} составляет {mean_sal:,.2f},\n '
            f'число сотрудников команды {list_value[0]} - {len_df}')
        print(
            f'Минимальное значение зарплаты сотрудников команды {list_value[0]} составляет {min_sal:,.2f}, \n'
            f'Мaксимальное значение зарплаты сотрудников команды {list_value[0]} составляет {max_sal:,.2f}, \n')


# создаем data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
pd.options.display.float_format = '{:.2f}'.format
print(df.head(10))
new_row = pd.DataFrame({'Name': 'Andrey Ivanov', 'Team': 'S-Petersburg', 'Number': 3,
                        'Position': 'PG', 'Age': 28, 'Height': '6-2',
                        'Weight': 189, 'College': 'SPbPU', 'Salary': 11000000}
                       , index=[0])

df = pd.concat([new_row, df]).reset_index(drop=True)
print(df.head(10))

df_analysis = pd.DataFrame(columns=['Team', 'Min sal', 'Mean sal', 'Max sal', 'Quantity'])
list_teams = list(set(df.Team.tolist()))
cleanedList = [x for x in list_teams if str(x) != 'nan']
cleanedList_1 = sorted(cleanedList)
print(f'Список всех команд : {cleanedList_1}')

max_age = df['Age'].max()
min_age = df['Age'].min()
mean_age = round(df['Age'].mean())
print(f'Максимальный возраст сотрудников - {max_age}, минимальный - {min_age}')
# 
less_than_mean_age = df[df['Age'] <= mean_age]
analysis_data(less_than_mean_age, '0', [min_age, mean_age])
#
greater_than_mean_age = df[df['Age'] > mean_age]
analysis_data(greater_than_mean_age, '0', [mean_age, max_age])
#
for team in cleanedList_1:
    team_list = df[df['Team'] == team]
    analysis_data(team_list, '1', [team, ])

print(df_analysis)
#
df_analysis.plot(x='Team', y=['Min sal', 'Mean sal', 'Max sal'], kind="bar", fontsize=5)
plt.show()
#
df_new = df_analysis.groupby('Team')['Max sal'].sum().sort_values()
ax = df_new.plot.barh(x='Team', y='Max sal')
plt.show()
