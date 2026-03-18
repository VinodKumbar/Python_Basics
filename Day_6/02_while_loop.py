# While loop is used to execute a block of code repeatedly as long as a given condition is true.
# It is useful when the number of iterations is not known beforehand.

it = 0
while it <= 10:
    print(it)    # 0, 1 , 2 ................. 10
    it = it + 1
print("End of While loop")

print ("Print Even Number from 1 to 10 using While Loop")

iz = 0
while iz <= 10:
    if iz % 2 == 0:  #  0 % 2 = 0  || 1 % 2 = 0.111  || 2 % 2 = 0
        print("Print the even Number: " + str(iz))
    iz = iz + 1

print ("Print Even Number from 10 to 0 using While Loop")
ab = 10
while ab >= 0:
    if ab % 2 == 0:
        print("Print the even Number: " + str(ab))
    ab = ab - 1


print("Skip Printing 3 and 5 : " )
it = 0
while it <= 10:
    if it !=3 and it !=5:
     print("Print the Numbers skipping 3 and 5 : " + str(it))
    it = it + 1
print("End of While loop")


print ("Break Statement in While Loop")
it = 0
while it <= 10:
    if it >= 5:
        print("Breaking the loop at number : " + str(it))
        break
    print(it)
    it = it + 1
print("End of While loop")



