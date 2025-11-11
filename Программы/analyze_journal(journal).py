
# Написать функцию analyze_journal(journal), которая:
#  1. Спрашивает у пользователя имя ученика.
#  2. Если такого ученика нет → «Ученика нет в журнале».
#  3. Если есть → выводит:
#  • список всех предметов и среднюю оценку по каждому,
#  • общую среднюю оценку по всем предметам.
#  4. Если средняя оценка ≥ 4.5 → «Отличник»,
# если ≥ 3 → «Хорошист»,
# иначе → «Нужно подтянуть учёбу»


мjournal = {
    "Алиса": {"математика": [5, 4, 5], "русский": [4, 4, 3]},
    "Бек": {"математика": [3, 2, 4], "русский": [5, 5, 5]},
    "Дана": {"математика": [5, 5, 5], "русский": [4, 5, 4]}
}

def analyze_journal(journal):
    name = input("Введите имя ученика: ")
    if name not in journal:
        print("Ученика нет в журнале")
        return
    subjects = journal[name]
    total_sum = 0
    total_count = 0
    for subject, grades in subjects.items():
        avg = sum(grades) / len(grades)
        print(f"{subject}: средняя оценка {avg:.2f}")
        total_sum += sum(grades)
        total_count += len(grades)
    overall_avg = total_sum / total_count
    print(f"Общая средняя оценка: {overall_avg:.2f}")
    if overall_avg >= 4.5:
        print("Отличник")
    elif overall_avg >= 3:
        print("Хорошист")
    else:
        print("Нужно подтянуть учёбу")

analyze_journal(мjournal)