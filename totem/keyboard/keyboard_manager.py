import pygame as py
from pygame.locals import *


class KeyManager:
    def __init__(self):
        """Set up method to read the keyboard every cycle and understand what has changed."""
        self.new_keys_cycle = []
        self.existing_keys = []
        self.supported_key_list = []
        self.keys_found = False
        self.key_action_dict = self._generate_key_matrix()

    def process_new_key(self, key_press):
        """Read all the new keys and see whats new. If a new key, process it."""
        self.new_keys_cycle.append(key_press)
        if not self.existing_keys.get(key_press):
            self.existing_keys.append(key_press)

        self.keys_found = True

        if self.keys_found:
            for each_key in self.existing_keys:
                # Process each new key press.
                self.take_key_action(each_key)

    def process_all_keys(self):
        pass

    def take_key_action(self, key_press):
        if key_press in self.key_action_dict.keys():
            print(key_press)
            result = self.key_action_dict[key_press]
            print(result)

    def _generate_key_matrix(self):
        """Expected output: {K_KEY: self.key_escape()}"""
        output_dict = {}
        defined_functions = [named_func for named_func in dir(self) if '__' != named_func[0:2]]
        for function_name in defined_functions:
            if 'action' == function_name[0: 6]:
                try:
                    function_call = getattr(self, function_name)
                    supported_key = str(function_name[7:].upper())
                    self.supported_key_list.append(supported_key)
                    output_dict.update({supported_key: function_call})
                except:
                    breakpoint()
        return output_dict

    """-----Start of key functions-----"""
    def action_k_escape(self):
        print('escape!')
        return True



