premium_shipping = 125
def ground_shipping(weight):
   if weight <= 2:
     cost = (1.5 * weight) + 20
     return cost
   elif weight >= 2 and weight <= 6:
     cost = (3 * weight) + 20
     return cost
   elif weight >= 6 and weight <= 10:
     cost = (4 * weight) + 20
     return cost
   else:
     cost = (4.75 * weight) + 20
     return cost
def drone_shipping(weight):
  if weight <= 2:
     cost = (4.5 * weight)
     return cost
  elif weight >= 2 and weight <= 6:
     cost = (9 * weight)
     return cost
  elif weight >= 6 and weight <= 10:
     cost = (12 * weight)
     return cost
  else:
     cost = (14.25 * weight)
     return cost
def cheapest_shipping(weight):
  if drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping:
    return "You should ship using drone shipping"
  elif ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
    return "You should ship using ground shipping"
  else:
    return "You should ship using premium shipping"

print(ground_shipping(8.4))
print(drone_shipping(1.5))
print(cheapest_shipping(2))
