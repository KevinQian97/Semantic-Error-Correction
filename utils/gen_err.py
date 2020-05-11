import os
import json
import random
import copy
root_path = "../datasets"
obj_list = ["fruits","animals","vehicles"]
att_list = ["fluid","jew"]
pat_list = ["nations","beverage"]


def parsed_rule(rules):
    parsed_rules = []
    for rule in rules:
        new_dict = {}
        tokens = rule.split(" ")
        num_toks = len(tokens)
        if "(agent)" in tokens:
            new_dict["agent"] = {}
            idx = tokens.index("(agent)")
            if idx >0 and tokens[idx-1]!="(clause)":
                new_dict["agent"]["bef"] = tokens[idx-1]
            if idx < num_toks-1 and tokens[idx+1] != "(clause)":
                new_dict["agent"]["aft"] = tokens[idx+1]
        if "(attr)" in tokens:
            new_dict["attr"] = {}
            idx = tokens.index("(attr)")
            if idx >0 and tokens[idx-1]!="(clause)":
                new_dict["attr"]["bef"] = tokens[idx-1]
            if idx < num_toks-1 and tokens[idx+1] != "(clause)":
                new_dict["attr"]["aft"] = tokens[idx+1]
        parsed_rules.append(new_dict)
        if "(patient)" in tokens:
            new_dict["patient"] = {}
            idx = tokens.index("(patient)")
            if idx >0 and tokens[idx-1]!="(clause)":
                new_dict["patient"]["bef"] = tokens[idx-1]
            if idx < num_toks-1 and tokens[idx+1] != "(clause)":
                new_dict["patient"]["aft"] = tokens[idx+1]
        parsed_rules.append(new_dict)
    return parsed_rules



def data_pre():
    nl_list = []
    nls = open(os.path.join(root_path,"src-train.txt"),"r")
    for nl in nls:
        nl_list.append(nl.strip())
    rule_list = []
    rules = open(os.path.join(root_path,"rules"),"r")
    rules = rules.readlines()
    for rule in rules:
        rule_list.append(rule.strip())
    parsed_rules = parsed_rule(rule_list)
    rep_objs = []
    for name in obj_list:
        objs = open(os.path.join(root_path,name+""),"r")
        objs = objs.readlines()
        for obj in objs:
            if len(obj.strip().split("("))>1:
                obj = obj.strip().split("(")[0]
            else:
                obj = obj.strip()
            rep_objs.append(obj)   
    rep_atts = []
    for name in att_list:
        objs = open(os.path.join(root_path,name+""),"r")
        objs = objs.readlines()
        for obj in objs:
            if len(obj.strip().split("("))>1:
                obj = obj.strip().split("(")[0]
            else:
                obj = obj.strip()
            rep_atts.append(obj)   
    rep_pats = []
    for name in pat_list:
        objs = open(os.path.join(root_path,name+""),"r")
        objs = objs.readlines()
        for obj in objs:
            if len(obj.strip().split("("))>1:
                obj = obj.strip().split("(")[0]
            else:
                obj = obj.strip()
            rep_pats.append(obj)   
    return parsed_rules,rep_objs,rep_atts,rep_pats,nl_list


# def nl_noise(rule_list,rep_objs,nl_list):
#     noise_list = []
#     correct_list = []
#     for nl in nl_list:
#         noise_list.append(nl)
#         correct_list.append(nl)
#         for rule in rule_list:
#             if nl.startswith(rule) and len(nl.split(rule))>0:
#                 splits = nl.split(rule)
#                 print(splits[1].split(" "))
#                 tar = splits[1].split(" ")[2:]
#                 words = random.sample(rep_objs, 20)
#                 for word in words:
#                     noise_list.append(rule+" "+word+" "+" ".join(tar))
#                     correct_list.append(nl)
#     return noise_list,correct_list

def gen_update_tag(elem,rep_objs,rep_atts,rep_pats):
    if elem=="agent":
        words = random.sample(rep_objs,10)
    elif elem=="attr":
        words = random.sample(rep_atts,10)
    else:
        words = random.sample(rep_pats,10)
    return words


def nl_noise(parsed_rules,rep_objs,rep_atts,rep_pats,nl_list):
    nois = []
    corrs = []
    for nl in nl_list:
        nois.append(nl)
        corrs.append(nl)
        toks =nl.split(" ")
        num = len(toks)
        new_dict = {}
        for rule in parsed_rules:
            flag = True
            elems = list(rule.keys())
            for elem in elems:
                if not flag:
                    break
                tag = ""
                locs = list(rule[elem].keys())
                for loc in locs:
                    if rule[elem][loc] not in toks:
                        flag = False
                        break
                    idx = toks.index(rule[elem][loc])
                    if loc=="bef" and idx ==(num-1) or loc=="aft" and idx==0:
                        flag = False
                        break
                    if tag=="":
                        if loc=="bef":
                            tag=toks[idx+1]
                        else:
                            tag=toks[idx-1]
                    else:
                        if loc=="bef":
                            if tag !=toks[idx+1]:
                                flag = False
                                break    
                        else:
                            if tag !=toks[idx-1]:
                                flag = False
                                break   
                if flag:
                    new_dict[elem] = tag
            elems = list(new_dict.keys())
            for elem in elems:
                tag = new_dict[elem]
                words = gen_update_tag(elem,rep_objs,rep_atts,rep_pats)
                for word in words:
                    idx = toks.index(tag)
                    inner_toks = copy.deepcopy(toks)
                    inner_toks[idx]=word
                    nois.append(" ".join(inner_toks))
                    corrs.append(nl)
    return nois, corrs




                    



def main():
    parsed_rules,rep_objs,rep_atts,rep_pats,nl_list = data_pre()
    # print(parsed_rules)

    # raise RuntimeError("sanity check")
    noise_list,correct_list = nl_noise(parsed_rules,rep_objs,rep_atts,rep_pats,nl_list)
    f = open(os.path.join(root_path,"nonl.txt"),"w")
    g = open(os.path.join(root_path,"nl.txt"),"w")
    for line in noise_list:
        f.write(line+"\n")
    for line in correct_list:
        g.write(line+"\n")
    f.close()
    g.close()

main()






