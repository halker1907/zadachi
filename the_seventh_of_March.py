N = int(input())
months = []

for i in range(N):
    months.append(input().split(".")[1])

months_count = dict()
for month in months:
    if month in months_count:
        months_count[month] += 1
    else:
         months_count[month] = 1
months_names = { 
    "01": "Январь",
    "02": "Февраль",
    "03": "Март",
    "04": "Апрель",
    "05": "Май",
    "06": "Июнь",
    "07": "Июль",
    "08": "Август",
    "09": "Сентябрь",
    "10": "Октябрь",
    "11": "Ноябрь",
    "12": "Декабрь",

}


#{"12": 2, "01": 1}
max_value = max(months_count.values())
for month in months_count:
    if  months_count[month] == max_value:
        print(months_names[month])