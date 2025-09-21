import requests

def get_students(course, token):
    headers = {
        "authorization": f"Bearer {token}",
    }
    students = []

    for i in range(1, 4):
        students_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/students/?page={i}&page_size=15"

        students_data = requests.get(students_url, headers=headers)

        if students_data.status_code == 200:
            data = students_data.json()
            for student in data["results"]:
                students.append(f"{student['firstName']} {student['lastName']}")
        else:
            print("Ошибка:", students_data.status_code, students_data.text)
            return
    return students

def get_student_by_id(course, student, token):
    headers = {
        "authorization": f"Bearer {token}",
    }
    student_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/students/{student}"

    student_data = requests.get(student_url, headers=headers)
    if student_data.status_code == 200:
        data = student_data.json()
        student_name = f"{data["firstName"]} {data["lastName"]}"
    else:
        print("Ошибка:", student_data.status_code, student_data.text)
        return
    return student_name
