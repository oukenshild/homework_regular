from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("C:\\Users\\Данил Илюхин\\PycharmProjects\\Homework_regular\\phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contacts_list_updated = []
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
def names_moving():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(name_pattern, name_substitution, line).split())) == 3:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = re.sub(name_pattern, name_substitution, line).split()[2]
        elif len((re.sub(name_pattern, name_substitution, line).split())) == 2:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = ''
        elif len((re.sub(name_pattern, name_substitution, line).split())) == 1:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = ''
            column[2] = ''
    return


def phone_number_formatting():
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = phone_pattern.sub(phone_substitution, column[5])
    return


def duplicates_combining():
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]

    for contact in contacts_list:
        if contact not in contacts_list_updated:
            contacts_list_updated.append(contact)
    return contacts_list_updated


if __name__ == '__main__':
    names_moving()
    phone_number_formatting()
    duplicates_combining()

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("C:\\Users\\Данил Илюхин\\PycharmProjects\\Homework_regular\\phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_updated)
