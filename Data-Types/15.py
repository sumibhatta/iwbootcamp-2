#Write a Python function to insert a string in the middle of a string.
#Sample function and result :
#insert_sting_middle('[[]]<<>>', 'Python') 
# -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') 
# -> {{PHP}}
# one = '[[]]'
# print((len(one))//2)

def insert_sting_middle(one, two):
    print(one[0:len(one)/2]+two+one[len(one)/2:])
    

insert_sting_middle('[[]]<<>>', 'Python')
insert_sting_middle('{{}}', 'PHP')
insert_sting_middle("[[]]","yyy")