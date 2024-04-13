import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

if __name__ == "__main__":
    students = {}

    while True:
        info = input()
        if info == "end":
            break
        info = info.split(",")
        name = info[0]
        surname = info[1]
        index = info[2]
        subject = info[3]
        points = int(info[4]) + int(info[5]) + int(info[6])
        grade = None
        if points <= 50:
            grade = 5
        elif points <= 60:
            grade = 6
        elif points <= 70:
            grade = 7
        elif points <= 80:
            grade = 8
        elif points <= 90:
            grade = 9
        else:
            grade = 10

        if index in students:
            students[index][subject] = grade
        else:
            students[index] = {'name': f'{name} {surname}', subject: grade}

    for student, info in students.items():
        print(f'Student: {info["name"]}')
        for sub, grade in info.items():
            if sub == 'name':
                continue
            print(f'----{sub}: {grade}')
        print()
