def add(num1,num2):
   return num1 + num2
def subtract (num1,num2):
   return num1 - num2
def multiply  (num1,num2):
   return num1 * num2
def divide  (num1,num2):
   if num2 ==0:
      return 'Error: Cannot divide by zero!'
   return num1 / num2
calculator ={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
    }
def calculate(num1='',operation='',num2=''):
    """
    Performs basic arithmetic operations (+, -, *, /) on two numbers.
    
    Parameters:
    num1 (str/float): The first number.
    operation (str): The operator symbol.
    num2 (str/float): The second number.
    
    Returns:
    int/float/str: The calculated result, formatted cleanly, or an error message.
    """
    if  '' in [num1,num2, operation] :
        return ('Please enter the first number, the operation , and the second number.  ')
    else:
      try:
        n1=float(num1)
        n2=float(num2)
        if operation in calculator:
            result = calculator[operation](n1, n2)
            #Safely check if the float result is a whole number (e.g., 5.0) to format it as an int
            if isinstance(result,float)and result.is_integer():
                return int(result)
            else:
                return result
        else:
            return 'Invalid Operation!'
      except ValueError:
        return 'Please enter valid numbers only!'
another_round='y'
while another_round=='y': 
   print('='*60)
   print(f"Calculate".center(60))
   print('='*60)
   user_inputs =[
   input('Please Enter First Number : ').strip(),
   input('"+" Or "-" Or "*" Or "/" : ').strip() ,
   input('Please Enter Second Number:  ').strip()]
   print(calculate(*user_inputs)) # 30
   another_round = input('Do you want to perform another calculation? (Press y to continue): ').strip().lower()
print('='*60)
print("Thank you for using the calculator!")