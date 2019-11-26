
# input=input("Enter answer")
#
# def if_yes_fun(input):
#
#     if input.lower() == 'yes':
#          print("correct")
#
#     else:
#          print("Wrong")
#
# if_yes_fun(input)

# firstNo=int(input("Enter a number"))
# secNo=int(input("Enter a second number"))
# thirdNo=int(input("Enter a  third number"))
#
# def largestNum(firstNo,secNo,thirdNo):
#         if(firstNo>secNo) and (firstNo>thirdNo):
#             print('The largest no is {}'.format(firstNo))
#
#         elif(secNo>firstNo) and (secNo>thirdNo):
#             print('The largest no is {}'.format(secNo))
#         elif(thirdNo>firstNo)and(thirdNo>secNo):
#             print('The largest no is {}'.format(thirdNo))
# largestNum(firstNo,secNo,thirdNo)

a=[8,9,8,78,987,78]

def picklastandFirst(a):
    l=a[0]
    f=a[-1]
    result=print(("first value is",l)+ ("last val is ",f))
    return result
picklastandFirst(a)

myDict={
    "Name":"stan",
    "age":34
}
bl=[]
for each in myDict.items():
    c=list(each)
    bl.append(c)
print(bl)


profit={
    "cost_price":32.67,
    "sell_price":45.00,
    "inventory":1200
}
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# })
def cal_profit(profit):
    profit=(profit['sell_price']-profit['cost_price'])*profit['inventory']
    return profit
prof=(cal_profit(profit))
print("%.2f"%prof)