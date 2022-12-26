import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
contacts_list_new = []
for i in contacts_list:
    fio = (i[0].split() + i[1].split() + i[2].split())
    if len(fio) == 2:
        fio.append('')
    if len(fio) == 1:
        fio.append('')
        fio.append('')
    fio.append(i[3])
    fio.append(i[4])
    fio.append(i[5])
    fio.append(i[6])
    contacts_list_new.append(fio)

#определяем повторяющиеся имя и фамилию
check_dubles = []
for q in contacts_list_new:
    check_dubles.append(q[0:2])
dup = [x for i, x in enumerate(check_dubles) if i != check_dubles.index(x)]

#склеиваем два списка с одинаковым именем и фамилией
contacts_list_matched = []
for el in range(0, len(dup)):
    matched_list = []
    for w in contacts_list_new:
        if w[0:2] == dup[el]:
            matched_list.append(w)
            matched_tuple = tuple(matched_list)
    temp_list = []
    for k in range(0, len(matched_tuple[0])):
        if matched_tuple[0][k] != matched_tuple[1][k] and matched_tuple[0][k] == '':
            temp_list.insert(k, matched_tuple[1][k])
        elif matched_tuple[0][k] != matched_tuple[1][k] and matched_tuple[1][k] == '':
            temp_list.insert(k, matched_tuple[0][k])
        else:
            temp_list.insert(k, matched_tuple[0][k])
    contacts_list_matched.append(temp_list)

#определяем элементы до матчинга, которые нужно удалить
tt = []
for d in range(0, len(dup)):
    for i in contacts_list_new:
        if i[0:2] == dup[d]:
            tt.append(i)
for i in tt:
    contacts_list_new.remove(i)

#соединяем отредактированный и сматченный списки
contacts_list_final = contacts_list_new+contacts_list_matched

#приводим номера телефонов к единому виду
pattern = r"(\+7|8)?\s?\(?(\d+)[\)|-]?\s*(\d{3})-?(\d{2})-?(\d{2})(\s\(?(доб.)\s(\d+)\)?)?"
for i in contacts_list_final:
    i[5] = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8", i[5])

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_final)

