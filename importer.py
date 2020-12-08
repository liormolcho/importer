from hospital import Hospital
import glob

class Importer(object):
	def __init__(self, configuration_folder):
		self.hospitals = [Hospital(file) for file in glob.glob(configuration_folder+"*.txt")]
		self.hospitals_starters = {hos.files_start: hos for hos in self.hospitals}

	def process_file(self, file):
		starter, ending = file.split("\\")[-1].rsplit('_', 1)
		if starter in self.hospitals_starters:
			current_hospital = self.hospitals_starters[starter]
			if "Treatment" in ending:
				current_hospital.parse_treatment_file(file)
			else:
				current_hospital.parse_patient_file(file)
		else:
			raise ValueError("No hospital with this starter:" + starter + " ! please check configuration files")

	def process_folder(self, folder):
		for file in glob.glob(folder+"*.csv"):
			self.process_file(file)

	def print_db(self):
		for hospital in self.hospitals:
			print("now printing: " + hospital.files_start)
			hospital.print_db()

if __name__ == '__main__':
	i = Importer("./")
	i.process_folder("./Software Engineer/")
	i.print_db()