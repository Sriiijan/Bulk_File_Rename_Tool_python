import os
path=input("Enter the Path(Enter a \ after the path) : ")
path=path.replace('\\','/')
print(path)
format=input("Enter the new file format : ")
new=input("Enter new file name type : ")

print(os.listdir(path))

def main():
    i=1
    for filename in os.listdir(path):
        new_name=path+new+str(i)+format
        old_name=path+filename
        os.rename(old_name,new_name)
        i+=1

main()
print("\ndone")
