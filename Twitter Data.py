import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv("tweets.csv", chunksize=10):
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

print(counts_dict)

# Define count_entries()
def count_entries(csv_file, c_size, colname):

    # Initialize an empty dictionary: counts_dict
    counts_dict2 = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        for entry in chunk[colname]:
            if entry in counts_dict2.keys():
                counts_dict2[entry] += 1
            else:
                counts_dict2[entry] = 1

    return counts_dict2

result_counts = count_entries('tweets.csv', 10, 'lang')

print(result_counts)





