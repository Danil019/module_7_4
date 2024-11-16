team1_num = int(input('Введите сколько участников в первой команде: '))
team2_num = int(input('Введите сколько участников во второй команде: '))
score_1 = int(input('Введите сколько очков у первой команды: '))
score_2 = int(input('Введите сколько очков у второй команды: '))
team1_time = float(input('Введите сколько времени потребовалось первой команде: '))
team2_time = float(input('Введите сколько времени потребовалось второй команде: '))
print('В команде Мастера кода участников: %(team1_num)s !' % {'team1_num': team1_num})
print('Итого сегодня в командах учасников: %(team1_num)s и %(team2_num)s' % {'team1_num': team1_num,
                                                                             'team2_num': team2_num})
print('Команда Мастера кода решила задач: {score_1}'.format(score_1 = score_1))
print('Команда Волшебники данных решила задач: {score_2}'.format(score_2 = score_1))
print('Мастера кода решили задачи за {team1_time} с !'.format(team1_time = team1_time))
print('Волшебники данных решили задачи за {team2_time} с !'.format(team2_time = team2_time))
time_total = team1_time + team2_time
tasks_total = score_1 + score_2
time_avg = round(time_total / tasks_total, 1)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
print(f'Команды решили {score_1} и {score_2} задач')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}!')