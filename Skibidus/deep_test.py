def flip_bit(input_string, position):
    """
    Flips the bit at the given position in the input string.
    Positions are 1-indexed.
    """
    if position < 1 or position > len(input_string):
        raise ValueError("Position is out of bounds.")
    input_string[position - 1] = '1' if input_string[position - 1] == '0' else '0'
    return input_string

def calc(s):
    """
    Calculates the number of transitions between '0' and '1' in the string.
    """
    if not s:
        return 0
    transitions = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            transitions += 1
    return transitions

def build_dict(input_string):
    """
    Builds a dictionary of roots and children for the input string.
    Each root is a character index, and its children are subsequent indices.
    """
    return [
        {'root': str(i), 'children': [str(j) for j in range(i + 1, len(input_string))]}
        for i in range(len(input_string))
    ]

def skuld(input_string):
    """
    Generates a list of substrings based on the input string.
    """
    my_names = build_dict(input_string)
    substring_list = []
    for name in my_names:
        root = name['root']
        for child in name['children']:
            substring_list.append(f"{root},{child}")
    return ultima(my_names, substring_list)

def ultima(my_names, substring_list):
    """
    Processes the list of substrings to append children to the last part of each substring.
    """
    last = my_names[-1]
    new_substrings = []
    for l in substring_list:
        last_part = l.rsplit(",", 1)[-1]
        if last_part == last['root']:
            new_substrings.append(l)
        else:
            for name in my_names:
                if last_part == name['root']:
                    for child in name['children']:
                        new_substrings.append(f"{l},{child}")
                    break
    return clean_list(new_substrings)

def clean_list(substring_list):
    """
    Filters out substrings that start with '0' and removes redundant substrings.
    """
    filtered_list = [l for l in substring_list if l[0] == '0']
    return ultima_clean(filtered_list)

def ultima_clean(substring_list):
    """
    Removes substrings that are contained within other substrings.
    """
    to_delete = set()
    for i in range(len(substring_list)):
        for j in range(len(substring_list)):
            if i != j and substring_list[i] in substring_list[j]:
                to_delete.add(substring_list[i])
    return [l for l in substring_list if l not in to_delete]

def build_skuld(input_string):
    """
    Generates unique substrings from the input string.
    """
    heroes = skuld(input_string)
    unique_substrings = set()
    for l in heroes:
        parts = l.split(',')
        for j in range(len(parts)):
            for k in range(j + 1, len(parts) + 1):
                substring = ','.join(parts[j:k])
                if substring:
                    unique_substrings.add(substring)
    return list(unique_substrings)

def Skibidus(input_string, positions):
    """
    Processes the input string and positions to compute results.
    """
    query_results = []
    for pos in positions:
        input_string = flip_bit(input_string, pos)
        substrings = build_skuld(input_string)
        total = 0
        for substring in substrings:
            total += calc(substring.split(','))
        query_results.append(total % 998244353)
    return query_results

def main():
    """
    Main function to handle input and output.
    """
    try:
        t = int(input('Enter the number of test cases: '))
        all_results = []
        for _ in range(t):
            input_string = list(input('Enter the string: '))
            q = int(input('Enter the number of queries: '))
            positions = list(map(int, input('Enter the positions: ').split()))
            if len(positions) != q:
                raise ValueError("Number of positions must match the number of queries.")
            results = Skibidus(input_string, positions)
            all_results.append(results)
        for result in all_results:
            print(*result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()