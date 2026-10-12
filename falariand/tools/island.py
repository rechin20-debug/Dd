import sys, math
from PIL import Image
from collections import deque
im=Image.open(sys.argv[1]).convert('RGB'); P=im.load(); W,H=im.size
R=9556; d=math.radians(0.18)
def water(x,y):
  r,g,b=P[x,y]; return b>r+15 and b>=g and (r+g+b)/3>150
def lat(y): return 90-(y+0.5)*0.18
def lon(x): return (x+0.5)*0.18
def fill(sx,sy):
  seen={(sx,sy)}; q=deque([(sx,sy)])
  while q:
    x,y=q.popleft()
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      n=(x+dx,y+dy)
      if 0<=n[0]<W and 0<=n[1]<H and n not in seen and not water(*n):
        seen.add(n); q.append(n)
  return seen
def area(pts): return sum((R*d)**2*math.cos(math.radians(lat(y))) for x,y in pts)
def dist(a,b):
  p1,p2=math.radians(lat(a[1])),math.radians(lat(b[1])); dl=math.radians(lon(b[0])-lon(a[0]))
  return R*math.acos(min(1,math.sin(p1)*math.sin(p2)+math.cos(p1)*math.cos(p2)*math.cos(dl)))
wadun=(1565,74)
for name,seed in [('south island',(1485,120)),('terluff land',(1555,151))]:
  pts=fill(*seed)
  if len(pts)>200000: print(name,'leaked'); continue
  xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
  near=min(pts,key=lambda p:dist(wadun,p))
  print(name, len(pts),'px', round(area(pts)),'km2', 'x',min(xs),max(xs),'y',min(ys),max(ys),
        'lat %.1f-%.1f'%(lat(max(ys)),lat(min(ys))), 'nearest pt to Wadun',near, round(dist(wadun,near)),'km')
print('Wadun lat %.1f'%lat(74))
