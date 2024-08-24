#python one.py
print('hello')


def func():
    print('Func in one.py')

print('top level in one.py')

#this tells you this python script is being run directly
if __name__ == "__main__":
    #run the script
    print('one.py is being run directly')
else:
    print('one.py has been imported.')