import csv
from Patient import Patient

def read_patients_from_csv(filename):
    """
    Reads patient data from a CSV file and returns a list of patients
    Args:
        filename (str): the name of the CSV file
    Returns:
        list<Patient>: a list of patients read from the CSV file
    """
    patients = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # skip the header
        next(csvreader)

        for row in csvreader:
        
            patient = Patient(row[0], row[1], row[2], row[3], row[4])
            patients.append(patient)

    return patients


