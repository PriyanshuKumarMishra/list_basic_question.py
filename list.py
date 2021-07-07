#### prime , even and odd number #####

# l=int(input("How many input do you need :"))
# x=[]
# y=[]
# z=[]
# b=[]
# for p in range (l):
#     t=int(input("Enter the number :"))
#     x.append(t)
# for i in x:
#     if i > 1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             y.append(i)
# for h in x:
#     if h % 2 ==0:
#         z.append(h)
# for k in x:
#     if k % 2 ==1:
#         b.append(k)
# print("This is prime number", y)
# print("This is even number",z)
# print("This is odd number",b)




#### bubble sort #####


# a = [16, 19, 11, 15, 10, 12, 14]
# for j in range(len(a)):
#     b= False
#     i = 0
#     while i<len(a)-1:
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i] 
#             b= True
#         i = i+1
#     if b == False:
#         break 
# print (a)



##### palindrome using list #####

# a=list(input())
# b=[]
# for i in a[::-1]:
#     b.append(i)
# if a==b:
#     print("yes")
# else:
#     print("no")



### find which numbers are not present in the second array ###

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7] 
# for i in list2 :
#     for j in list1 :
#         if i == j :
#             list1.remove(j)
# print(list1)    


#### sum of nested list ####

#marks = [ [78, 76, 94, 86, 88], [91, 71, 98, 65, 76],[95, 45, 78, 52, 49] ] 
#b=0
#for i in marks:
#	for j in i:
#		b=j+b
#print(b)


###### sum of the list and average the list ######

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# for i in marks:
#     sum=0
#     for j in i:
#         sum=sum+j
#     av=sum/len(i)
#     print(sum)
#     print(round(av,2))




######## sum of odd number and sum of even ########

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# d=0
# e=0
# for i in elements:
#     if i % 2 == 1:
#         d+=i
#     else:
#         e+=i
# print("sum of odd number :",d)
# print("sum of even number :",e)


#### Total sum 30 ####

# number = 30
# a = [10, 11, 12, 13, 14, 17, 18, 19] 
# c=[]
# for i in a:
#     sum = 0
#     for j in a :
#         sum = i +j
#         if number == sum:
#             c.append([i,j])
#             a.remove(i)
#             a.remove(j)
# print(c)



#### find odd even number and sum of odd even number ####
#### and average of odd even number ####

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# b=[]
# c=[]
# d=0
# e=0
# for i in elements:
#     if i % 2 == 1 :
#         b.append(i)
#         d+=i        
#     else:
#         c.append(i)
#         e+=i
# print("odd number is :",len(b),b)
# print("even number is :",len(c),c)
# print("sum of odd number :",d)
# print("sum of even number :",e)
# r=d/len(b)
# s=e/len(c)
# print("average of odd number :",round (r,2))
# print("average of even number :",round (s,2))





####sum same indexing ka same indexing ke sath ####

# a=[23,45,67,87,98,90]
# b=[24,45,5,78,12,34]
# c=[]
# for i in a:
#     sum=0
#     for j in b:
#         sum= i+j  
#         b.remove(b[0]) 
#         break
#     c.append(sum)
# print(c)



#### Bubble short ####

# a=[23,45,56,12,21,13,14,54]
# b=[]
# for i in range(len(a)):
#     v=min(a)
#     a.remove(v)
#     b.append(v)
# print(b)



####  Write a Python program to multiplies all the items in a list. ####

# a=int(input())
# c=[]
# b=1
# for i in range (a) :
#     d=int(input())
#     c.append(d)
#     b=b*d
# print(b)


#### Write a Python program to get the largest number from a list. ####

# a=int(input())
# b=[]
# c=0
# for i in range (a):
#     d=int(input())
#     b.append(d)
# print(b) 
# for j in b:
#     if j > c:
#         c=j
# print(c)




#### Write a Python program to get the minium number from a list ####

# a=int(input())
# b=[]
# for i in range(a):
#     d= int(input())
#     b.append(d)
# print(b)
# c=b[0]
# for  j in b:
#     if j < c:
#         c=j
# print(c)



#### Write a Python program to count the number of ####
#### strings where the string length is 2 or more and the ####
#### first and last character are same from a given list of strings. ####

# a=int(input())
# b=[]
# for i in range (a):
#     c=input()
#     b.append(c)
# print(b)
# e=0
# for j in b:
#     if len(b)>2 and j[0]==j[-1]:
#         e+=1
# print(e)


##### remove duplicate items from list #####

# a=int(input())
# b=[]
# for i in range (a):
#     c=input()
#     b.append(c)
# d=[]
# for j in b:
#     if j not in d:
#         d.append(j)
# print(d)


##### print whose element not in the list end of the lenth #####

# a=[1,7,9,12]
# c=[]
# b=0
# while b < a[-1]:
#     if b not in a :
#         c.append(b)
#     b+=1
# print(c)



######## find maximum or second maximum number from list ##########

# a=[34,56738905,2234,3]
# b = a[0]
# c = a[0]
# for j in range (len(a)):
#     if a[j] > b:
#         c = b
#         b = a[j]
#     elif a[j] > c and a[j] < b:
#         c = a[j]
# print("maximum :", b,"\nsecond maximum :",c)




#### implement string ####

# def string(a,b):
#     for i in a:
    #         if b not in a:
    #             print(-1)
    #             break
    #     else:
    #         print(len(b))
    # a=input()
    # b=input()
    # string(a,b)






#### perfect number ####

# a=int(input())
# sum1=0
# c=[]
# for i in range (1,a):
#     if a%i==0:
#         sum1+=i
#         c.append(i)
# print(c)
# if a==sum1:
#     print("perfect number")
# else:
#     print("not perfect")


#### convert binary to decimal ####

# d=int(input())
# a=[]
# for j in range (d):
#     e=int(input())
#     a.append(e)
# c=0
# b=0
# for i in range(-1,-len(a)-1,-1):
#     c=a[i]*2**b+c
#     b+=1
# print(c)


############ find maximum and second maximum in the list #######

# a=[73,432345678905,2234,3,35,5789024,9,9,99999999,234,9]
# b = a[0]
# c = a[0]
# for j in range (len(a)):
#     if a[j] > b:
#         c = b
#         b = a[j]
#     elif a[j] > c and a[j] < b:
#         c = a[j]
# print("maximum :", b,"\nsecond maximum :",c)
