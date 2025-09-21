import requests

def get_course_name(course, token):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    course_url = f"https://lms-admin.webium.ru/api/v2/staff/courses/{course}/"
    course_data = requests.get(course_url, headers=headers)
    if course_data.status_code == 200:
        course_name = course_data.json()["name"]
    else:
        print("Ошибка:", course_data.status_code, course_data.text)
        return
    return course_name