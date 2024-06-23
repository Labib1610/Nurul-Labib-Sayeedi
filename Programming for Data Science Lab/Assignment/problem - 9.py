company_hr_register = {
101: {'name': 'Alice', 'age': 35,
'performance': 90, 'salary': 50000},
102: {'name': 'Bob', 'age': 58,
'performance': 98, 'salary': 70000},
103: {'name': 'Charlie', 'age': 45,
'performance': 85, 'salary': 60000},
104: {'name': 'David', 'age': 60,
'performance': 75, 'salary': 55000},
105: {'name': 'Eve', 'age': 28,
'performance': 92, 'salary': 48000},
106: {'name': 'Frank', 'age': 50,
'performance': 55, 'salary': 52000},
107: {'name': 'Grace', 'age': 62,
'performance': 97, 'salary': 75000},
}

updated_company_hr_register={}
total_employees = 0
total_bonus = 0
for i in company_hr_register:
    if company_hr_register[i]["age"]>=55 and company_hr_register[i]["performance"]>=90:
        updated_company_hr_register[i]={"name":company_hr_register[i]["name"]}
        total_employees+=1
    if company_hr_register[i]["age"]>55 :
        total_bonus+=10000
    if company_hr_register[i]["performance"]>95:
        total_bonus+=5000
    if company_hr_register[i]["performance"] < 60:
        continue
print(f'total_employees = {total_employees}')
print(f'total_bonus_amount = {total_bonus}')
print(updated_company_hr_register) 