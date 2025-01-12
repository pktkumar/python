try:
    val1 = int(input('enter first value '))
    va12 = int(input('enter second value '))
    result = val1/va12
    print(result)
except Exception as e:
    print('cant dive by zero ',e)
except ValueError:
    print("enter valid values ")