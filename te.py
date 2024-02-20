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
      for i in ui[1:]:
        ap=ap+i
      ap=ap[1:]
    if ed('a'): #append prev cursor
      pc=str(pc)+str(ap)
    if ed('l'): #print current line
      print(pc+'|'+lc)
    if ed('c'): #set cursor
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
    if ed('p'): #paste
      pc=pc+cr
    if ed('l.'): #print lines, indexed
      for i in range(len(ll)):
        print(str(i),ll[i])
    if ed('lm'): #print lines, indexed, with range
      for i in range(int(ap.split()[0])-1,len(ll[:int(ap.split()[1])])):
        print(str(i),ll[i])
    if ed('lp.'): #print lines, not indexed, with range
      for i in range(int(ap.split()[0])-1,len(ll[:int(ap.split()[1])])):
        print(ll[i])
    if ed('lp'): #print lines, not indexed
      for i in ll:
        print(i)
    if ed('quit'):
      run=0
    if ed('of'): #open file
      of=open(str(input()),'r')
      ll=of.read().splitlines()
      of.close()
    if ed('wf'): #write to file
      op=''
      for i in ll:
        op=op+str(i)+'\n'
      wf=open(str(input()),'w')
      wf.write(op)
      wf.close()
    if ed('ecl'): #clear all editor lines
      ll=[]
  except:
    pass
