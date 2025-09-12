import requests

import config

#TODO: довести до ума подтягивание токена
def get_access_token(refresh_token):
    token_url = "https://api.carrotquest.app/v3/auth/jwt/refresh"
    token_data = requests.post(
        token_url,
        json={"auth_token" : refresh_token}
    )
    if token_data.status_code == 200:
        access_token = token_data.json()["data"]["access"]
    else:
        print("Ошибка:", token_data.status_code, token_data.text)
        return
    return access_token

def get_students(course):
    headers = {
        "authorization": config.JWT,
    }
    students = []

    for i in range(1, 4):
        students_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/students/?page={i}&page_size=15"

        #TODO: .env для всех ссылок

        students_data = requests.get(students_url, headers=headers)

        if students_data.status_code == 200:
            data = students_data.json()
            for student in data["results"]:
                students.append(f"{student['firstName']} {student['lastName']}")
        else:
            print("Ошибка:", students_data.status_code, students_data.text)
            return
    return students

def get_course_name(course):
    headers = {
        "authorization": config.JWT,
    }
    course_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/"
    course_data = requests.get(course_url, headers=headers)
    if course_data.status_code == 200:
        course_name = course_data.json()["name"]
    else:
        print("Ошибка:", course_data.status_code, course_data.text)
        return
    return course_name

def get_student_by_id(course, student):
    headers = {
        "authorization": config.JWT,
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