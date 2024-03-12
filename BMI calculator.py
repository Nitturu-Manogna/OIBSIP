print('Welcome to BMI calculator!!')
#inputs
weight=float(input('enter your weight in kilograms:'))
height=float(input('enter your height in meters:'))
#calculation
bmi=weight/(height**2)
print('BMI=',bmi)
#division into categories
if bmi<18.5:
    print('You are underweight')
elif bmi>=18.5 and bmi<25:
    print('You are normal')
elif bmi>=25 and bmi<30:
    print('Your are overweight')
else:
    print('You are obese')
