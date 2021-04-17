def most_frequent(s):
    out_dict={}
    for x in s:
        if x in out_dict:
            out_dict[x]+=1
        else:
            out_dict[x]=1
    return out_dict
n=input("Enter the string:")
d=most_frequent(n)
d=sorted(d.items(),key=lambda x:x[1],reverse=True)#to get highest count letter first
for x in d:
    print(x[0],"=",x[1])

