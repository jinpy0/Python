def plus(a, b, *c):
	print(c)

# plus(1, 2, 3, 4, 5)

def args_test(**a):
	print(a)
	print("1st Value : {first}".format(**a))
	print("2nd Value : {second}".format(**a))
	print("3rd Value : {third}".format(**a))
	
# args_test(first = 1, second = 2, third = 3)

# a = 10
# b = 5
# print("%d + %d = %d"%(a, b , a+b))
 
# c = 4
# d = 8
# print("{} + {} = {}".format(c, d, c+d))

# e = 5
# f = 20
# print(f"{e} + {f} = {e+f}")

# color = ['red', 'blue', 'green', 'black', 'white', 'purple']
# print(color[0])
# print(color[0:3])
# print(color[:-2])
# print(color[-2:])

tuple = (1, 2, 3, 4)
# print(tuple)
# print(len(tuple))
# print(tuple * 2)
# print(tuple[0])
# tuple[0] = 5

# set = {'a', 'b', 'c', 'c', 'a'}
# print(set)

# dic = {1:"일진표", 2:"이진표", 3:"삼진표"}
# print(dic)
# dic[4] = "사진표"
# print(dic)

# a_list = ["일진표", "이진표", "삼진표"] # a_list에 요소들을 넣음 ( 패킹 )
# a, b, c = a_list # a_list에 있는 값을 변수 a, b, c에 언패킹
# print(a_list)
# print(a, b, c)

list_a = ["일진표", "이진표", "삼진표"]
for index, name in enumerate(list_a):
    print(f"{index} = {name}")

list = ["진표" for i in range(0,10)]
# print(list)
for index, name in enumerate(list):
    print(f"{index} : {name}")