DELIMITER //
CREATE TRIGGER drug_interaction AFTER INSERT ON prescriptions
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT drug_name FROM prescriptions
        WHERE patient_ID = NEW.patient_ID
        UNION
        SELECT drug_name_2 FROM adverse_interactions
        WHERE drug_name_1 = NEW.drug_name
    )
    THEN
		INSERT INTO alerts (patient_ID, physician_ID, alert_date, drug1, drug2)
        VALUES (NEW.patient_ID, NEW.physician_ID, NEW.date, (
        SELECT drug_name FROM prescriptions
        WHERE patient_ID = NEW.patient_ID
        UNION
        SELECT drug_name_2 FROM adverse_interactions
        WHERE drug_name_1 = NEW.drug_name
        ), NEW.drug_name);
	END IF;
END//
DELIMITER ;

DELIMITER //
CREATE procedure hospital.speciality_years (IN p_id CHAR(11), OUT speciality VARCHAR(128),
									OUT yoe NUMERIC(2,0))
BEGIN
	SELECT primary_speciality, experience_years
    INTO speciality, yoe
    FROM hospital.physicians
    WHERE SSN = p_id;
END//
DELIMITER ;