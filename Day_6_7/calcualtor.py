# Define a Function
def add(a,b):
    return a+b   # return their sum


add(10,90)    # Calling add function with 10 and 90 as arguments. The return value is not stored in any variable and not printed in the console


resAdd = add(10,90)  # Calling add function with 10 and 90 as arguments. The return value is stored in resAdd variable and printed in the console
print("Addition of 2 Numbers is " + str(resAdd))


def sub(a,b):
    return a-b
subRes = sub(5,3)
print ("Subtraction of 2 Numbers is " + str(subRes))

def mul(a,b):
    return a*b
mulRes = mul(5,3)
print ("Multiplication od 2 Numbers is "+ str(mulRes))

def div(a,b):
    return a/b
divRes = div( 15,3)
print ("Division of 2 Numbers is "+ str(divRes))

#Assignment
# Try to give Input Numbers in the console and call the function to perform the calculation. For example :