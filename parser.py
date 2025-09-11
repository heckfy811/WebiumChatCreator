import requests

import config

def get_students(course):
    students = []
    for i in range(1, 4):
        students_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/students/?page={i}&page_size=15"
        course_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/"

        headers = {
            "authorization": config.JWT,
        }
        #TODO: .env для всего выше

        students_data = requests.get(students_url, headers=headers)
        course_data = requests.get(course_url, headers=headers)

        if students_data.status_code == 200 and course_data.status_code == 200:
            course_name = course_data.json()["name"]
            data = students_data.json()
            for student in data["results"]:
                students.append(f"{student['firstName']} {student['lastName']}")
        else:
            print("Ошибка:", students_data.status_code, students_data.text)
            return
    return course_name, students

get_students("1612")