result = {}
with open('task_6.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    for line in content:
        line_s = line.split()
        hours = 0
        for el in line_s[1:]:
            num = '0'
            for i in el:
                if i.isdigit():
                    num += i
                else:
                    break
            hours += int(num)

        result.update({line_s[0]: hours})

print(result)
