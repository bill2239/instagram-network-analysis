__author__ = 'HP'
# create mapping of username and  anonymized id
import csv
import operator
d_dict_in=dict()
d_dict_out=dict()
map_dict=dict()
array=['0','1']
matrix=[]
#for calculating degree
m_1=[]
m_0=[]
d_in=[]
d_out=[]
fd=open('degree.txt','r')
fw=open('mapping.csv', 'wb')
fw_2=open('anonymized_edge_list.txt','w')
fw_3=open('anonymized_edge_list.csv', 'wb')
#fw=open('mapping.txt','w')
writer = csv.writer(fw)
writer2=csv.writer(fw_3)
with open('non_anonymized_egde_list.csv', 'rb') as csvfile:
    read_edge_list=csv.reader(csvfile)
    i=1

    for row in read_edge_list:
        matrix.append(row)



    n=len(matrix)
    for k in range(0,n):
        m_0.append(matrix[k][0])
        m_1.append(matrix[k][1])
        for j in range(2):
        #print array
            if(not map_dict.has_key(matrix[k][j])):
                global i
                print i
                print matrix[k][j]


                map_dict.setdefault(matrix[k][j],i)
                i=i+1


    #print map_dict
    for key, value in sorted(map_dict.items(), key=operator.itemgetter(1)):
        writer.writerow([key, value])
        '''for k in range(0,n):
            m_0.count(key)
            m_1.count(key)'''
    n=len(matrix)

    anonymized_data = []
    array=[]
    for k in range(n):
        array= [map_dict[matrix[k][0]], map_dict[matrix[k][1]]]
        content_a=','.join(map(str,array))
        fw_2.write(content_a)
        fw_2.write('\n')
        anonymized_data.append(array)
        writer2.writerow(array)
        array=[]





fw_2.close()
fd.close()
fw.close()
csvfile.close()