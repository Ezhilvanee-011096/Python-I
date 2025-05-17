class Funtion_group():
    def sub_fields():
        print('Sub-fields in AI are:')
        item_list = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for item in item_list:
            print(item)

    def odd_even(num):
        if((num % 2) == 0):
            print(num, 'is Even number')
        else:
            print(num, 'is  Odd number')

    def eligible(gen, age):
        if((gen.lower() == 'male' and age >= 21) or (gen.lower() == 'female' and age >= 18)):
            print('ELIGIBLE')
        else:
            print('NOT ELIGIBLE')

    def percentage():
        subject_count = 5
        subject_list = []
        add = 0
        for n in range(subject_count):
            subject_mark = int(input(f"Subject{n+1}="))
            subject_list.append(subject_mark)
        for marks in subject_list:
            add += marks
            avg = float(add / 5)
        print("Total :", add)
        print("Average :", float(avg))

    def calc_area(h, b):
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", ((h * b)/2))
        
    def calc_perimeter(h1, h2, b):
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", (h1 + h2 + b))