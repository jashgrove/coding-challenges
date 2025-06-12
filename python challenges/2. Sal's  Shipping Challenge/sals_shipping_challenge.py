weight = 41.5

#Ground Shipping
def calculate_ground_cost(weight):
  if weight <= 2:
    return weight * 1.50 + 20
  elif weight <= 6:
    return weight * 3 + 20
  elif weight <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

#Ground Shipping Premium
premium_cost = 125

#Drone Shipping
def calculate_drone_cost(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight <= 6:
    return weight * 9
  elif weight <= 10:
    return weight * 12
  else:
    return weight * 14.25

ground_cost = calculate_ground_cost(weight)
drone_cost = calculate_drone_cost(weight)
print(ground_cost, premium_cost, drone_cost)
