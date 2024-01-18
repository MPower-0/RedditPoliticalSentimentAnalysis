import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'text.color': "white"})

tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df= pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")
ukpolitics_df= pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed UKPolitics Comments.csv")

tories_right_wing = tories_df["Label"].str.count("Right-Wing").sum()
tories_left_wing = tories_df["Label"].str.count("Left-Wing").sum()

tories_data = [tories_right_wing, tories_left_wing]
labels = "Right-Wing", "Left-Wing"

plt.figure()
plt.title("r/tories")
tories_chart = plt.pie(tories_data, labels=labels, colors=["royalblue", "Red"], autopct='%1.2f%%', explode=(0, 0.1), shadow=True, startangle=90)

plt.savefig("tories_user_percentage.png", transparent=True)

labouruk_right_wing = labouruk_df["Label"].str.count("Right-Wing").sum()
labouruk_left_wing = labouruk_df["Label"].str.count("Left-Wing").sum()

labouruk_data = [labouruk_right_wing, labouruk_left_wing]

plt.figure()
plt.title("r/labouruk")
labouruk_chart = plt.pie(labouruk_data, labels=labels, colors=["royalblue", "Red"], autopct='%1.2f%%', explode=(0, 0.1), shadow=True, startangle=90)

plt.savefig("labouruk_user_percentage.png", transparent=True)

ukpolitics_right_wing = ukpolitics_df["Label"].str.count("Right-Wing").sum()
ukpolitics_left_wing = ukpolitics_df["Label"].str.count("Left-Wing").sum()

ukpolitics_data = [ukpolitics_right_wing, ukpolitics_left_wing]

plt.figure()
plt.title("r/ukpolitics")
ukpolitics_chart = plt.pie(ukpolitics_data, labels=labels, colors=["royalblue", "Red"], autopct='%1.2f%%', explode=(0, 0.1), shadow=True, startangle=90)

plt.savefig("ukpolitics_user_percentage.png", transparent=True)

print("Tories Data (Right-Wing:Left-Wing): ", tories_data)
print("LabourUK Data (Right-Wing:Left-Wing): ", labouruk_data)
print("UKPolitics Data (Right-Wing:Left-Wing): ", ukpolitics_data)

plt.show()

