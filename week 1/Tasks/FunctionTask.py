def NID(Name,PresentAdd,MobileNo,DOB,Gender):
     print()
     print(f"Name: {Name}")
     print(f"Present Address: {PresentAdd}")
     print(f"Mobile Number: {MobileNo}")
     print(f"DOB: {DOB}")
     print(f"Gender: {Gender}")

NID_data= {}    

NID_data["Name"] = input("Enter Your Name___")
NID_data["PresentAdd"] = input("Enter Your Present Address___")
NID_data["MobileNo"] = input("Enter Your Mobile Number___")
NID_data["DOB"] = input("Enter Your DOB___")
NID_data["Gender"] = input("Enter Your Gender___")

NID(NID_data["Name"],NID_data["PresentAdd"],NID_data["MobileNo"],NID_data["DOB"],NID_data["Gender"])

    