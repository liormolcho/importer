import json
from dateutil.parser import parse

class Configuration(object):
	def __init__(self, configuration_map, empty_value=None):
		self.db_field = configuration_map['db_field']
		self.csv_field = configuration_map['csv_field']
		self.split_by = None
		self.position = None
		self.special_mapping = {}
		self.has_special_mapping = False
		self.date = False
		self.empty_value = empty_value
		if 'date' in configuration_map:
			self.date = True
		if 'split_by' in configuration_map:
			self.split_by = configuration_map['split_by']
			self.position = configuration_map['position']
		if 'special_mapping' in configuration_map:
			self.has_special_mapping = True
			self.special_mapping = configuration_map['special_mapping']

	def get_parsed_value(self, db_value):
		if db_value == self.empty_value:
			return None
		split_value = self.get_split(db_value)
		if self.date:
			dt = parse(db_value)
			return dt.strftime('%d/%m/%Y')
		if self.has_special_mapping:
			if str(split_value) in self.special_mapping:
				return self.special_mapping[split_value]
			else:
				raise ValueError(str(split_value), " is not a valid input for ", self.csv_field, " mapping")
		return split_value

	def get_split(self, db_value):
		if self.split_by == None:
			return db_value
		else:
			return db_value.split(self.split_by)[self.position]