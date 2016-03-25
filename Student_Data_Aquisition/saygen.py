#!/usr/bin/python

import json

with open('output_files/eligible_CEN.json') as cenFile:
    students = json.load(cenFile)

for ubit, studentDict in students.iteritems():
    print ubit
