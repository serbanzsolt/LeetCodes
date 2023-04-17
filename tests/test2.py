# my_string = "    42"
# # my_string = my_string.split()
# print(my_string)
# my_string = my_string.replace(" ", "")
# my_string = list(my_string)
# print(my_string)
# print(type(my_string))
# my_string = "".join(my_string)
# my_string = int(my_string)
# print(type(my_string))
# print(my_string)

l1 = [0,1,2,3,4,5,6,7,8,9,]
l2 = [" ","a",3, 5]
l3 = ["x", "y", 5]

if any(element in l2 for element in l1 and l3):
    print("hi")

if not (any(element in l2 for element in l3 and l1)):
    print("hi")

# charlist = []
# print(chr(1_114_111))
# char_num = 97
# for i in range(0,26):
#     charlist.append(chr(char_num))
#     char_num += 1
    
# print(charlist)
# print(charlist.index("z"))

# chars = []
# for i in range(0, 1_114_111):
#     chars.append(chr(i))

# print(chars)
# print(chars.index("A"))
# print(chars.index("ݣ"))
# print(chars.index("Ő"))
# print(chars.index("ú"))
# print(chars.index("é"))
# print(chars.index("á"))
# print(chars.index("ű"))

list1 = ["x", "x", "x", "y"]
l2 = [item for item in list1 if item == "x"]
l3 = [item == "x" for item in list1[0:0]]
print(l3)
print(all([item == "x" for item in list1]))