class ErrorEspecial(ZeroDivisionError):
    pass

def this_fails():    
    also_fails()

def notas():   
    try:
        raise TypeError('bad type')
    except Exception as e:
        x = 10
        e.add_note(f'Add some information {x*10}')
        e.add_note('Add some more information')
        raise

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

def also_fails():
    raise ErrorEspecial()

try:
    notas()
except ValueError as err:
    print('Atrapado en main', err)
   