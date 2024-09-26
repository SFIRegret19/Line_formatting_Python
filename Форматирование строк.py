team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Использование %:
print('В команде Мастера кода участников: %s!' % (team1_num))
print('В команде Волшебники данных участников: %s!' % (team2_num))
print('Итого сегодня в командах участников: %(team1)s и %(team2)s!' % {'team1': team1_num, 'team2': team2_num})

# Использование format():
print('Команда Мастера кода решила задач: {}!'.format(score_1))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Мастера кода решили задачи за {time}c !'.format(time = team1_time))
print('Волшебники данных решили задачи за {time}c !'.format(time = team2_time))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Победа команды None!'
if score_1.__lt__(score_2):
    challenge_result = challenge_result.replace('None', team2_name)
elif score_1.__gt__(score_2):
    challenge_result = challenge_result.replace('None', team1_name)
else:
    print('Ничья')

print(challenge_result)

print(f'Сегодня было решено {tasks_total} задач, в среднем по {(team1_time+team2_time) / tasks_total} секунды на задачу!')