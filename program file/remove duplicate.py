def remove_dup(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    return a
list1=list(map(int,input().split()))
dup=remove_dup(list1)
print(dup)
# def remove_duplicates_no_set(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result

# # Example usage
# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = remove_duplicates_no_set(original_list)
# print(unique_list) 