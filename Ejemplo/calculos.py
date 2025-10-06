import sys
def suma(a,b):
    return f"a+b= {a+b}"
def resta(a,b):
    return f"a-b= {a-b}"


if __name__ == '__main__':
    print('No me ejecutes, ¡solo soy un modulo',end=" ")
    print(__name__)
    sys.exit(1)
else:
    print(__name__)