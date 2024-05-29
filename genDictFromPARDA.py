data = """
     0, 0.20022831,       1403001
     1, 0.09990001,        700000
     2, 0.29970019,       2100001
     3, 0.10047073,        703999
     4, 0.19980003,       1400000
    -1, 0.09990073,        700005
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