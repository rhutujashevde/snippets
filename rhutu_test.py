# lis = [1,2,3,4,5,6,7,8,9,88,77,66,55,44,33,22]
# lis1 = [(1,2),(3,4),(5,6)]
# from kyc_validation.rhutu_test import *
# main_fun(lis)

def main_fun(lis):
    type_ = "multiple" if type(lis[0]) == tuple else "single"
    temp = get_str_w_brackets(lis, type_)
    max_len = 10
    ind1,ind2=max_len, 0
    while ind2 < len(temp):
        ind1 = temp.find("),",ind1) + 1
        res_id_sliced = temp[ind2:ind1]
        if ind1 == 0:
            res_id_sliced = temp[ind2:]
            final_query = """insert into jumbo_write.aa_temp_res_ids values """+res_id_sliced
            print final_query
            break
        final_query = """insert into jumbo_write.aa_temp_res_ids values """+res_id_sliced
        ind2,ind1 = ind1+1,ind1+max_len
        print final_query

def get_str_w_brackets(lis, type_="single"):
    # type can also be "multiple"
    if type_ == "single":
        return "("+"),(".join(map(str,lis))+")"
    elif type_ == "multiple":
        return str(lis).strip("[]")
