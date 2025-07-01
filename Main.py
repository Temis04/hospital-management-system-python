# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import CSV


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','1234','B6 4TM') 
    doctors = [Doctor('Alex','Rider','Internal Med.'), Doctor('Mike','Falcone','Pediatrics'), Doctor('John','Doe','Cardiology')]
    #patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 36,'07555551234','L2 2AB'), Patient('David','Smith', 15, '07123456789','C1 ABC')]
    patients = CSV.read_patients_from_csv('Patient.csv')
    print(patients)
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        try:
            if admin.login():
                running = True # allow the program to run
                break
        except Exception as e:
            print(e)
            print("Try again")
        
        

    while running:  
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Group patients by family')
        print(' 7- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)
            pass

        elif op == '2':
            # 2- View or discharge patients
            admin.discharge()
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_patients(discharged_patients, patients)
            pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.A_assignDocToPatient()

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            
        elif op == '6':
            grouped_patients = admin.group_patients_by_username(patients)
            
            for username, username_members in grouped_patients.items():
                print(f'Username: {username}')
                
                for member in username_members:
                    print(f'   {member.full_name()}')

        elif op == '7':
            # 6 - Quit
            running = False
            print("Quitting Program")
            pass

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
