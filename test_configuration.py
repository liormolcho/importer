from configuration import Configuration
import unittest

class TestCofigurationMethods(unittest.TestCase):
	
	def test_non_unique_input_gets_same_output(self):
		conf_map = {"db_field":"this", "csv_field":"this"}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("hey"), "hey")

	def test_different_field_names_get_same_output(self):
		conf_map = {"db_field":"this", "csv_field":"Different"}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("hey"), "hey")

	def test_split_value_get_correct_output(self):
		conf_map = {"db_field":"this", "csv_field":"this", "split_by":"_", "position":0}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("first_second"), "first")

	def test_split_value_second_get_correct_output(self):
		conf_map = {"db_field":"this", "csv_field":"this", "split_by":"_", "position":1}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("first_second"), "second")

	def test_special_mapping_get_correct_output(self):
		conf_map = {"db_field":"this", "csv_field":"this", "special_mapping":{"1":1, "2":2}}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("1"), 1)

	def test_special_mapping_with_wrong_input_throws(self):
		conf_map = {"db_field":"this", "csv_field":"this", "special_mapping":{"1":1, "2":2}}
		conf = Configuration(conf_map)
		with self.assertRaises(ValueError):
			value = conf.get_parsed_value("wrong")

	def test_special_mapping_and_split_get_correct_output(self):
		conf_map = {"db_field":"this", "csv_field":"this", "split_by":"_", "position":0, "special_mapping":{"1":1, "2":2}}
		conf = Configuration(conf_map)
		self.assertEquals(conf.get_parsed_value("1_2"), 1)

	def test_empty_string_value_gets_None(self):
		conf_map = {"db_field":"this", "csv_field":"this"}
		conf = Configuration(conf_map, empty_value="NULL")
		self.assertEquals(conf.get_parsed_value("NULL"), None)

if __name__ == '__main__':
    unittest.main()