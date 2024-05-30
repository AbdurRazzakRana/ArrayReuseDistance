data = """
     0, 0.20053207,       3618001
     1, 0.09976717,       1800000
     2, 0.29930157,       5400001
     3, 0.10076479,       1817999
     4, 0.19920184,       3594001
     5, 0.00033250,          5999
   304, 0.00033256,          6000
    -1, 0.09976750,       1800006
"""

# Split the data into lines
lines = data.strip().split('\n')

# Generate dictionary
result_dict = {}
for line in lines:
    parts = line.split(',')
    key = int(parts[0].strip())
    value = int(parts[2].strip())
    result_dict[key] = value

print(result_dict)