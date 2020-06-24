class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


build1 = House("강남", "아파트", "매매", "10억", "2010년")
build2 = House("마포", "오피스텔", "전세", "5억", "2007년")
build3 = House("송파", "빌라", "월세", "500/50", "2000년")

# build1.show_detail()
# build2.show_detail()
# build3.show_detail()

build = []

build.append(build1)
build.append(build2)
build.append(build3)

for house in build:
    house.show_detail()

