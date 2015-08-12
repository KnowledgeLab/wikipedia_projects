
# coding: utf-8

# In[196]:

import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys
import re
import random

def load_csv(filename):
    soups = {}
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        soups[row[0]] = row[1:]
    return soups

def load_bots(filename):
    ret = []
    fil = open(filename,'rb')
    for line in fil.readlines():
        ret.append(line[5:].strip())
    return ret


# In[68]:

lib = load_csv("../processed_data/liberal_editors.txt")
cons = load_csv("../processed_data/conservative_editors_full.txt")
science = load_csv("../processed_data/science_editors.txt")


# In[76]:

bots = load_bots('../all_bots.txt')


# In[75]:

float(len(science))/len(full)


# In[77]:

def strip_bots(group_dict):
    total = 0
    b = 0
    for key in group_dict.keys():
        for editor in group_dict[key]:
            total = total + 1
            if editor in bots:
                b = b + 1
                group_dict[key].remove(editor)
    print float(b)/total
    return group_dict


# In[78]:

def strip_ips(group_dict):
    total = 0
    b = 0
    for key in group_dict.keys():
        for editor in group_dict[key]:
            total = total + 1
            aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",editor)
            if aa or (editor.count(':') >= 5) or (editor[-4:] == '.xxx'):
                b = b + 1
                group_dict[key].remove(editor)
    print float(b)/total
    return group_dict


# In[79]:

lib = strip_bots(lib)
lib = strip_bots(lib)
lib = strip_bots(lib)
lib = strip_bots(lib)


# In[80]:

cons = strip_bots(cons)
cons = strip_bots(cons)
cons = strip_bots(cons)
cons = strip_bots(cons)


# In[81]:

science = strip_bots(science)
science = strip_bots(science)
science = strip_bots(science)
science = strip_bots(science)


# In[82]:

lib = strip_ips(lib)
lib = strip_ips(lib)
lib = strip_ips(lib)
lib = strip_ips(lib)
lib = strip_ips(lib)
lib = strip_ips(lib)


# In[83]:

cons = strip_ips(cons)
cons = strip_ips(cons)
cons = strip_ips(cons)
cons = strip_ips(cons)
cons = strip_ips(cons)
cons = strip_ips(cons)


# In[84]:

science = strip_ips(science)
science = strip_ips(science)
science = strip_ips(science)
science = strip_ips(science)
science = strip_ips(science)
science = strip_ips(science)


# In[85]:

def strip_smackbot(group_dict):
    total = 0
    b = 0
    for key in group_dict.keys():
        for editor in group_dict[key]:
            total = total + 1
            if editor == 'SmackBot':
                b = b + 1
                group_dict[key].remove(editor)
            elif editor == '':
                b = b + 1
                group_dict[key].remove(editor)
    print float(b)/total
    return group_dict


# In[87]:

lib = strip_smackbot(lib)


# In[89]:

cons = strip_smackbot(cons)


# In[91]:

science = strip_smackbot(science)


# In[235]:

lib_small = random.sample(lib.items(), 5200)
lib_small[0]
ls = {}
for i in lib_small:
    ls[i[0]] = i[1]
ls[ls.keys()[0]]


# In[236]:

cons_small = random.sample(cons.items(), 5800)
cons_small[0]
cs = {}
for i in cons_small:
    cs[i[0]] = i[1]


# In[237]:

science_small = random.sample(science.items(), 9000)
science_small[0]
ss = {}
for i in science_small:
    ss[i[0]] = i[1]


# In[53]:

def make_net_dict():
    ret = {}
    for key in lib.keys():
        ret[key] = ['liberal', lib[key]]
    for key in cons.keys():
        k = key[62:-8]
        ret[k] = ['conservative', cons[key]]
    for key in science.keys():
        k = key[57:-8]
        ret[k] = ['science', science[key]]
    return ret

full = make_net_dict()
len(full)



# In[238]:

def make_net_dict_small():
    ret = {}
    for key in ls.keys():
        ret[key] = ['liberal', ls[key]]
    for key in cs.keys():
        k = key[67:-8]
        ret[k] = ['conservative', cs[key]]
    for key in ss.keys():
        k = key[57:-8]
        ret[k] = ['science', ss[key]]
    return ret

mid = make_net_dict_small()
len(mid)


# In[239]:

out = open("../processed_data/cleaned_editors_mid.txt", 'wb')
wb = csv.writer(out)
for key in small.keys():
    wb.writerow([key, small[key][0]] + small[key][1])
out.close()


# In[2]:

def load_clean(filename):
    soups = {}
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        soups[row[0]] = [row[1], row[2:]]
    return soups


# In[149]:

full = load_clean('../processed_data/cleaned_editors_small.txt')


# In[151]:

full[full.keys()[500]]


# In[56]:

political_dic = {}
for key in full.keys():
    if full[key][0] in ['liberal', 'conservative']:
        for editor in full[key][1]:
            political_dic[editor] = []
for key in full.keys():
    if full[key][0] in ['liberal', 'conservative']:
        for editor in full[key][1]:
            political_dic[editor].append(full[key][0])
t = 0
d = 0
for k in political_dic.keys():
    if len(set(political_dic[k])) > 1:
        d = d + 1
    t = t + 1

print d
print t
print float(d)/t


# In[57]:

editor_dic = {}
for key in full.keys():
    for editor in full[key][1]:
        editor_dic[editor] = []
for key in full.keys():
    for editor in full[key][1]:
        editor_dic[editor].append(full[key][0])
t1 = 0
d1 = 0
for k in editor_dic.keys():
    if ('science' in set(editor_dic[k])):
        t1 = t1 + 1
        if (len(set(editor_dic[k])) > 1):
            d1 = d1 + 1

print d1
print t1
print float(d1)/t1

#print set(science_list).intersection(liberal_list).union(set(science_list).intersection(conservative_list))
print len(set(science_list))


# In[58]:

liberal_list = []
conservative_list = []
science_list = []
for key in full.keys():
    if full[key][0] == 'liberal':
        liberal_list.extend(full[key][1])
    elif full[key][0] == 'conservative':
        conservative_list.extend(full[key][1])
    elif full[key][0] == 'science':
        science_list.extend(full[key][1])
article_d = {}
d2 = 0
t2 = 0

both = set(liberal_list).intersection(set((conservative_list)))
for key in full.keys():
    if full[key][0] in ['liberal', 'conservative']:
        t2 = t2 + 1
        local = 0
        for editor in full[key][1]:
            if editor in both:
                local = local + 1
        if local:
            d2 = d2 + 1

print d2
print t2
print float(d2)/t2


# In[135]:

liberal_list = []
conservative_list = []
science_list = []
for key in small.keys():
    if small[key][0] == 'liberal':
        liberal_list.extend(full[key][1])
    elif small[key][0] == 'conservative':
        conservative_list.extend(full[key][1])
    elif small[key][0] == 'science':
        science_list.extend(full[key][1])
    


# In[195]:

conservative_list


# In[7]:

dic = {}
i = 0
for ed in set(liberal_list):
    print i
    i = i + 1
    one = liberal_list.count(ed)
    two = conservative_list.count(ed)
    three = science_list.count(ed)
    dic[ed] = [one, two, three]


# In[59]:

editor_dic = {}
for key in full.keys():
    for editor in full[key][1]:
        editor_dic[editor] = []
for key in full.keys():
    for editor in full[key][1]:
        editor_dic[editor].append(key)


# In[60]:

sorted_list = sorted(editor_dic.items(), key=lambda x: len(x[1]), reverse=True)


# In[ ]:

Cydebot, Rjwilmsi(?), Full-date unlinking bot, VIAFbot, 


# In[61]:

edi = []
for it in sorted_list:
    edi.append([it[0], len(it[1])])
edi[:100]


# In[97]:

print len(set(liberal_list).intersection(set((conservative_list))))
print len(set(liberal_list).union(set(conservative_list)))
print float(30724)/135494


# In[139]:

small.keys()[0]


# In[62]:

article_d = {}
d3 = 0
t3 = 0
political = set(liberal_list).union(set(conservative_list))
poli_sci = political.intersection(set(science_list))
for key in full.keys():
    if full[key][0] in ['science']:
        t3 = t3 + 1
        local = 0
        for editor in full[key][1]:
            if editor in poli_sci:
                local = local + 1
        if local:
            d3 = d3 + 1
                
                

print d3
print t3
print float(d3)/t3


# In[63]:

len(editor_dic.keys())


# In[100]:

s = sorted(poli_sci)
print s[:1000]


# In[ ]:

import networkx as nx
import itertools

comb = itertools.combinations(full.keys(), 2)
temp = []

for tup in comb:
    first = full[tup[0]][1]
    second = full[tup[1]][1]
    weight = len(set(first).intersection(set(second)))
    if weight > 0:
        temp.append((tup[0], tup[1], weight))


# In[7]:

len(temp)


# In[105]:

full['Joseph_W_Chalmers']


# In[114]:

set(full['Joseph_W_Chalmers'][1]).intersection(set(full['James_Graham_Fair'][1]))


# In[136]:

import networkx as nx
G=nx.Graph()
temp = []
i = 0
while i < len(full.keys()):
    j = i + 1
    while j < len(full.keys()):
        first = full[full.keys()[i]][1]
        second = full[full.keys()[j]][1]
        weight = len(set(first).intersection(set(second)))
        if weight > 0:
            temp.append((full.keys()[i], full.keys()[j], weight))
        j = j + 1
    i = i + 1
    print i


# In[203]:

def load_edges(filename):
    ret = []
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        ret.append((row[0], row[1], row[2]))
    return ret

ret = load_edges('../processed_data/edges.txt')
len(ret)


# In[204]:

import networkx as nx
G=nx.Graph()
G.add_weighted_edges_from(ret)
print len(G.nodes(data=True))


# In[214]:

for node in G:
    if small[node][0] == 'liberal':
        color = -1
    elif small[node][0] == 'science':
        color = 0
    elif small[node][0] == 'conservative':
        color = 1
    else: color = 5
    G.node[node]['color'] = color


# In[233]:

for node in G:
    for edge in G.edge[node].keys():
        if int(G.edge[node][edge]['weight']) < 3:
            G.remove_edge(node, edge)

G.edge['Enid_Greene']
    
    


# In[234]:

nx.write_graphml(G,'../small.graphml')


# In[213]:

ss


# In[144]:

set(full['Neurite'][1]).intersection(set(full['Gadolinium'][1]))


# In[139]:

full['Anisocoria'][1]


# In[15]:

nx.write_graphml(G,'so.graphml')


# In[ ]:



