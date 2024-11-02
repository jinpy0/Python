def test1():
    for i in range(2,10,1):
        for j in range(1,10):
            # print("%d * %d = %d" %( i, j, i*j))
            # print("{} * {} = {}".format(i, j, i*j))
            print(f"{i} * {j} = {i*j}")
# test1()

# 시험문제
def test2():
    cities = ['서울', '부산', '인천', '대구', '대전', '광주' ,'울산', '수원']
    print(cities)
    print(cities[:])
    print(cities[:4])
    print(cities[:-4])
    print(cities[-4:])

test2()