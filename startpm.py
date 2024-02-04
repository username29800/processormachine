#needed lists
#1. IfExec, in matrix form (same as list array)
#2. Register, in matrix form
#base modules
#1. input interface
#2. input parser
#3. repeater(test component)
#4. auto Helloworld
#5. argument repeater

l1=[] #L1
le=[] #Le=IfExec
for i in range(32):
  l1.append([])
  le.append([])
le[0]=[1,1,0,0,1,1,0,0,0,0,0]
le[1]=[0,0,0]
# IfExec reservations:
  # 0: core components(interface and test)
  # 1: basic applications(calc, text, etc.)
  # 2: user extensions(third-party applications)
l1[0].extend([0,0])
def fadr(flag):
  for i in range(1,len(l1)):
        if l1[i]!=[]:
          if l1[i][0]==flag:
            return i
while le[0][0]:
  # module substructure
  # 1. memory allocation and registration
  # MemReg format: list sublist amount
  # 2. functional section
  # 3. memory unregistration
  if le[0][1]: #1. main interface init
    l1[0][0]=(0,1,3)
    l1[0][1]=0
    while l1[0][1]>=0:
      if l1[l1[0][1]]==[]:
        for i in range(l1[0][0][2]+1):
          l1[l1[0][1]].append(0)
        l1[l1[0][1]][0]=l1[0][0]
        l1[0][1]=-1
        le[0][1]=0
        le[0][2]=1
      else:
        l1[0][1]+=1
  if le[0][2]: #2. main input
    l1[fadr((0,1,3))][1]=input()
  if le[0][3]: #3. repeater
    print(l1[fadr((0,1,3))][1])
  if le[0][4]: #4. argument parser
    try:
      l1[fadr((0,1,3))][2]=l1[fadr((0,1,3))][1].split()[0]
      l1[fadr((0,1,3))][3]=''
      for i in l1[fadr((0,1,3))][1].split()[1:]:
        l1[fadr((0,1,3))][3]=l1[fadr((0,1,3))][3]+str(i)+' '
      l1[fadr((0,1,3))][3]=l1[fadr((0,1,3))][3][:-1]
    except:
      pass
  if le[0][5]: #5. command dictionary
    l1[0][0]=(0,5,3)
    l1[0][1]=0
    while l1[0][1]>=0:
      if l1[l1[0][1]]==[]:
        for i in range(l1[0][0][2]+1):
          l1[l1[0][1]].append(0)
        l1[l1[0][1]][0]=l1[0][0]
        l1[0][1]=-1
        le[0][5]=0
        le[0][6]=1
      else:
        l1[0][1]+=1
  if le[0][6]: #6. cd functional
    l1[fadr((0,5,3))][1]=['rpt','quit','rarg','hw','pl','text']
    l1[fadr((0,5,3))][2]=[0,0,0,0,0,1]
    l1[fadr((0,5,3))][3]=[3,7,8,9,10,0]
    try:
      le[l1[fadr((0,5,3))][2][l1[fadr((0,5,3))][1].index(l1[fadr((0,1,3))][1])]][l1[fadr((0,5,3))][3][l1[fadr((0,5,3))][1].index(l1[fadr((0,1,3))][1])]]=1-le[l1[fadr((0,5,3))][2][l1[fadr((0,5,3))][1].index(l1[fadr((0,1,3))][1])]][l1[fadr((0,5,3))][3][l1[fadr((0,5,3))][1].index(l1[fadr((0,1,3))][1])]]
      #print(le[l1[fadr((0,5,3))][2][l1[fadr((0,5,3))][1].index(l1[1][1])]][l1[fadr((0,5,3))][3][l1[fadr((0,5,3))][1].index(l1[1][1])]])
    except:
      pass
  if le[0][7]: #7. quit
    le[0][0]=0
  if le[0][8]: #8. print argument
    print(l1[fadr((0,1,3))][3])
  if le[0][9]: #9. auto helloworld
    l1[0][0]=(0,9,1)
    l1[0][1]=0
    while l1[0][1]>=0:
      if l1[l1[0][1]]==[]:
        for i in range(l1[0][0][2]+1):
          l1[l1[0][1]].append(0)
        l1[l1[0][1]][0]=l1[0][0]
        l1[0][1]=-1
        le[0][9]=0
      else:
        l1[0][1]+=1
    l1[fadr((0,9,1))][1]="Hello, world!"
    print(l1[fadr((0,9,1))][1])
    l1[fadr((0,9,1))]=[]
  if le[0][10]: #10. print lists
    print(l1)
  if le[1][0]: #1. text editor
    #memory allocation
    l1[0][0]=(1,0,3)
    l1[0][1]=0
    while l1[0][1]>=0:
      if l1[l1[0][1]]==[]:
        for i in range(l1[0][0][2]+1):
          l1[l1[0][1]].append(0)
        l1[l1[0][1]][0]=l1[0][0]
        l1[0][1]=-1
        le[1][0]=0
        le[1][1]=1
      else:
        l1[0][1]+=1
  if le[1][1]: #text editor functional part
    pass
