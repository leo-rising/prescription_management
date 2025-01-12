# Relational Database for Prescription Management (MySQL)
## Description
A database developed for MySQL using example data (in data folder) and a set of tables modeling patient, pharmacy, and physician interactions.

## Functions
A trigger is made for insertions of new prescriptions, which creates an alert if an adverse interaction exists with an already prescribed drug.

A procedure `speciality_years` takes in a physicians SSN and outputs the number of years at their primary speciality.

## How to use

A local server should be hosted through MySQL after downloading the example data provided in .csv format.

`create_tables` contains Python script which uses the `mysql-connector-python` package to deploy SQL commands to MySQL. Running this populates your server with a database called `hospital` containing the tables described in the schema below.

The SQL script `create_functions.sql` creates the custom trigger and procedure described above.

## Database schema

**Bold** text indicates a `primary key`. Arrows `→` indicate `foreign key` implementations.

`patients`(**ssn**, name, address, birth-date, physician_id)
* physician_id `→` physicians(ssn)

`physicians`(**ssn**, name, primary_specialty, experience_years)

`pharmacies`(**id**, name, address, phone)

`drugs`(id, **name**)

`prescriptions`(**id**, patient_id, physician_id, drug_name, date, quantity)
* patient_id `→` patients(ssn)
* physician_id `→` physicians(ssn)
* drug_name `→` drugs(name)

`adverse_interactions`(**drug_name, drug_name**)
* drug_name `→` drugs(name)

`alerts`(patient_id, physician_id, alert_date, drug1, drug2) <br>
`drug2` triggers entry
* patient_id `→` patients(ssn)
* physician_id `→` physicians(ssn)
Ensuring that a patient is prescribed both drug1 and drug2
* (patient_id, drug1) `→` prescriptions(patient_id, drug_name)
* (patient_id, drug2) `→` prescriptions(patient_id, drug_name)

pharmacy_fills(**prescription_id, pharmacy_id**, date, cost)
* prescription_id `→` prescriptions(id)
* pharmacy_id `→` pharmacy(id)

companies(**id**, name, address, contact_phone, contact_name)

contracts(**id**, company_id, pharmacy_id, drug_name, dosage, quantity, date
* company_id `→` companies(id)
* pharmacy_id `→` pharmacies(id)
* drug_name `→` drugs(name)


