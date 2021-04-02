import os

path_EEG = 'D:\\Child Mind\\Release1_1\\EEG\\Set_1'
path_MRI = 'D:\\Child Mind\\release1_1\\MRI\\Set_1'
EEG_list = os.listdir(path_EEG)
MRI_list = os.listdir(path_MRI)
EEG_l = len(EEG_list)
MRI_l = len(MRI_list)

for i in range(EEG_l):
    p = EEG_list[i]
    EEG_list[i] = p[:12]
    
for i in range(MRI_l):
    p = MRI_list[i]
    MRI_list[i] = p[4:16]

s = 0;
EEG_MRI_match = list()
f = open("EEG_MRI_match.txt","w")
for i in range(EEG_l):
    for k in range(MRI_l):
        if EEG_list[i] == MRI_list[k]:
            f.write(EEG_list[i])
            f.write("\n")
            print(EEG_list[i])
            EEG_MRI_match.insert(s,EEG_list[i])
            s = s+1
f.close()