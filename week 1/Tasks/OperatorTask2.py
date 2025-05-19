Nehal = float(input("Enter Nehal's CGPA____"))
Dhruvo = float(input("Enter Dhruvo's CGPA____"))
Ifti = float(input("Enter Ifti's CGPA____"))

ave = (Nehal+Dhruvo+Ifti)/3

if Nehal<Dhruvo and Nehal<Ifti:
    print(f"{Nehal}, Nehal.... My man don't cry :') ")
elif Dhruvo<Nehal and Dhruvo<Ifti:
    print(f"{Dhruvo}, Yeah...that's impossible(Dhruvo)")
else:
    print(f"{Ifti}, Study hard Brother (Ifti) :'))) ") 

print(f"Average CGPA is {ave}")    