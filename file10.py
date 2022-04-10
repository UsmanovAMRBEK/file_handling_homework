def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split('\n')
    ans = 0
    for row in data:
        if len(row) > ans:
            ans = len(row)
    return ans

# Read data from file
f=open(".\\txt_file\data10.txt","r")
data=f.read()
print(main(data))
f.close()