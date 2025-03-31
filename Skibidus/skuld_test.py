
def build_dict(s) :
    dic_list = []
    for i in range(0, len(s)) :
        dic = {
            'root' : str(i),
            'children' : []
        }

        for j in range(i+1, len(s)) :
            dic['children'].append(str(j))

        dic_list.append(dic)

    return dic_list



def skuld(s) :
    my_names = build_dict(s)
    list = []

    for name in my_names :
        sub = name['root']
        for child in name['children'] :
            subs = sub + child
            list.append(subs)
            subs = ''

    return ultima(my_names, list)


def adjust_lenght(list_of_names, lenght, my_names) :
    last = my_names[-1]
    for l in list_of_names :
        if len(l) < lenght and l[-1] == last[-1]:
            list_of_names.remove(l)

    return list_of_names




def ultima(my_names, list) :
    last = my_names[-1]
    #print(last['root'])
    #print(list)
    for l in list : 
        #print(l)
        if l[-1] == last['root'] :
            #print(l)
            continue

        else :
            #print(l)
            current = l
            for name in my_names :
                if l[-1] == name['root']:
                    for child in name['children'] :
                        list.append(l + child)
                    break
            continue


        

    return clean_list(list)



def clean_list(list) :
    clean = []
    for l in list :
        if l[0] == '0' :
            clean.append(l)

    return ultima_clean(clean)


def ultima_clean(clean):
    to_del = []
    for a in clean :
        for c in clean :
            if a in c and a != c :
                to_del.append(a)
                break
    
    filtered_list = [x for x in clean if x not in to_del]

    return filtered_list


def build_skuld(s) :
    heroes = skuld(s)
    substring = ''
    substring_list = []
    for l in heroes :
        for  j in range(len(l)+1) :
            for k in range(j , len(l)+1):
                substring = l[j:k]
                substring_list.append(substring)
                substring = ''

    unique_list = list(dict.fromkeys(substring_list))

    if '' in unique_list :
        unique_list.remove('')

    return unique_list

def main() :
    s = 'hamza'
    lenght = 3
    print(build_skuld(s))

if __name__ == '__main__' :
    main()
