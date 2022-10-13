"""
Первое задание:
1) Посчитать среднее по признаку кредитного рейтинга для ушедших клиентов
2) Посчитать средний возраст всех клиентов
3) Посчитать долю ушедших клиентов
4) Вывести идентификаторы клиентов, которые ушли от банка
"""
print('Задание 1')
users = [
         [15634602, 15647311, 15619304, 15701354],#'CustomerId'
         ['Hargrave', 'Hill', 'Onio', 'Boni'],#'Surname'
         [ 619, 608, 502, 699], #'CreditScore'
         ['Female', 'Female', 'Male', 'Female'], #'Gender'
         [ 42, 41, 42, 39], #'Age'
         [1, 0, 1, 0] #Exited(0 - не ушёл / 1 - ушёл)
         ]
credit_score_exited, exited_users = 0, []

for index in range(len(users[5])):
    if users[5][index] == 1:
        credit_score_exited += users[2][index]
        exited_users.append(users[0][index])


print(f'Среднее по признаку кредитного рейтинга для ушедших клиентов: {credit_score_exited / users[5].count(1)}')
print(f'Средний возраст всех клиентов {round(sum(users[4]) / len(users[4]))} год(a)')
print(f'Доля ушедших клиентов - {users[5].count(1) / len(users[5]) * 100}%')
print(f'Идентификаторы клиентов, которые ушли от банка:', *exited_users, sep=' | ')

"""
Второе задание:
Создать и вывести список с сылками на изображения
"""
print('Задание 2')
response = {'response': [{'id': 42565717,
                          'name': 'Python',
                          'screen_name': 'club42565717',
                          'is_closed': 0,
                          'type': 'group',
                          'members_count': 37319,
                          'activity': 'Открытая группа',
                          'photo_50': 'https://sun9-127.userapi.com/c845524/v845524906/1a71c2/A2r_4JtmiLQ.jpg?ava=1',
                          'photo_100': 'https://sun9-58.userapi.com/c845524/v845524906/1a71c1/2fBtsS0k8XY.jpg?ava=1',
                          'photo_200': 'https://sun9-50.userapi.com/c845524/v845524906/1a71c0/Kfo-eQIn0DU.jpg?ava=1'},

                         {'id': 3183750,
                          'name': 'Веб программист - PHP, JS, Python, Java, HTML 5',
                          'screen_name': 'php2all',
                          'is_closed': 0,
                          'type': 'page',
                          'members_count': 117833,
                          'activity': 'Программирование',
                          'photo_50': 'https://sun9-54.userapi.com/c626421/v626421613/941/HSj4ylRsk8k.jpg?ava=1',
                          'photo_100': 'https://sun9-5.userapi.com/c626421/v626421613/940/yKaZLxGShkY.jpg?ava=1',
                          'photo_200': 'https://sun9-49.userapi.com/c626421/v626421613/93f/2EygT_FJKWg.jpg?ava=1'}]}
photo_list = []

for index in range(len(response['response'])):
    photo_list.append([])
    photo_list[index].append(response['response'][index]['photo_50'])
    photo_list[index].append(response['response'][index]['photo_100'])
    photo_list[index].append(response['response'][index]['photo_200'])

print(photo_list)
