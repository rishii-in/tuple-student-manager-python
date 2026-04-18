print()
print("======== 🎓 student record manager ============")

students=()

while True:
    print()
    print("📌 1. Add student ")
    print("📋 2.Show students")
    print("🏆 3.Find Topper")
    print("📊 4.Average marks")
    print("🔍 5.Search student")
    print("🚪 6.Exit\n")
  
    c=int(input("👉 Enter your choice (1-6) : "))

    if c==1:
        n=input("\n👤 Enter name : ")
        m=int(input("📝 Enter marks :  "))
        students+=((n,m),)
        print("✅ Student added successfully!")
    elif c==2:
        if len(students) == 0:
            print("⚠️ Student Records Not found")
        else:
            print("📊 Students Data\n")
            print("-------------------------------")
            for i in students:
                print("👤 Name:", i[0], "| Marks:", i[1])
            print("-------------------------------")

    elif c==3:
        print("🏆 Finding Topper... ")
        if len(students)== 0:
            print("⚠️ No Students Available ")
        else: 
            t=students[0]
            for i in students:
                if i[1]>t[1]:
                    t=i
            print("\n🏆 Topper Details")
            print("-----------------------------------")
            print("🥇 Topper is :",t[0],"\n💯 Marks :",t[1])
            print("-----------------------------------\n")
    elif c==4:
        if len(students) == 0:
            print("⚠️ No students available!")
        else:
            total=0
            for s in students:
                total+=s[1]
            avg=total/len(students)
            print(f"📊 Average Marks: {avg:.2f}")

    elif c==5:
        name=input("\n🔍 enter Student name to search : ")
        for i in students:
            if i[0]==name:
                print("\n student",i[0]," is found ✅ ")
                break
        else:
            print("\n❌ Student not found ")
    elif c==6:
        print("\n🚪Logging off....👋 Nice to Meet You \n")
        break
    else:
        print("\n❌ Invalid choice")
