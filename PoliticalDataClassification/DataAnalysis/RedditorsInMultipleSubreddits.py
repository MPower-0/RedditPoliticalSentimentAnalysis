import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'text.color': "white"})

tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")
ukpolitics_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed UKPolitics Comments.csv")

tories_unique = pd.Series(tories_df["Redditor"].unique())
labouruk_unique = pd.Series(labouruk_df["Redditor"].unique())
ukpolitics_unique = pd.Series(ukpolitics_df["Redditor"].unique())

tories_in_labouruk = (tories_unique.isin(labouruk_unique)).value_counts()
print("Amount of r/tories redditors that post in r/labouruk\n", tories_in_labouruk)

tories_in_ukpolitics = (tories_unique.isin(ukpolitics_unique)).value_counts()
print("Amount of r/tories redditors that post in r/ukpolitics\n", tories_in_ukpolitics)

labouruk_in_tories = (labouruk_unique.isin(tories_unique)).value_counts()
print("Amount of r/labouruk redditors that post in r/tories\n", labouruk_in_tories)

labouruk_in_ukpolitics = (labouruk_unique.isin(ukpolitics_unique)).value_counts()
print("Amount of r/labouruk redditors that post in r/ukpolitics\n", labouruk_in_ukpolitics)

plt.figure()
plt.title("Amount of r/tories Redditors that Post in r/labouruk")
plt.pie(tories_in_labouruk, labels=["Post in r/tories only", "Post in both"], colors=["royalblue", "Red"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("tories_in_labouruk.png", transparent=True)

plt.figure()
plt.title("Amount of r/tories Redditors that Post in r/ukpolitics")
plt.pie(tories_in_ukpolitics, labels=["Post in r/tories only", "Post in both"], colors=["royalblue", "Green"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("tories_in_ukpolitics.png", transparent=True)

plt.figure()
plt.title("Amount of r/labouruk Redditors that Post in r/tories")
plt.pie(labouruk_in_tories, labels=["Post in r/labouruk only", "Post in both"], colors=["red", "royalblue"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("labouruk_in_tories.png", transparent=True)

plt.figure()
plt.title("Amount of r/labouruk Redditors that Post in r/ukpolitics")
plt.pie(labouruk_in_ukpolitics, labels=["Post in r/labouruk only", "Post in both"], colors=["red", "green"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("labouruk_in_ukpolitics.png", transparent=True)

plt.show()