import csv


class Cate:
    def __init__(self, cate_en, cate_name):
        self.cate_en = cate_en
        self.cate_name = cate_name


with open('files/category_20210331.csv', newline='', encoding="utf-8-sig", ) as csvfile:

    rows = csv.reader(csvfile)
    cate_list = []
    for row in rows:
        cate_list.append(Cate(row[0], row[1]))
        print(row, row[0], row[1])

print(cate_list)