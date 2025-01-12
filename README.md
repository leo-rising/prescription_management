# Relational Database for Prescription Management (MySQL)
### Description
A database developed for MySQL using example data (in data folder) and a set of tables modeling patient, pharmacy, and physician interactions.

### Database schema

patients(ssn, name, address, birth-date, physician_id)
FK references:
physician_id  physicians(ssn)
physicians(ssn, name, primary_specialty, experience_years)
pharmacies(id, name, address, phone)
drugs(id, name)
prescriptions(id, patient_id, physician_id, drug_name, date, quantity)
FK references: patient_id  patients(ssn)
		    physician_id  physicians(ssn)
		     drug_name  drugs(name)
adverse_interactions(drug_name, drug_name)
FK references: drug_name  drugs(name)

#we assume that prescription of drug2 is what triggers the entry in the alert
alerts(patient_id, physician_id, alert_date, drug1, drug2)
FK references: 
		    patient_id  patients(ssn)
		    physician_id  physicians(ssn)
		#The following two FK references are to ensure that patient was prescribed both drug1 and drug2
		     (patient_id, drug1)  prescriptions(patient_id, drug_name)
		    (patient_id, drug2)  prescriptions(patient_id, drug_name)
		
#Here we are assuming that pharmacies sell only prescription drugs
pharmacy_fills(prescription_id, pharmacy_id, date, cost)
FK references: prescription_id  prescriptions(id)
		    pharmacy_id  pharmacy(id)
companies(id, name, address, contact_phone, contact_name)
contracts(id, company_id, pharmacy_id, drug_name, dosage, quantity, date)
FK references: company_id  companies(id)
		    pharmacy_id  pharmacies(id)
		    drug_name  drugs(name)
![image](https://github.com/user-attachments/assets/41973353-55d5-4870-b806-6035609d4354)

### Functions

### How to use


