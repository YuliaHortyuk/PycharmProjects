import json

firms = {}
count = 0
income_sum = 0
with open('task_7.txt') as file:
    content = file.readlines()
    for line in content:
        line_s = line.split()
        income = float(line_s[2]) - float(line_s[3])
        firms.update({line_s[0]: income})
        if income > 0:
            count += 1
            income_sum += income

av_income = income_sum / count
list_info = [firms, {'average_income': round(av_income)}]

with open('list_info.json', 'w') as file:
    json.dump(list_info, file)

