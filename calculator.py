def add(a, b):
    return a + b

def subtract(a, b):
   return a - b

if __name__ == "__main__":
    a = 5
    b = 3
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")