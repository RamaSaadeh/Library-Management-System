#student ID : F213886

import database
import csv
import matplotlib.pyplot as plt

def generate_freq():
  frequency_table={}

  database.load_library()
  with open('log.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
      Lbook_id = row[0]
      
      genre = database.library[Lbook_id]["genre"]

      if genre in frequency_table.keys():
        frequency_table[genre] += 1
      else:
        frequency_table[genre]=1
      
  return frequency_table
      

def suggest():
  suggest_table={}

  database.load_library()
  with open('log.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
      Lbook_id = row[0]
      
      title = database.library[Lbook_id]["title"]
      price = database.library[Lbook_id]["purchase_price"]

      if title in suggest_table.keys():
        suggest_table[title] += 1
      else:
        suggest_table[title]=1
        
  most_popular = []
  for i in range(0,5):
      most_checked_out = max(suggest_table, key=suggest_table.get)
      del suggest_table[most_checked_out]
      most_popular.append(most_checked_out)
      
    
  return most_popular

def budget():
  budget_value={}

  database.load_library()
  with open('log.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
      Lbook_id = row[0]
      
      price = database.library[Lbook_id]["purchase_price"]

      if price in budget_value.keys():
        budget_value[price] += 1
      else:
        budget_value[price] = 1
        
  sum = 0
  for i in range(0,min(5, len(budget_value))):
      most_checked_out = max(budget_value, key=budget_value.get)
      sum += budget_value[most_checked_out]
      del budget_value[most_checked_out]
      
      
    
  return sum