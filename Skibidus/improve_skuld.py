def Skibidus (s, pos):
    sum = 0
    q_sum = []
    for i in pos :
        if s[i-1] == '0' :
            s[i-1] = '1'
        else :
            s[i-1] = '0'


        my_full_names = build_skuld(s)

        sub = ''
        for name in my_full_names :
            for i in range(len(name)) :
                sub += s[int(name[i])]
            sum += calc(sub)
            sub = ''

        q_sum.append(sum % 998244353)
        sum = 0

    return q_sum






def skuld(s) :
    my_names = build_dict(s)
    list = []

    for name in my_names :
        sub = name['root']
        for child in name['children'] :
            subs = sub + ','+ child
            list.append(subs)
            subs = ''

    return ultima(my_names, list)



def build_skuld(s) :
    heroes = skuld(s)
    substring = ''
    substring_list = []
    for l in heroes:
        p = l.split(',')
        substring_list.extend(p[j:k] for j in range(len(p)) for k in range(j+1, len(p)+1))

    unique_list = list(map(list, dict.fromkeys(map(tuple, substring_list))))

    unique_list = [sublist for sublist in unique_list if sublist != ['']]

    unique_list = [sublist for sublist in unique_list if sublist]

    return unique_list


def ultima(my_names, list) :
    last = my_names[-1]


    for l in list : 
        last_part = l.rsplit(",", 1)[-1]
        if last_part == last['root'] :
            continue

        else :
            for name in my_names :
                if last_part == name['root']:
                    for child in name['children'] :
                        list.append(l + ','+ child)
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
            

def calc(s) :
    return sum(1 for a, b in zip(s, s[1:]) if a != b) + 1



def build_dict(s) :
    dict_list = []
    for i in range(len(s)):
        children = [str(j) for j in range(i+1, len(s))]
        dict_list.append({'root': str(i), 'children': children})
    return dict_list


def main():
    t = input('Enter the number of test cases : ')
    t = int(t)

    all_my_results = []

    for i in range(t) :
        s = input('Enter the string : ')
        q = input('Enter the number of queries : ')
        q = int(q)

        pos = list(map(int, input('Enter the positions: ').split()))



        s = list(s)
        res = Skibidus(s, pos)

        all_my_results.append(res)

    
    for res in all_my_results :
        print(*res)


        

if __name__ == '__main__':
    main()

