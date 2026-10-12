import sys, math
from PIL import Image
from collections import deque
im=Image.open(sys.argv[1]).convert('RGB'); P=im.load()
x0,x1,y0,y1=1270,1700,30,115
w,h=x1-x0,y1-y0
def cls(x,y):
  r,g,b=P[x+x0,y+y0]; l=(r+g+b)/3
  if l<90: return 0      # border
  if b>r+15 and b>=g and l>150: return 1  # water
  return 2
C=[[cls(x,y) for x in range(w)] for y in range(h)]
lab=[[-1]*w for _ in range(h)]; comps=[]
for y in range(h):
  for x in range(w):
    if C[y][x]==2 and lab[y][x]<0:
      q=deque([(y,x)]); lab[y][x]=len(comps); pts=[]; edge=False
      while q:
        cy,cx=q.popleft(); pts.append((cy,cx))
        if cy==0 or cx==0 or cx==w-1 or cy==h-1: edge=True
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
          ny,nx=cy+dy,cx+dx
          if 0<=ny<h and 0<=nx<w and C[ny][nx]==2 and lab[ny][nx]<0:
            lab[ny][nx]=len(comps); q.append((ny,nx))
      comps.append((pts,edge))
R=float(sys.argv[2]); d=math.radians(0.18)
def area(pts): return sum((R*d)**2*math.cos(math.radians(90-(y+y0+0.5)*0.18)) for y,x in pts)
res=[]
for pts,edge in comps:
  if len(pts)<3: continue
  xs=[p[1]+x0 for p in pts]; ys=[p[0]+y0 for p in pts]
  res.append((min(xs),max(xs),min(ys),max(ys),len(pts),round(area(pts)),edge))
res.sort()
for t in res: print(t)
