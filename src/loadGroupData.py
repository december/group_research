def load_data(n, day=50):
    gid_list_path='../../groupdata/idset.csv'
    dir_path='../../groupdata/'
    f=open(gid_list_path,'r')
    lines=f.readlines()
    line=lines[n]
    gid=line.strip()
    f.close()
    f=open(dir_path+gid+'.csv','r')
    data=list()
    count = 0
    for i in range(4):
        line=f.readline()
        tmp=list()
        for j in line.strip().split(','):
            if count < day:
                tmp.append(int(j))
                count += 1
            else:
                count = 0
                break
        data.append(tmp)
    f.close()
    return data

def load_test_data(n):
    gid_list_path='../../groupdata/idset.csv'
    dir_path='../../groupdata/'
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
