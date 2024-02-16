kwd0=''
pc=''
lc=''
ec=''
cr=''
ll=[]
run=1
def ed(x):
  if str(ui)==str(x):
    return 1
  else:
    return 0
while run:
  try:
    if 1: #input
      ui=input('> ')
    if ed('a'):
      pc=str(pc)+str(input())
    if ed('l'):
      print(pc+'|'+lc)
    if ed('c'):
      ec=pc+lc
      nc=input()
      pc=ec[:int(nc)]
      lc=ec[int(nc):]
    if ed('x'):
      pc=pc[:-int(input())]
    if ed('d') and ll!=[]:
      ll[int(input())-1]=[]
    if ed('o'):
      ln=int(input())-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append('')
      lpc[-1]=pc+lc
      ll=lpc+llc
      pc=''
      lc=''
    if ed('la'):
      ll.append('')
      ll[-1]=pc+lc
      pc=''
      lc=''
    if ed('y'):
      cr=ll[int(input())-1]
    if ed('n'):
      pc=ll[int(input())-1]
      lc=''
    if ed('p'):
      pc=pc+cr
    if ed('ls'):
      for i in ll:
        print(i)
    if ed('quit'):
      run=0
    if ed('cl'):
      lb=[]
      for i in ll:
        if i!=[]:
          lb.append(i)
      ll=lb
    if ed('of'):
      of=open(str(input()),'r')
      ll=of.read().splitlines()
      of.close()
    if ed('wf'):
      op=''
      for i in ll:
        op=op+str(i)+'\n'
      op=op[:-1]
      wf=open(str(input()),'w')
      wf.write(op)
      wf.close()
    if ed('ecl'):
      ll=[]
  except:
    pass
