from configuration import Configuration

class HospitalConfigurationHandler(object):
	def __init__(self, json_of_configurations):
		self.configurations = {}
		empty_value = None
		if "empty_value" in json_of_configurations:
			empty_value = json_of_configurations["empty_value"]
		for json_config in json_of_configurations["configurations"]:
			conf = Configuration(json_config, empty_value)
			if conf.csv_field in self.configurations:
				self.configurations[conf.csv_field].append(conf)
			else:
				self.configurations[conf.csv_field] = [conf]

	def parse_line(self, csv_map):
		res_map = {}
		for map_value in csv_map:
			if map_value in self.configurations and csv_map[map_value] not in ['', None]:
				for conf in self.configurations[map_value]:
					res_map[conf.db_field] = conf.get_parsed_value(csv_map[map_value])
		return res_map

