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
      for i in ui.split()[1:]:
        ap=ap+' '+i
      ap=ap[1:]
    if ed('a'): #append prev cursor
      pc=str(pc)+str(ui[2:])
    if ed('l'): #print current line
      print(pc+'|'+lc)
    if ed('p'): #set pointer
      ec=pc+lc
      pc=ec[:int(ap)]
      lc=ec[int(ap):]
    if ed('x'): #delete char, prev cursor
      pc=pc[:-int(ap)]
    if ed('d') and ll!=[]: #delete line
      del ll[int(ap)-1]
    if ed('o') and ll!=[]: #insert line
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append(pc+lc)
      ll=lpc+llc
      pc=''
      lc=''
    if ed('lo'): #append line
      ll.append(pc+lc)
      pc=''
      lc=''
    if ed('y'): #yank
      cr=ll[int(ap)-1]
    if ed('n'): #set line
      pc=ll[int(ap)-1]
      lc=''
    if ed('pi'): #paste into
      pc=pc+cr
    if ed('l.'): #print lines, indexed
      li=1
      for i in ll:
        print(str(li),i)
        li+=1
    if ed('lm'): #print lines, indexed, with range
      li=1
      for i in ll[int(ap.split()[0])-1:int(ap.split()[1])]:
        print(str(int(ap.split()[0])+li-1),i)
        li+=1
    if ed('ml'): #print lines, not indexed, with range
      for i in ll[int(ap.split()[0])-1:int(ap.split()[1])]:
        print(i)
    if ed('.l'): #print lines, not indexed
      for i in ll:
        print(i)
    if ed('quit'):
      run=0
    if ed('of'): #open file
      of=open(str(ap),'r')
      ll=of.read().splitlines()
      of.close()
    if ed('wf'): #write to file
      op=''
      for i in ll:
        op=op+str(i)+'\n'
      wf=open(str(ap),'w')
      wf.write(op)
      wf.close()
    if ed('ecl'): #clear all editor lines
      ll=[]
    if ed('fn'): #forward search with count
      pa=ap.split()
      pa[0]=str(pa[0])
      pa[1]=int(pa[1])
      for p in range(pa[1]):
        pc=pc+lc[0]
        lc=lc[1:]
        for i in range(len(lc)):
          if lc[i:i+len(pa[0])]==pa[0]:
            pc=pc+lc[:i]
            lc=lc[i:]
            break
    if ed('bn'): #backward search with count
      pa=ap.split()
      pa[0]=str(pa[0])
      pa[1]=int(pa[1])
      for p in range(pa[1]):
        lc=pc[-1]+lc
        pc=pc[:-1]
        for i in range(len(pc),0,-1):
          if pc[i-len(pa[0]):i]==pa[0]:
            uc=pc+lc
            pc=uc[:i]
            lc=uc[i:]
            break
    if ed('pl'): #move pointer to the end of the line
      pc=pc+lc
      lc=''
    if ed('pp'): #set relative cursor position
      if ap[0]=='0':
        ap=-int(ap)
      else:
        ap=int(ap)
      cc=len(pc)
      uc=pc+lc
      pc=uc[:cc+ap]
      lc=uc[cc+ap:]
  except Exception as xp:
    print(xp)
