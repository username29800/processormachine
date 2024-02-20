kwd0=''
pc=''
lc=''
ec=''
cr=''
cp=''
ap=''
ll=[]
run=1
def ed(x):
  if str(cp)==str(x):
    return 1
  else:
    return 0
while run:
  try:
    if 1: #input
      ui=str(input('> '))
      cp=ui.split()[0]
      ap=''
      for i in ap[1:]:
        ap=ap+i
    if ed('a'):
      pc=str(pc)+str(ap)
    if ed('l'):
      print(pc+'|'+lc)
    if ed('c'):
      ec=pc+lc
      pc=ec[:int(ap)]
      lc=ec[int(ap):]
    if ed('x'):
      pc=pc[:-int(ap)]
    if ed('d') and ll!=[]:
      del ll[int(ap)-1]
    if ed('o') and ll!=[]:
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append(pc+lc)
      ll=lpc+llc
      pc=''
      lc=''
    if ed('la'):
      ll.append(pc+lc)
      pc=''
      lc=''
    if ed('y'):
      cr=ll[int(ap)-1]
    if ed('n'):
      pc=ll[int(ap)-1]
      lc=''
    if ed('p'):
      pc=pc+cr
    if ed('ls'):
      for i in ll:
        print(str(ll.index(i)),i)
    if ed('lr'):
      for i in ll[ap.split()[0]-1:ap.split[1]-1]:
        print(str(ll.index(i)),i)
    if ed('lrw'):
      for i in ll[ap.split()[0]-1:ap.split[1]-1]:
        print(i)
    if ed('lsw'):
      for i in ll:
        print(i)
    if ed('quit'):
      run=0
    if ed('of'):
      of=open(str(input()),'r')
      ll=of.read().splitlines()
      of.close()
    if ed('wf'):
      op=''
      for i in ll:
        op=op+str(i)+'\n'
      wf=open(str(input()),'w')
      wf.write(op)
      wf.close()
    if ed('ecl'):
      ll=[]
  except:
    pass
