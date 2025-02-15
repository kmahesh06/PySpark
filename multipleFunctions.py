class multipleFunction():
    def oddEven():
        num = int(input("Enter the Number:"))
        if((num%2==1)):
            print("Odd Number")
            message = "Odd Number"
        else:
            print("Even Number")
            message = "Even Number"
        return message

    def BMI():
        BMI = int(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("UnderWeight")
            message = "UnderWeight"
        elif(BMI>=18.5 and BMI <24.9):
            print("NormalWeight")
            message = "NormalWeight"
        elif(BMI>=24.9 and BMI <29.9):
            print("OverWeight")
            message = "OverWeight"
        else:
            print("Very OverWeight")
            message = "Very OverWeight"
        return message