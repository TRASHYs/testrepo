def tri_check():
    result = None
    if s1< s2+s3 and s2< s1+s3 and s3< s2+s1:
        result = True
    else:
        result = False
    return result

s1 =int(input("Enter the first side :"))
s2 =int(input("Enter the second side :"))
s3 =int(input("Enter the third side :"))

if tri_check():
    print("Given sides will form a triangle .")
else:
    print("Triangle will not be formed using these sides .")
