pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def pirate_leg(list):
    name_list = []
    for p in (list):
        if p['has_wooden_leg'] == True and p['gold'] > 15:
            name_list.append(p['Name'])
    return name_list

print('The wooden-leg pirates who has too much gold:', pirate_leg(pirates))
