def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    while i<len(list1):
        if list1[0]!=list1[i]:
            return False
        i+=1
    return True
print(main(list1=[0,0,0,0,0]))
print(main(list1=[1,2,0,3,4,0]))