def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    answer = 0
    for char in data:
        if char.isdigit():
            answer = min(answer, int(char))
    return answer

# Read data from file
f=open("./txt_file/data09.txt","r")
data=f.read()
print(main(data))
f.close()