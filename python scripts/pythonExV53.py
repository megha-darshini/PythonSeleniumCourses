import json
op_dict = {}
email_list=[]
with open("v52.csv", 'r') as f:
    # for i in f:
    #     i=i.strip(",\n")
    #     #i=i.strip(',')
    #     #print(i)
    #     email_list.append( i.split("@"))
    email_raw = f.readlines()
    email_list = [i.strip(',\n') for i in email_raw]
    #print(email_list)

    #print(domain_list)
    for email in email_list:
        domain = email.split('@')[-1]
        #print(domain_list)
        if domain not in op_dict:
            op_dict[domain]= 1
        else:
            op_dict[domain]  = op_dict[domain] + 1
    #print(email_list)
with open("v53.json", 'w') as f:
    json_obj = json.dumps(op_dict)
    f.write(json_obj)
