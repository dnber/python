num=[1,2,3,4,5,6,7,8,9,10]
def check(x):
    if int(x)%3==0:
        return x
num=list(filter(check,num))
print(num)