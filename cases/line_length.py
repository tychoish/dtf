#!/usr/bin/python

from cases import DtfCase
from utils import expand_tree
import dtf

class DtfLineLength(DtfCase):
    @staticmethod
    def check_line(line, max_length):
        if len(line) > max_length: 
            return True
        else: 
            return False

    def check_file(self, source_file, p=True):
        ln = 1
        with open(source_file, 'r') as f:
            ln += 1
            for line in f.readlines():
                ln = ln + 1
                if self.check_line(line, self.case['max_length']):
                    p = False
                    break

        if p is False: 
            return p, ln
        else:
            return p, None

    def test(self):
        result = self.check_file(self.case['file'])

        if result[0] is True: 
            msg = ('[%s]: %s has no lines longer than %s characters.' 
                   % (self.name, self.case['file'], self.case['max_length']))
        else:
            msg = ('[%s]: line %s in "%s" is longer than %s characters.' 
                   % (self.name, result[1], self.case['file'], self.case['max_length']))
            
        return result[0], msg

def main(name, case):
    c = DtfLineLength(name, case)
    c.required_keys(['file', 'max_length', 'name'])
    c.run()
