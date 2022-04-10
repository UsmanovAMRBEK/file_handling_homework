def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    digital = 0
    non_digital = 0
    for i in data:
        if i.isdigit():
            digital += 1
        else:
            non_digital += 1
    return [digital, non_digital]
# Read data from file
f=open(".\\txt_file\data05.txt","r")
data=f.read()
print(main(data))
f.close()
