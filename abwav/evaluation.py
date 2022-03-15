import os 
import numpy as np 
import pdb

test_mode = True
markdown_file = "test.md" if test_mode else "index.md"

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



def making_radio_in_html(file, count):
    f.write('\t<tr>\n')
    f.write('\t\t<td colspan="3">\n')
    for i in range(0, 6):
        id_var = "_prosody" if i < 3 else "_dynamics"
        name_var = str(cnt - 1) + id_var
        value_prefix = ""
        value_var = ""
        if i % 3 == 0:
            value_prefix = 'A'
        elif i % 3 == 1:
            value_prefix = 'B'
        else:
            value_prefix = 'C'
        value_var = value_prefix + id_var

        f.write('\t\t\t<label><input type="radio" id="{}" name="{}" value="{}">{}</label>\n'.format(id_var, name_var, value_var, value_var))
    f.write('\t\t</td>\n')
    f.write('\t</tr>\n')


for idx, key in enumerate(NSinger2Aug_dict.keys()):
    np.random.seed(idx)
    perm = np.random.permutation(["NSinger2Aug", "NSinger2Tune"])
    dict1 = dict_dict[perm[0]]
    dict2 = dict_dict[perm[1]]
    
    if idx == 0:
        with open(markdown_file, 'w') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            index_dict[perm[0]].append(cnt-1)
            cnt += 1
            f.write('\t\t<td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(dict2[key]))
            index_dict[perm[0]].append(cnt-1)
            f.write('\t</tr>\n')
            ##
            making_radio_in_html(f, cnt)
            ##
            f.write('</tbody>\n')
    else: 
        with open(markdown_file, 'a') as f:
            f.write('<tbody>\n')
            f.write('\t<tr>\n')
            f.write('\t\t<th scope="row">{}</th> <td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(cnt, dict1[key]))
            index_dict[perm[0]].append(cnt-1)
            cnt += 1
            f.write('\t\t<td><audio controls="" ><source src="{}" type="audio/wav"></audio></td>\n'.format(dict2[key]))
            index_dict[perm[0]].append(cnt-1)
            f.write('\t</tr>\n')
            ##
            making_radio_in_html(f, cnt)
            ##
            f.write('</tbody>\n')

# The code below have to be inserted after closing table
# f.write('\n<button name="submit" onclick="http://www.google.com">Click me</button>\n')
# <input type="submit" value="Submit"> <input type="reset" value="Reset">