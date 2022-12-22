countries_dict = dict()
countries_dict = {}
print(countries_dict)

countries_dict = {"Россия":"Москва", "Белоруссия":"Минск"}
print(countries_dict)

countries_dict = dict.fromkeys(["Россия", "Белоруссия"], "")
print(countries_dict)

# ключ - строка
# пример словаря: ключ - страна, значение - столица
countries_dict = {
	"Россия":"Москва",
	"Белоруссия":"Минск",
	"Германия":"Берлин",
	"Франция":"Париж"
}
# узнать столицу выбранной страны:
print(countries_dict["Россия"])
# добавить новую страну:
countries_dict["Турция"] = "Анкара"

# вывести информацию страна-столица:
for country in countries_dict:
	print(country, countries_dict[country])
	
# вывести информацию страна-столица более простым способом:
for country, city in countries_dict.items():
	print(country, city)
	
# получить все ключи словаря (все страны):
keys = countries_dict.keys()
print(type(keys))
print(keys)
keys_list = list(keys)
print(keys_list)

# получить все значения словаря (все столицы):
values = countries_dict.values()
print(type(values))
print(values)
print(list(values))

# получить все пары страна-столица
items = countries_dict.items()
print(type(items))
print(items)
print(list(items))

# опасные места словарей
# если такого ключа в словаре нет, код будет падать
# print(countries_dict["Турция"])
# чтобы этого не случилось, необходимо сначала проверить, есть ли такой ключ:
if "Турция" in countries_dict.keys():
	print(countries_dict["Турция"])
else:
	print("Нет такого ключа")
# либо использовать безопасное получение значения.
# если такого ключа нет, вернется None
print(countries_dict.get("Турция"))

# добавить значение в словарь:
# countries_dict["Турция"] = "Анкара"
countries_dict.setdefault("Турция", "Анкара")

# удалить значение из словаря:
# del countries_dict["Турция"]
# val = countries_dict.pop("Турция")
# print(val)

# объединить два словаря через update
# пусть мы пока не определились со столицей Турции:
countries_dict["Турция"] = ""
print(countries_dict)
# словарь стран, с которым будем объединять:
countries2_dict = {
	"Великобритания":"Лондон",
	"Индия":"Нью-Дели",
	"Турция":"Анкара"
}
countries_dict.update(countries2_dict)
print(countries_dict)
