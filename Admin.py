from Doctor import Doctor
import csv

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a_list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if self.__username == username and self.__password == password:
            return self.__username
        else:
            raise Exception("Incorrect username or password")

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        speciality = input("Enter speciality: ")
        return first_name, surname, speciality
        pass

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input()
        pass


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
            pass

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break
                   
            else:
                doctors.append(Doctor(first_name, surname, speciality))
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)
            

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            if op == 1:
                new_name = input("Enter the new first name: ")
                doctors[doctor_index].set_first_name(new_name)
            
            elif op == 2:
                  new_name = input("Enter the new surname: ")
                  doctors[doctor_index].set_surname(new_name)
                  
            elif op == 3:
                  new_speciality = input("Enter the new speciality: ")
                  doctors[doctor_index].set_speciality(new_speciality)
            
            print("Doctor details have been updated.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            try:
                # doctor_index is the patient ID mines one (-1)
                doctor_index = int(doctor_index) -1
                
                #check if the id is in the list of doctors
                if doctor_index not in range(len(doctors)):
                    print("The ID entered was not found.")
                else:
                    del doctors[doctor_index]
                    print("Doctor has been deleted.")
                    
            except ValueError: # the entered id could not be changed into an int
               print("The id entered is incorrect")
                    

    def view_patients(self, a_list, patients):
        """
        print a list of patients
        Args:
            a_list (list): a list of patient objects
        """
        self.view(patients)



    def A_assignDocToPatient(self):
        assignPatients = True
        columnNames = ["First name","Surname","Age","Mobile number","Postcode","Symptoms","Assigned doctor"]
        patientAssignList = []
        
        doctorName = input("Enter doctors name:\n")
        while(assignPatients):
            patientName = input("\nEnter patient name:\n")
            patientAddress = input("\nEnter patient Address:\n")
            patientAssignList.append(patientName)
            choice = input("Would you like to assign another patient?\t(Y/N)\n")
            if choice == "N":
                assignPatients = False
                break
            else:
                pass
        
        with open('Patient.csv', "r", newline="") as r:
            readerpatients = csv.reader(r)
            rowspatients = list(readerpatients)
        for rows in rowspatients[1:]:
            if rows[0] == patientName and rows[4] == patientAddress:
                rows[6] = doctorName
        
        with open('Patient.csv','w',newline='')as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(rowspatients)
            f.close()
            
        


    def discharge(self):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("----Discharge Patient----")
        patient_index = input("Please enter the patient ID: ")
        with open("Patient.csv", "r", newline="") as patients:
            readerpatients = csv.reader(patients)
            rowspatients = list(readerpatients)
        try:
            #patient_index is the patient ID mines one
            patient_index = int(patient_index)
            
            #check if the id is in the list of patients
            if patient_index not in range(len(rowspatients)):
                print("The id entered was not found.")

            
        except ValueError:
                print("Please enter a number for the ID.")
            
        #move patient from active patient list to deleted patient list
        if 0 < patient_index and patient_index <= len(rowspatients):
            information = rowspatients[patient_index]
            with open("Discharge.csv", "a", newline="") as discharge:
                dischargewriter = csv.writer(discharge)
                dischargewriter.writerow(information)
                
            del rowspatients[patient_index]
            with open("Patient.csv", "w", newline="") as patientremove:
                 writerdoc = csv.writer(patientremove)
                 writerdoc.writerows(rowspatients)
        
            print("The patient has been discharged.")
        else:
            print("Patient ID Out Of Range!")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        for patient in discharged_patients:
            patient_details = patient.get_details()
            doctor_details = patient.get_doctor().get_details()
            
            print(f'{patient_details["id"]} | {patient_details["name"]} | {doctor_details["name"]} | {patient_details["Age"]} | {patient_details["Mobile"]} | {patient_details["Postcode"]}')
        pass

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input("Enter the new username: ")
            print("The username has been updated.")
            self.__username = new_username
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                print("The password has been updated.")
                self.__password = password

        elif op == 3:
            new_address = input("Enter the new address: ")
            print("The address has been updated.")
            self.__address = new_address
            
            pass

        else:
            print("Invalid operation")
            pass
        
    def group_patients_by_username(self, patients):
        grouped_patients = {}
        for patient in patients:
            surname = patient.get_surname()
            
            if surname in grouped_patients:
                grouped_patients[surname].append(patient)
            else:grouped_patients[surname] = [patient]
            
        return grouped_patients
                

