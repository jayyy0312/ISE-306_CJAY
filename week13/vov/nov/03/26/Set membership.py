register_ids = {104,108,115,121}

print (115 in registered_ids) # True
print (999 in registered_ids) # False

registered_ids.add(130)
registered_ids.discard(108)