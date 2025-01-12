pip install mysql-connector-python

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GundralaPK98"   #REPLACE THIS WITH THE PASSWORD YOU SET
)
 
print(mydb)
 
if mydb.is_connected():
    print("CONNECTION SUCCESSFUL")

#create a database
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE hospital")

#populate with tables and primary + foreign keys

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE hospital.physicians (SSN CHAR(11) PRIMARY KEY, name VARCHAR(128), primary_speciality VARCHAR(128), experience_years NUMERIC(2,0))")

mycursor.execute("CREATE TABLE hospital.patients (SSN CHAR(11) PRIMARY KEY, name VARCHAR(128), address VARCHAR(255), birth_date VARCHAR(128), physician_ID CHAR(11), FOREIGN KEY(physician_ID) REFERENCES hospital.physicians(SSN))")

mycursor.execute("CREATE TABLE hospital.pharmacies (ID NUMERIC(3,0) PRIMARY KEY, name VARCHAR(128), address VARCHAR(255),phone VARCHAR(20))")

mycursor.execute("CREATE TABLE hospital.drugs (ID NUMERIC(3,0), name VARCHAR(128) PRIMARY KEY)")

mycursor.execute("""CREATE TABLE hospital.prescriptions (ID NUMERIC(3,0) PRIMARY KEY, patient_ID CHAR(11), 
physician_ID CHAR(11), drug_name VARCHAR(128),
date VARCHAR(128), quantity NUMERIC(3,0),
FOREIGN KEY(patient_ID) REFERENCES hospital.patients(SSN),
FOREIGN KEY(physician_ID) REFERENCES hospital.physicians(SSN),
FOREIGN KEY(drug_name) REFERENCES hospital.drugs(name))""")

mycursor.execute("""CREATE TABLE hospital.adverse_interactions (drug_name_1 VARCHAR(128), 
drug_name_2 VARCHAR(128), PRIMARY KEY (drug_name_1, drug_name_2),
FOREIGN KEY(drug_name_1) REFERENCES hospital.drugs(name),
FOREIGN KEY(drug_name_2) REFERENCES hospital.drugs(name))""")

mycursor.execute("""CREATE TABLE hospital.alerts (patient_ID CHAR(11), physician_ID CHAR(11),
alert_date VARCHAR(128), drug1 VARCHAR(128), drug2 VARCHAR(128),
PRIMARY KEY (patient_ID, drug1, drug2),
FOREIGN KEY(patient_ID) REFERENCES hospital.patients(SSN),
FOREIGN KEY(physician_ID) REFERENCES hospital.physicians(SSN))""")

mycursor.execute("""CREATE TABLE hospital.pharmacy_fills (prescription_ID NUMERIC(3,0),
pharmacy_ID NUMERIC(3,0), date VARCHAR(128), cost NUMERIC(6,2),
PRIMARY KEY(prescription_ID, pharmacy_ID),
FOREIGN KEY(prescription_ID) REFERENCES hospital.prescriptions(ID),
FOREIGN KEY(pharmacy_ID) REFERENCES hospital.pharmacies(ID))""")

mycursor.execute("""CREATE TABLE hospital.companies (ID NUMERIC(3,0) PRIMARY KEY, name VARCHAR(128), address VARCHAR(255),
contact_phone VARCHAR(20), contact_name VARCHAR(128))""")

mycursor.execute("""CREATE TABLE hospital.contracts (ID NUMERIC(3,0) PRIMARY KEY, drug_name VARCHAR(128), 
dosage NUMERIC(5,0), pharmacy_ID NUMERIC(3,0), company_ID NUMERIC(3,0), quantity NUMERIC(3,0), date VARCHAR(128),
price NUMERIC(6,2),
FOREIGN KEY(drug_name) REFERENCES hospital.drugs(name),
FOREIGN KEY(pharmacy_ID) REFERENCES hospital.pharmacies(ID),
FOREIGN KEY(company_ID) REFERENCES hospital.companies(ID))""")

# add index for multi-column foreign keys
mycursor.execute("""ALTER TABLE hospital.prescriptions
ADD INDEX idx_patient_drug (patient_ID, drug_name)""")

mycursor.execute("""ALTER TABLE hospital.alerts
ADD CONSTRAINT fk_alerts_prescriptions
FOREIGN KEY (patient_ID, drug1)
REFERENCES hospital.prescriptions (patient_ID, drug_name)""")

mycursor.execute("""ALTER TABLE hospital.alerts
ADD CONSTRAINT fk_alerts_prescriptions_2
FOREIGN KEY (patient_ID, drug2)
REFERENCES hospital.prescriptions (patient_ID, drug_name)""")