#-------------------------------------------------------------------------------

# Purpose:     Database connectivity sample code 
#-------------------------------------------------------------------------------



while True:
    mat_no = input("Enter matriculation number of student: " )
    try:
        mat = int(mat_no)
    except:
        print('Wrong input')
        continue

    surname = input("Enter surname: " )
    try:
        sur_n = str(surname)
    except:
        print("Wrong Input")
        continue

    first_name = input("Enter first name: " )
    try:
        fst_n = str(first_name)
    except:
        print("Wrong Input")
        continue

    gender = input("Enter gender: " )
    try:
        gend = str(gender)
    except:
        print("Wrong Input")
        continue

    faculty = input("Enter Faculty: " )
    try:
        fac = str(faculty)
    except:
        print("Wrong Input")
        continue

    department = input("Enter Department: " )
    try:
        dpt = str(department)
    except:
        print("Wrong Input")
        continue

    home_address = input("Enter Home address: " )
    try:
        home_add = str(home_address)
    except:
        print("Wrong Input")
        continue

    email = input("Enter Email: " )
    try:
        mail = str(email)
    except:
        print("Wrong Input")
        continue

    phone_number = input("Enter Phone number: " )
    try:
        phone_no = float(phone_number)
    except:
        print("Wrong Input")
        continue

    import sqlite3
    connection = sqlite3.connect('C:\Program Files\DB Browser for SQLite\Saved Database\Copy.db')
    cursor = connection.cursor()

    # values = user_input.split(',')
    cursor.execute("INSERT INTO Admission (mat_no, surname, first_name, gender, faculty, department, home_address, email, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (mat, sur_n, fst_n, gend, fac, dpt, home_add, mail, phone_no))
    connection.commit()

    ask = input('Are you done? (Enter yes/no)' )

    if ask == 'yes':
        break
    elif ask == 'no':
        continue
    else:
        print('Wrong input')

connection.close()
