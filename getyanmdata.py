import yaml

def getyanmdata():
    with open("./data.yaml",'r') as f:
        data=yaml.safe_load(f)
        # print(data)
    return data
# getyanmdata()