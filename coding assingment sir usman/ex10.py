def if_even_or_odd(number):
    if number % 2 == 0:
        return ' Number is  even.'
    else:  
        return 'Number is odd.'     
                
def main():
    user_number = int(input('Enter your number.'))
    result = if_even_or_odd(user_number)
    print(result)


main()


