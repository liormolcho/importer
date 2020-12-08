import json
class DBHospital(object):
	def __init__(self):
		self.patient_row = {"patient_id":None, "mrn":None, "date_of_birth":None, "date_of_death":None,
		             		"deceased":None, "first_name":None, "last_name":None,
		             		"gender":None, "sex":None, "address":None, 
		             		"state":None, "city":None, "zip":None, "last_updated":None}
		self.treatment_row = {"patient_id":None, "start_date":None, "end_date":None, "active":None, 
		                      "name":None, "diagnoses":None, "cycles": None, 
		                      "days":None, "treatment_id":None, "protocol_id":None}
		self.patients_dict = {}
		self.treatments_dict = {}

	def insert_patient(self, patient):
		if not 'patient_id' in patient:
			return
		new_row = self.patient_row.copy()
		new_row.update(patient)
		self.patients_dict[patient["patient_id"]] = new_row

	def insert_treatment(self, treatment):
		if not 'patient_id' in treatment:
			return
		new_row = self.treatment_row.copy()
		new_row.update(treatment)
		self.treatments_dict[treatment["treatment_id"]] = new_row

	def print_db(self):
		print("patients:")
		for id in self.patients_dict:
			print(json.dumps(self.patients_dict[id]))
		print("treatments:")
		for id in self.treatments_dict:
			print(json.dumps(self.treatments_dict[id]))
