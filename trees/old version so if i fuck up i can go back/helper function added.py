#===================================
#===================================
# Name   : Mujtaba Khalid   
# Roll no: 241547337
# Section: B
# Date   : 23-4-23
#===================================
#===================================



class Node:
    def __init__(self,name,data=None,parent =None,type="directory",children=[]):
        self.name= name
        self.parent = parent
        self.data=data
        self.type= type
        self.children = children



    #-------------HELPER METHODS-------------------

def findNodeFromstrEntireTree(root,current,path,func):
    temp=current
    separatedList=path.split("/")
    found=False
    for i in separatedList[1:]:
        if i=="~":
            temp=root
        elif i==".":
            pass
        elif i=="..":
            if temp.parent:
                temp=temp.parent
            else:
                print(f"{func}: {path}: no such file or directory")
                return
        elif i!="." or i!="..":
            for j in temp.children:
                if j.name == i:
                    found=True
                    temp=j
                    break
    if found==False:
        print(f"{func}: {path}: No such file or directory")
        return None
    return temp

def deepCopyTree(n):
    if n==None:
        return None
    final = Node(name=n.name, data=n.data, parent=None, type=n.type, children=[])

    for i in n.children:
        newChild=deepCopyTree(i)
        newChild.parent=final
        final.children.append(newChild)
    
    return final

def findNode(parent,childName):
    if parent==None:
        return None
    if parent.name==childName:
        return parent
    try:
        for i in parent.children:
            n=findNode(i,childName)
            if n:
                return n
    except:
        return None
    return None


def adddir(childName,parent):
    parent.children.append(Node(name=childName,parent=parent,type="directory",children=[],data=None))

def addfile(childName,childData,parent):
    parent.children.append(Node(name=childName,parent=parent,type="file",data=childData,children=[]))


def iterate(root):
    print(root.name,root.type)
    try:
        for i in root.children:
            if i.type=="directory":
                iterate(i)
            else:
                print(i.name,i.type)
    except:
        print(root.name)

#----------------------------------------------------------------

class VirtualFileSystem:
    def __init__(self):


        self._main=Node(name="/")   #PARENT OF ALL DIRECTORY
        self._currentNode = self._main  #CURRENT POINTER




    def Quit(self):
        print("Terminating current session. Bye...")


    
    def mkdir(self, dir):

        if len(dir)==0:
            print("mkdir: Too few arguments")
            return
        if "/" not in dir:
            adddir(dir,self._currentNode)
            return
        elif "/" in dir:
            separatedList = dir.split("/")
            # checking if the directory exists or 
            if len(separatedList)>2: #if len less than2 probably wrong input
                exists=findNode(self._currentNode,separatedList[1])
                c=1
                while exists and c<len(separatedList)-2: #checking if dir exists
                    c+=1
                    exists=findNode(exists,separatedList[c])
                
                if exists:   #we found the parent node
                    adddir(separatedList[-1],exists)
                else: #not found
                    dir=dir.removesuffix(f"/{separatedList[-1]}")
                    print(f"mkdir: {dir} : No such file or directory")
            else:#len less than 2 ignore / and add to current.children
                adddir(dir.removeprefix("/"),self._currentNode)


    def ls(self,dir):
        if dir=="": #will list the current node chilren
            for i in self._currentNode.children:
                if i.type=="directory":
                    print(f"-d-  {i.name}")
                elif i.type=="file":
                    print(f"-f-  {i.name}")
        elif "/" in dir:
            #checking here if path is correct or not
            separatedList = dir.split("/")
            exists=findNode(self._currentNode,separatedList[1])
            c=1
            while exists and c!=len(separatedList)-1: #checking if dir exists
                c+=1
                exists=findNode(exists,separatedList[c])
            
            if exists:   #we found the parent node now we iterate and print
                for i in exists.children:
                    if i.type=="directory":
                        print(f"-d-  {i.name}")
                    elif i.type=="file":
                        print(f"-f-  {i.name}")
            else:
                print(f"ls: {dir} : No such file or directory")
        else:
            exists=findNode(self._currentNode,dir)
            if exists:
                for i in exists.children:
                    if i.type=="directory":
                        print(f"-d-  {i.name}")
                    elif i.type=="file":
                        print(f"-f-  {i.name}")
            else:
                print(f"ls: {dir} : No such file or directory")


    def touch(self,dir,data):
        if len(dir)==0 and len(data)==0:
            print("touch: Too few arguments")
            return
        if len(dir)==0 and len(data)>0:
            print("touch: Too few arguments")
            return
        if "/" not in dir:
            addfile(dir,data,self._currentNode)
            return
        elif "/" in dir:
            if dir.count("/")==1:
                addfile(dir.removeprefix("/"),data,self._currentNode)
            else:
                 #checking here if path is correct or not
                separatedList = dir.split("/")
                exists=findNode(self._currentNode,separatedList[1])
                c=1
                while exists and c!=len(separatedList)-2: #checking if dir exists
                    c+=1
                    exists=findNode(exists,separatedList[c])
                
                if exists:   
                    addfile(separatedList[-1],data,exists)
                else:
                    dir=dir.removesuffix(f"/{separatedList[-1]}")
                    print(f"touch: {dir} : No such directory")



    def cat(self,dir):
        if len(dir)==0:
            print("cat: Too few arguments")
            return
        
        if "/" not in dir:
            for i in self._currentNode.children:
                if i.name==dir:
                    if i.type=="directory":
                        print(f"cat: {dir}: is a directory")
                        return
                    elif i.type=="file":
                        print(i.data)
                        return
        if "/" in dir:
            #checking here if path is correct or not
            separatedList = dir.split("/")
            exists=findNode(self._currentNode,separatedList[1])
            c=1
            while exists and c!=len(separatedList)-1: #checking if dir exists
                c+=1
                exists=findNode(exists,separatedList[c])
            
            if exists:   #we found the parent node now we iterate and print
                if exists.type=="directory":
                    print(f"cat: {separatedList[-1]}: is a directory")
                elif exists.type=="file":
                    print(exists.data)

            else:
                print(f"cat: {dir} : No such file or directory")


    def cd(self,dir):
        # print("----------------",self._currentNode.name,dir)
        if len(dir)==0:
            print("cd: Too few arguments")
            return
        
        if "/" not in dir:
            for i in self._currentNode.children:
                if i.name==dir:
                    self._currentNode=i
                    return
            print(f"cd: {dir}: No such file or directory")


        if "/" in dir:
            #checking if path is correct or not
            separatedList = dir.split("/")
            for i in separatedList[1:]:
                if i=="`":
                    self._currentNode=self._main
                elif i==".":
                    pass
                elif i=="..":
                    if self._currentNode.parent:
                        self._currentNode=self._currentNode.parent
                    else:
                        print(f"cd: {dir}: no such file or directory")
                        return
                elif i!="." or i!="..":
                    found=False
                    for j in self._currentNode.children:
                        if j.name == i:
                            found=True
                            self._currentNode=j
                            break
                    if found==False:
                        print(f"cd: {dir}: No such file or directory")
                        return
                    
                            

    def pwd(self):
        if self._currentNode.name=="/":
            print("/")
            return
        
        temp=self._currentNode
        li=[]
        while temp!=None:
            li.append(temp.name)
            temp=temp.parent
        li = li[::-1]
        dir= li[0]
        for i in li[1:]:
            dir+=i
            if i!=li[-1]:
                dir +="/"
        print(dir)
        return
    
    def rm(self,dir):
        if len(dir)==0:
            print("rm: Too few arguments")
            return
        
        if "/" not in dir:
            for i in self._currentNode.children:
                if i.name==dir:
                    self._currentNode.children.remove(i)
                    return
            print(f"rm: {dir}: no such file or directory")

        elif "/" in dir:
            #checking if file or directory exists
            separatedList=dir.split("/")
            temp=self._main
            for i in separatedList[1:]:
                found=False
                for j in temp.children:
                    if j.name == i:
                        found=True
                        temp=j
                        break
                if found==False:
                    print(f"rm: {dir}: No such file or directory")
                    return
            temp.parent.children.remove(temp)
                
    def cp(self,source,dir):
        temp=self._main
        if len(dir)==0 or len(source)==0:
            print("cp: Too few arguments")
            return
        
        if "/" not in source:
            #checking if source exists or not
            source0=None
            for i in self._currentNode.children:
                if i.name==source:
                    source0=i #we found source node
                    break
            if source0:
                #we found source
                # checking if destination exists or not
                temp=findNodeFromstrEntireTree(self._currentNode,self._main,dir,"auoooo")
                if temp==None:
                    return
                temp.children.append(deepCopyTree(source0))
                return
            else:
                print(f"cp: {source} no such file or directory")
                return
            #incomplete
        elif "/" in source:
            source0=findNodeFromstrEntireTree()
            


def Main():
    fileSystem = VirtualFileSystem()
    fileSystem.mkdir("mujtaba")
    fileSystem.mkdir("kidnapper")

    fileSystem.mkdir("/mujtaba/minahil")
    fileSystem.mkdir("/mujtaba/maryam")
    fileSystem.mkdir("/mujtaba/minahil/kid1")
    fileSystem.mkdir("/mujtaba/minahil/kid2")
    fileSystem.mkdir("/mujtaba/maryam/kid3")
    fileSystem.mkdir("/mujtaba/maryam/kid4")
    # iterate(fileSystem._currentNode)

    # fileSystem.mkdir("//////")

    print("--------------test cases for mkdir-----------------")
    # print(fileSystem._currentNode.children[0].name=="mujtaba")
    # print(len(fileSystem._currentNode.children[0].children)==2)
    # print(fileSystem._currentNode.children[0].children[0].name=="minahil" and fileSystem._currentNode.children[0].children[1].name=="maryam")
    # print(fileSystem._currentNode.children[0].children[0].children[0].name=="kid1" and fileSystem._currentNode.children[0].children[0].children[1].name=="kid2")
    # print(fileSystem._currentNode.children[0].children[1].children[0].name=="kid3" and fileSystem._currentNode.children[0].children[1].children[1].name=="kid4")

    print("--------------test cases for ls-----------------")
    # fileSystem.ls("")
    # fileSystem.ls("/mujtaba/minahil")
    # fileSystem.ls("///////")
    # fileSystem.ls("//")
    # fileSystem.ls("/")

    print("--------------test cases for touch-----------------")

    
    fileSystem.touch("sadlife.txt","helloJee\nmujtaba here")
    print(fileSystem._currentNode.children[1].data=="helloJee\nmujtaba here" and fileSystem._currentNode.children[1].name=="sadlife.txt" )
    fileSystem.touch("/mujtaba/maryam/ankaraMessi.txt","breakup hogya\nsad emojis")
    print(fileSystem._currentNode.children[0].children[1].children[2].name=="ankaraMessi.txt" and fileSystem._currentNode.children[0].children[1].children[2].data=="breakup hogya\nsad emojis")
    fileSystem.touch("","ankara messi")


    print("--------------test cases for cat-----------------")

    # fileSystem.cat("sadlife.txt")
    # fileSystem.cat("/mujtaba/maryam/ankaraMessi.txt")
    # fileSystem.cat("//////////////")
    # fileSystem.cat("")
    # fileSystem.cat("mujtaba")


    print("---------------test cases for cd-------------")

    # fileSystem.cd("mujtaba")
    # print(fileSystem._currentNode.name=="mujtaba")
    # fileSystem.cd("minahil")
    # print(fileSystem._currentNode.name=="minahil")
    # fileSystem.cd("/../../mujtaba")
    # print(fileSystem._currentNode.name=="mujtaba")
    # fileSystem.cd("/..")
    # print(fileSystem._currentNode.name=="/")
    # fileSystem.cd("/mujtaba/minahil/kid1")
    # print(fileSystem._currentNode.name=="kid1")
    # fileSystem.cd("/`/mujtaba/minahil")
    # print(fileSystem._currentNode.name=="minahil")
    # fileSystem.cd("/`")


    print("---------------test cases for pwd-------------")
    # fileSystem.pwd()
    # fileSystem.cd("/mujtaba/minahil/kid1")
    # fileSystem.pwd()
    # fileSystem.cd("/../../maryam/kid4")
    # fileSystem.pwd()
    # fileSystem.cd("/`")


    print("--------------test cases for rm----------------")
    # fileSystem.rm("/mujtaba/maryam/kid4")
    # fileSystem.ls("/mujtaba/maryam")
    # fileSystem.rm("/")
    # fileSystem.ls("")
    # fileSystem.cd("/`")


    print("-----------------test for cp----------------")
    # fileSystem.cp("mujtaba", "/kidnapper")
    # fileSystem.ls("/kidnapper/mujtaba")
    print(fileSystem._currentNode.name)
    fileSystem.cp("mujtaba", "/mujtaba/minahil/kid1/../../../kidnapper")
    fileSystem.cd("/kidnapper")
    iterate(fileSystem._currentNode)
    

    print("=============================================")
    print(fileSystem._currentNode.name)
    print("=============================================")
    # iterate(fileSystem._main)


Main()
    
