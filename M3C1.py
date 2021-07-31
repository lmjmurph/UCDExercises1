import pandas as pd

# Exercise 1
ride_sharing = pd.read_csv("ride_sharing_new.csv")


# Print the information of ride_sharing
print(ride_sharing.info())
print("_______________________")

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
print("_______________________")

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype("category")

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics
print(ride_sharing['user_type_cat'].describe())
print("_______________________")

# Exercise 2

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip("minutes")

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing[['duration', 'duration_trim', 'duration_time']])
print(ride_sharing["duration_time"].mean())

# -------------------
# Exercise 3
# Uses field "tire sizes" which is not in the dataset provided - done on Datacamp only

# --------------------
