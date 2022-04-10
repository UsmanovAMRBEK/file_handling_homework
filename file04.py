def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    for i in data:
        if i.isdigit():
            continue
        else:
            l.append(i)
    return l
# Read data from file
f=open(".\\txt_file\data04.txt","r")
data=f.read()
print(main(data))
f.close()