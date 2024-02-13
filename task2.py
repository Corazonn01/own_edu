main_dict = {
    'elina': {'age': 22,
              'name': 'Elina',
              'city': "Almaty",
              'girl': True,
              'hobbies': {'drawing': 'akrill', 'programming': 'python'},
              'future_job': 'AI',
              'education': {'uni': 'kimep', 'major': 'bacs', 'year': 4},
              'salary': [567000, 1000000, 789000]
             },

    'dana': {'age': 21,
             'name': 'Dana',
             'city': "Almaty",
             'girl': True,
             'hobbies': {'studying': 'smm', 'watching': 'movies'},
             'future_job': 'marketing',
             'education': {'uni': 'kimep', 'major': 'bmkt', 'year': 4},
             'salary': [134000, 423000, 654000]
            },

    'alua': {'age': 20,
             'name': 'Alua',
             'city': "Astana",
             'girl': True,
             'hobbies': {'help': 'caring children', 'making': 'videos'},
             'future_job': 'accounting',
             'education': {'uni': 'kimep', 'major': 'bacta', 'year': 4},
             'salary': [1435000, 345000, 654000]
            }
}

# for i in main_dict:
#     print('my name is ' + main_dict[i]['name'])
#     print('my age is ' + str(main_dict[i]['age']) + ' my city is ' + main_dict[i]['city'])
for person in main_dict.values():
    mean_salary = sum(person['salary']) / len(person['salary'])
    print(f"Name: {person['name']}, Mean Salary: {mean_salary:.2f}")
    if mean_salary >= 500000:
        print('Your salary is high.')
    elif mean_salary >= 400000:
        print('Your salary is middle enough.')
    else:
        print('Your salary is low.')
