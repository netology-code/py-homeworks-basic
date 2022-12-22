# вопрос: чем плоха эта структура данных?
# ответ: сложно догадаться, что означают ключи и что - значения
# по сути, сами ключи - на самом деле не ключи, а тоже значения
countries_dict = {
	"Россия":["Москва", "Санкт-Петербург", "Клин"],
	"Белоруссия":["Минск", "Гомель"],
	"Германия":["Берлин", "Дюссельдорф", "Мюнхен"],
	"Франция":["Париж", "Страсбург"]
}

# поэтому при проектировании структур данных ключ своим названием поясняет, что за данные должны в нем находиться

# КЕЙС: Сравним курсы Нетологии по программированию
# исходные данные взяты отсюда:
# https://netology.ru/programs/python#/experts
# https://netology.ru/programs/java-developer#/experts
# https://netology.ru/programs/fullstack-python-dev#/experts
# https://netology.ru/programs/front-end#/experts

# вспомним исходные данные с лекции про множества
# у нас был список курсов и список преподавателей с них
courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# а теперь давайте спроектируем типовое описание курса так, чтобы все уместилось в одной структуре данных и подходило для каждого курса:
course_dict = {
	"title": "Название курса",
	"mentors": []
}
# вот так будет выглядеть курс по Python:
py_course_dict = {
	"title": "Python-разработчик с нуля",
	"mentors": ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"]
}

# все остальные курсы будут иметь такую же структуру
# но мы говорили, что ключи в словаре должны быть уникальны. то есть не может быть два title или два mentors
# в таких случаях создаются СПИСКИ СЛОВАРЕЙ, где каждый словарь не зависит от других
courses_list = []
for course, mentor in zip(courses, mentors):
	course_dict = {"title": course, "mentors":mentor}
	courses_list.append(course_dict)

from pprint import pprint
pprint(courses_list)

# например, первый курс в списке:
pprint(courses_list[0])

# сколько всего курсов:
print(f"Всего у нас {len(courses_list)} курсов")
# перечислим названия наших курсов
for course in courses_list:
	print(course["title"])
# подсчитаем, сколько преподавателей на каждом из курсов:
for course in courses_list:
	title = course["title"]
	mentors_count = len(course["mentors"])
	print(f"На курсе {title} {mentors_count} преподавателей")

# пусть самый крутой курс - тот, на котором больше всего преподавателей. давайте найдем этот курс:
max_count = 0
course_id = None
for id, course in enumerate(courses_list):
	mentors_count = len(course["mentors"])
	if mentors_count > max_count:
		max_count = mentors_count
		course_id = id

title = courses_list[course_id]["title"]
print(f"Самый крутой курс {title}, потому что на нем {max_count} преподавателей")
