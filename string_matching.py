def string_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    
    
    for i in range(n-m+1):
        match= True
        for j in range(m):
            if text[i+j]!= pattern[j]:
                match=False
                break
        if match:
            return i
    return -1


text=input("enter the text:")   
pattern=input("enter the pattern to be search")
result=string_matching(text,pattern)
if result!=-1:
    print(f"pattern found at index{result}")
else:
    print('pattern does not found')