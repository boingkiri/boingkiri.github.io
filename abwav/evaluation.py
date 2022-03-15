import os 
import numpy as np 
import pdb


abtest_dirs = os.listdir("wav/abtest")

NSinger2Aug_dict = dict() 
NSinger2Tune_dict = dict() 

for d in abtest_dirs:
    model_name = d.split("_")[0]
    data_name = d[len(model_name)+1:]
    if model_name == "NSinger2Aug":
        NSinger2Aug_dict[data_name] = "wav/abtest/"+d
    elif model_name == "NSinger2Tune":
        NSinger2Tune_dict[data_name] = "wav/abtest/"+d

cnt = 1
dict_dict = {"NSinger2Aug": NSinger2Aug_dict, "NSinger2Tune": NSinger2Tune_dict}
index_dict = {"NSinger2Aug": list(), "NSinger2Tune": list()}

for idx, key in enumerate(NSinger2Aug_dict.keys()):
    np.random.seed(idx)
    perm = np.random.permutation(["NSinger2Aug", "NSinger2Tune"])
    dict1 = dict_dict[perm[0]]
    dict2 = dict_dict[perm[1]]
    
    if idx == 0:
        with open("test.md", 'w') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            index_dict[perm[0]].append(cnt-1)
            cnt += 1
            f.write('\t\t<td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(dict2[key]))
            index_dict[perm[0]].append(cnt-1)
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
    else: 
        with open("test.md", 'a') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            index_dict[perm[0]].append(cnt-1)
            cnt += 1
            f.write('\t\t<td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(dict2[key]))
            index_dict[perm[0]].append(cnt-1)
            f.write('\t</tr>\n')
            f.write('</tbody>\n')
