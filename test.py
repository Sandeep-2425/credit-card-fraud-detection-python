# text="india"


# def first_non_repeating(s):
#     seen={}
#     for ch in s:
#         seen[ch]=seen.get(ch,0)+1

#     for ch in s:
#         if seen[ch]==1 :
#             return ch

#     return None


# result= first_non_repeating(text)

# print("first non repeating character:",result)


str1="dearsa"
str2="resada"

def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False

    freq={}

    for ch in s1 :
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s2 :
        if ch not in freq :
            return False
        freq[ch] = freq[ch] -1
        if freq[ch] < 0 :
            return False

    for value in freq.values():
        if value != 0 :
            return False

    return True


if is_anagram(str1 ,str2):
    print("anagram")
else:
    print(" not anagram")