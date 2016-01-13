def load_data(n):
    gid_list_path='../group_data_lyf/idset.csv'
    dir_path='../group_data_lyf/'
    f=open(gid_list_path,'r')
    lines=f.readlines()
    line=lines[n]
    gid=line.strip()
    f.close()
    f=open(dir_path+gid+'.csv','r')
    data=list()
    for i in range(4):
        line=f.readline()
        tmp=list()
        for j in line.strip().split(','):
            tmp.append(int(j))
        data.append(tmp)
    f.close()
    return data

def load_test_data(n):
    gid_list_path='../group_data_lyf/idset.csv'
    dir_path='../group_data_lyf/'
    f=open(gid_list_path,'r')
    lines=f.readlines()
    line=lines[n]
    gid=line.strip()
    f.close()
    f=open(dir_path+gid+'.csv','r')
    data=list()
    for i in range(4):
        line=f.readline()
        tmp=list()
        for j in line.strip().split(','):
            tmp.append(int(j))
        s=len(tmp)
        data.append(tmp[0:s/2])
    f.close()
    return data
