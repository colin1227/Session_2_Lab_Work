import math  # Required in Python 3
from functools import reduce
import operator

import time

cancelled = False

final = []


def inquiryUser(reqInputs= 3, error=False):
  value = ''
  # Prompt user for numbers
  if reqInputs > 0 and True != bool(error): value = input('{0} number: '.format(str(int((3 * reqInputs / - 3)  + 4))))
  if reqInputs > 0 and bool(error): value = input('must be a number,{0} number: '.format(str(int((3 * reqInputs / - 3)  + 4))))
  
 # Evaluate Response and Recurse 
  if reqInputs > 0:
    try:
      if isinstance(int(value), int):
        final.append(int(value))
        if reqInputs != 1: inquiryUser(reqInputs - 1, False)
    except ValueError:
      inquiryUser(reqInputs, True)
  return final


def LabOne():
  print("Lab One")
  time.sleep(1)
  inquiryUser()
  return f"min: {min(final)}, max: {max(final)}"

def LabTwo():
  time.sleep(1)
  print("Lab Two")
  time.sleep(1)
  inquiryUser()
  return f"sum: {sum(final)}, average: {sum(final) / len(final)}, product: {reduce(operator.mul, final, 1)}, smallest: {min(final)}, largest: {max(final)}"

# python3 ./prog.py
try:

  # first Lab executes
  print(LabOne())
  final = []
  print('')


  # second Lab executs
  print(LabTwo())
  final = []
  print('')

except KeyboardInterrupt:
  print("\nCancelled..")