nl_path = "/mnt/ssda/kevinq/OpenNMT-py/data_er2nl/src-train.txt"
sql_path = "/mnt/ssda/kevinq/OpenNMT-py/data_erll2ll/train_ersql.txt"
ll_path = "/mnt/ssda/kevinq/OpenNMT-py/data_erll2ll/train_erasql.txt"

def prepare_data(sql_path,nl_path):
    sqls = []
    nls = []
    with open(sql_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            sqls.append(line.strip())
    with open(nl_path,"r") as g:
        lines = g.readlines()
        for line in lines:
            nls.append(line.strip())
    return sqls,nls

def reloc_tokens(nl_tokens,sql_tokens):
    ll_tokens = []
    rear = 0
    for loc in range(len(nl_tokens)-1):
        rear = loc+1
        tar_tok = nl_tokens[loc]
        # print(tar_tok)
        rear_tok = nl_tokens[rear]
        if tar_tok not in sql_tokens:
            ll_tokens.append(tar_tok)
        else:
            tar_indx = sql_tokens.index(tar_tok)
            if rear_tok not in sql_tokens:
                for tok in sql_tokens[0:tar_indx+1]:
                    ll_tokens.append(tok)
                sql_tokens = sql_tokens[tar_indx:]
            else:
                rear_indx = sql_tokens.index(rear_tok)
                for tok in sql_tokens[0:rear_indx]:
                    ll_tokens.append(tok)
                sql_tokens = sql_tokens[rear_indx:]
    if nl_tokens[-1] not in ll_tokens:
        ll_tokens.append(nl_tokens[-1])
    if len(sql_tokens)>1:
        for tok in sql_tokens:
            ll_tokens.append(tok)
    # raise RuntimeError("sanity check")
    return ll_tokens




def genll(sqls,nls):
    assert len(sqls) == len(nls)
    lls = []
    for i in range(len(sqls)):
        sql = sqls[i]
        nl = nls[i]
        nl_tokens = nl.split(" ")
        sql_tokens = sql.split(" ")
        ll_tokens = reloc_tokens(nl_tokens,sql_tokens)
        ll = " ".join(ll_tokens)
        lls.append(ll)
    return lls


def main():
    sqls,nls=prepare_data(sql_path,nl_path)
    lls = genll(sqls,nls)
    k = open(ll_path,"w")
    for ll in lls:
        k.write(ll+"\n")
    k.close()

main()


