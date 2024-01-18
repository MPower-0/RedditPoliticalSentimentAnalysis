import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")

users_to_analyse = ["b0cc008d4a8fbced52183219ef5fa635511090d9c4cc653a5192553ee2287762","2caf414cb95e3dadd07b9da56fdd51d6793fdaf97b6a7bbbe9ac01093baceb39",
                  "26cf9a8e8d088a3ec5d175f916003d1fcbb06f969c7abc6cd73a208cb120454f", "95e215f5a8e499f2bdb3432c5c39f0c3585b073b166b45b78d1465bfe5583a62", "e37f12987aa58f5a69d81e2252832510dad0eb901087e4d82d9f89f46813ad83"]

#Gets the political labelling of the selected Redditors comments and calculates the percentages of left-wing to right-wing comments
user1_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[0]]
user1_label_count = user1_tories["Label"].value_counts()
user1_right_percentage = (user1_label_count[0] / (user1_label_count[0] + user1_label_count[1])) * 100
user1_left_percentaage = (user1_label_count[1] / (user1_label_count[0] + user1_label_count[1])) * 100
user1_percentages = [user1_right_percentage, user1_left_percentaage]

user2_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[1]]
user2_label_count = user2_tories["Label"].value_counts()
user2_right_percentage = (user2_label_count[0] / (user2_label_count[0] + user2_label_count[1])) * 100
user2_left_percentaage = (user2_label_count[1] / (user2_label_count[0] + user2_label_count[1])) * 100
user2_percentages = [user2_right_percentage, user2_left_percentaage]

user3_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[2]]
user3_label_count = user3_tories["Label"].value_counts()
user3_right_percentage = (user3_label_count[0] / (user3_label_count[0] + user3_label_count[1])) * 100
user3_left_percentaage = (user3_label_count[1] / (user3_label_count[0] + user3_label_count[1])) * 100
user3_percentages = [user3_right_percentage, user3_left_percentaage]

user4_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[3]]
user4_label_count = user4_tories["Label"].value_counts()
user4_right_percentage = (user4_label_count[0] / (user4_label_count[0] + user4_label_count[1])) * 100
user4_left_percentaage = (user4_label_count[1] / (user4_label_count[0] + user4_label_count[1])) * 100
user4_percentages = [user4_right_percentage, user4_left_percentaage]

user5_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[4]]
user5_label_count = user5_tories["Label"].value_counts()
user5_right_percentage = (user5_label_count[0] / (user5_label_count[0] + user5_label_count[1])) * 100
user5_left_percentaage = (user5_label_count[1] / (user5_label_count[0] + user5_label_count[1])) * 100
user5_percentages = [user5_right_percentage, user5_left_percentaage]

print("User 1 Label Count\n", user1_percentages)
print("User 2 Label Count\n", user2_percentages)
print("User 3 Label Count\n", user3_percentages)
print("User 4 Label Count\n", user4_percentages)
print("User 5 Label Count\n", user5_percentages)


fig, ax = plt.subplots()

ax.broken_barh([(0, user1_percentages[0]), (user1_percentages[0], user1_percentages[1])], [10, 9], facecolors=("royalblue", "red"))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.set_yticks([30])

ax.set_axisbelow(True)

ax.set_yticklabels(["User 1"])
ax.grid(axis="x")
ax.text(user1_percentages[0]-12, 14.5, "60.00%", fontsize=10)
ax.text((user1_percentages[0]+user1_percentages[1])-12, 14.5, "40.00%", fontsize=10)

fig.suptitle('User 1 Right vs Left Labelled Views', fontsize=16)

leg1 = mpatches.Patch(color='royalblue', label='Right-Wing')
leg2 = mpatches.Patch(color='red', label='Left-Wing')
ax.legend(handles=[leg1, leg2], ncol=2)
plt.savefig("user1_labelled_views", transparent=True)

fig, ax = plt.subplots()

ax.broken_barh([(0, user2_percentages[0]), (user2_percentages[0], user2_percentages[1])], [10, 9], facecolors=("royalblue", "red"))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.set_yticks([30])

ax.set_axisbelow(True)

ax.set_yticklabels(["User 2"])
ax.grid(axis="x")
ax.text(user2_percentages[0]-12, 14.5, "58.27%", fontsize=10)
ax.text((user2_percentages[0]+user2_percentages[1])-12, 14.5, "41.73%", fontsize=10)

fig.suptitle('User 2 Right vs Left Labelled Views', fontsize=16)

leg1 = mpatches.Patch(color='royalblue', label='Right-Wing')
leg2 = mpatches.Patch(color='red', label='Left-Wing')
ax.legend(handles=[leg1, leg2], ncol=2)
plt.savefig("user2_labelled_views", transparent=True)

fig, ax = plt.subplots()

ax.broken_barh([(0, user3_percentages[0]), (user3_percentages[0], user3_percentages[1])], [10, 9], facecolors=("royalblue", "red"))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.set_yticks([30])

ax.set_axisbelow(True)

ax.set_yticklabels(["User 3"])
ax.grid(axis="x")
ax.text(user3_percentages[0]-12, 14.5, "55.17%", fontsize=10)
ax.text((user3_percentages[0]+user3_percentages[1])-12, 14.5, "44.83%", fontsize=10)

fig.suptitle('User 3 Right vs Left Labelled Views', fontsize=16)

leg1 = mpatches.Patch(color='royalblue', label='Right-Wing')
leg2 = mpatches.Patch(color='red', label='Left-Wing')
ax.legend(handles=[leg1, leg2], ncol=2)
plt.savefig("user3_labelled_views", transparent=True)

fig, ax = plt.subplots()

ax.broken_barh([(0, user4_percentages[0]), (user4_percentages[0], user4_percentages[1])], [10, 9], facecolors=("royalblue", "red"))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.set_yticks([30])

ax.set_axisbelow(True)

ax.set_yticklabels(["User 4"])
ax.grid(axis="x")
ax.text(user4_percentages[0]-12, 14.5, "74.07%", fontsize=10)
ax.text((user4_percentages[0]+user4_percentages[1])-12, 14.5, "25.93%", fontsize=10)

fig.suptitle('User 4 Right vs Left Labelled Views', fontsize=16)

leg1 = mpatches.Patch(color='royalblue', label='Right-Wing')
leg2 = mpatches.Patch(color='red', label='Left-Wing')
ax.legend(handles=[leg1, leg2], ncol=2)
plt.savefig("user4_labelled_views", transparent=True)

fig, ax = plt.subplots()

ax.broken_barh([(0, user5_percentages[0]), (user5_percentages[0], user5_percentages[1])], [10, 9], facecolors=("royalblue", "red"))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.set_yticks([30])

ax.set_axisbelow(True)

ax.set_yticklabels(["User 5"])
ax.grid(axis="x")
ax.text(user5_percentages[0]-12, 14.5, "67.14%", fontsize=10)
ax.text((user5_percentages[0]+user5_percentages[1])-12, 14.5, "32.86%", fontsize=10)

fig.suptitle('User 5 Right vs Left Labelled Views', fontsize=16)

leg1 = mpatches.Patch(color='royalblue', label='Right-Wing')
leg2 = mpatches.Patch(color='red', label='Left-Wing')
ax.legend(handles=[leg1, leg2], ncol=2)
plt.savefig("user5_labelled_views", transparent=True)

plt.show()