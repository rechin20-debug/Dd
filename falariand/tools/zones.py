import sys, math
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); P=im.load()
R=float(sys.argv[2]); d=math.radians(0.18)
def lum(x,y): r,g,b=P[x,y]; return (r+g+b)/3
def water(x,y): r,g,b=P[x,y]; return b>r+15 and b>=g and (r+g+b)/3>150
zones={'west':(1283,1447,80),'crown':(1447,1577,82),'east':(1577,1679,103)}
for n,(a,b,ylim) in zones.items():
  A=0; cols=0; ys=[]
  for x in range(a,b):
    # find north border: first dark pixel from y=30 downward
    yt=None
    for y in range(30,60):
      if lum(x,y)<110: yt=y; break
    if yt is None: continue
    cols+=1
    for y in range(yt+1,ylim):
      if water(x,y): 
        # stop at first sustained water (3px)
        if all(water(x,y+k) for k in range(3)): break
        continue
      A+=(R*d)**2*math.cos(math.radians(90-(y+0.5)*0.18)); ys.append(y)
  print(n,cols,round(A),min(ys),max(ys), 'lat %.1f-%.1f'%(90-max(ys)*0.18,90-min(ys)*0.18))
print('px km at lat77:', R*d, R*d*math.cos(math.radians(77)))
