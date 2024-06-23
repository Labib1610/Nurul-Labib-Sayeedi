Original_student_data = {
    'Emma': {'name': 'Emma', 'major': 'Computer Science', 'cgpa': 3.8, 'completed_credits': 90},
    'Daniel': {'name': 'Daniel', 'major': 'Electrical Engineering', 'cgpa': 3.5, 'completed_credits': 75},
    'Sophia': {'name': 'Sophia', 'major': 'Mechanical Engineering', 'cgpa': 3.2, 'completed_credits': 60}
}

empty1 = {}
empty2 = {}

for student in Original_student_data.values():
    empty2 = {}
    empty2['cgpa'] = student['cgpa']
    empty2['completed_credits'] = student['completed_credits']
    empty1[student['name']] = empty2

print(empty1)