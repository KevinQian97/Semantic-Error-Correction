import os
import json
import numpy as np

def gen_nl(path):
    f = json.load(open(path,"r"))
    nls = []
    qrs = []
    print(len(f))
    print(f[0].keys())
    keys = list(f[0].keys())
    for key in keys[1:]:
        print(key)
        print(f[0][key])
        print("\n\n")
    for i in range(len(f)):
        nls.append(f[i]["question"])
        qrs.append(f[i]["query"])
    return nls,qrs


def main():
    f = open("./datasets/src-train.txt","w")
    g = open("./datasets/tgt-train.txt","w")
    path = "./datasets/train.json"
    nls,qrs = gen_nl(path)
    for line in nls:
        f.write(line+"\n")
    for line in qrs:
        g.write(line+"\n")
    f.close()
    g.close()
    f = open("./datasets/src-test.txt","w")
    g = open("./datasets/tgt-test.txt","w") 
    path = "./datasets/dev.json"
    nls,qrs = gen_nl(path)
    for line in nls:
        f.write(line+"\n")
    for line in qrs:
        g.write(line+"\n")
    f.close()
    g.close()
    

main()