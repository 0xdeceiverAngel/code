
import random


inp = [[1,1,1,2,3],
[1,2,1,2,3],
[1,1,1,2,2]]

for i in inp:
    print(i)
print()

walked = set()
def fill(mat,y,x,oldv, newv):
    if (
        y<0 or y >= len(mat) or x<0 or x >= len(mat[0]) 
        or mat[y][x] == newv or mat[y][x] != oldv or (y,x)  in walked
        ):
        return
    walked.add((y,x))
    
    for i in mat:
        print(i)

    print(y,x,oldv,newv)
    print()
    
    mat[y][x]=newv
    fill(mat,y-1,x,oldv, newv)
    fill(mat,y+1,x,oldv, newv)
    fill(mat,y,x+1,oldv, newv)
    fill(mat,y,x-1,oldv, newv)

K=0
for y in range(3):
    for x in range(5):
        if (y,x) not in walked:
            #nv=random.randint(50,100)
            #fill(inp,y,x,inp[y][x],nv)
            fill(inp,y,x,inp[y][x],K)
            K=K+1




for i in inp:
    print(i)

se =set()
for i in inp:
    for j in i:
        se.add(j)

print(len(se))
