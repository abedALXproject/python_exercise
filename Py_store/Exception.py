"""
try:
    meme = [1,2,3]
    print(meme[3])
except(IndexError, NameError)
except IndexError:
    print("err rong input try again....")
except:
    print("unknown entry....")
    
    
class DogNameError(Exception):
    def __init__(self):
        Exception.__init__(self, *args, **kwargs)
try:
    dogname = input("What is your dogs name : ")
        
    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("your dom enough that you cant spellcheck your name")
    
    
num1, num2 = input("Enter 2 values to divide : ").split()
try:
    quotien = int(num1) / int(num2)
        
    print("{} / {} = {}".format(num1, num2, quotient))
except ZeroDivisionError:
    print("you can’t divide by zero!")
        
else:
    print("You didn’t raise an exception")
    
finally:
    print("i execute no matter what")
    

    
try:
    myFile = open("inno.py", encoding="utf-8")

except FileNotFoundError as me:
    print("that file was not found")
    print(ex.args)
else:
    print("File :", myFile.read())
    myFile.close()
finally:
    print("Finished working with File")



class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for clss in [B, C, D]:
    try:
        raise clss()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
        """
    
try:
    raise Exception('spam', 'edds')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be                  # printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
