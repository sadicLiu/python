class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地%.2f" % (self.name, self.area)


class House:

    def __init__(self, describe, area):
        self.describe = describe
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("%s 占地%.2f[剩余%.2f]\n家具列表：%s"
                % (self.describe, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        if item.area > self.free_area:
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("席梦思", 4.0)
table = HouseItem("餐桌", 8.2)

home = House("两室一厅", 60)
home.add_item(bed)
home.add_item(table)

print(home)