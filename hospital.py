from hospital_configurations_handler import HospitalConfigurationHandler
from db_hospital import DBHospital
import json
import csv

class Hospital:
	def __init__(self, configuration_file):
		with open(configuration_file, "r") as f:
			lines = f.readlines()
			self.files_start = lines[0].strip()
			self.patient_configuration = HospitalConfigurationHandler(json.loads(lines[1]))
			self.treatment_configuration = HospitalConfigurationHandler(json.loads(lines[2]))
		self.db = DBHospital()

	def is_it_my_file(self, file_name):
		return file_name.startswith(self.files_start)

	def parse_patient_file(self, file):
		with open(file, newline='', encoding = 'utf-8-sig') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				parsed = self.patient_configuration.parse_line(row)
				self.db.insert_patient(parsed)

	def parse_treatment_file(self, file):
		with open(file, newline='', encoding = 'utf-8-sig') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				parsed = self.treatment_configuration.parse_line(row)
				self.db.insert_treatment(parsed)

	def print_db(self):
		self.db.print_db()