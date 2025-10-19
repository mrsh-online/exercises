import pandas as pd

# data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
# df = pd.DataFrame(data)


# From a list of lists
data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]
df = pd.DataFrame(data, columns=["Name", "Age"])

# df = pd.read_csv("./RacismDetectionDataSet.csv")
# print(df)

print(df["Name"])

df.to_csv('hello.csv', index=False)
