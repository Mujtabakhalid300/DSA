# ===================================
# ===================================
# Name   : Mujtaba Khalid
# Roll no: 241547337
# Section: B
# Date   : 23-4-23
# ===================================
# ===================================


class Node:
    def __init__(self, name, data=None, parent=None, type="directory", children=[]):
        self.name = name
        self.parent = parent
        self.data = data
        self.type = type
        self.children = children

    # -------------HELPER METHODS-------------------


def deepCopyTree(n):
    # this function helps in the copy path and move path function by making a new deep copy of tree given
    if n == None:
        return None
    final = Node(name=n.name, data=n.data, parent=None, type=n.type, children=[])

    for i in n.children:
        newChild = deepCopyTree(i)
        newChild.parent = final
        final.children.append(newChild)

    return final


def findNode(parent, childName):
    # this function finds the node in the parent and returns the reference
    if parent == None:
        return None
    if parent.name == childName:
        return parent
    try:
        for i in parent.children:
            n = findNode(i, childName)
            if n:
                return n
    except:
        return None
    return None


def adddir(childName, parent):
    # this is just a normal function to append a node, made this so i dont clutte the code
    parent.children.append(
        Node(name=childName, parent=parent, type="directory", children=[], data=None)
    )


def addfile(childName, childData, parent):
    # this adds a file instead of a directrory
    parent.children.append(
        Node(name=childName, parent=parent, type="file", data=childData, children=[])
    )


def iterate(root):
    # this function just prints out the entire tree using recursion
    print(root.name, root.type)
    try:
        for i in root.children:
            if i.type == "directory":
                iterate(i)
            else:
                print(i.name, i.type)
    except:
        print(root.name)


# ----------------------------------------------------------------


class VirtualFileSystem:
    def __init__(self):
        self._main = Node(name="/")  # PARENT OF ALL DIRECTORY
        self._currentNode = self._main  # CURRENT POINTER
        self._searchResult = []

    # ----------------------------------------------------------------------#
    # -------------------------helper functions-----------------------------#
    # ----------------------------------------------------------------------#

    def findNodePrinter(self, parent, childName):
        # this is a helper function for the find method, this finds the node and adds it to a list
        # so that i can print the search results
        if parent == None:
            return None
        if parent.name == childName:
            self._searchResult.append(parent)
        try:
            for i in parent.children:
                n = self.findNodePrinter(i, childName)
                if n:
                    return n
        except:
            return None
        return None

    def findNodeFromstrEntireTree(self, path, func):
        # this function checks if a path is correct or not
        # by going over the path and checking if each pathanme
        #  is corrcet in order or not
        if "/" in path:
            temp = self._currentNode
            separatedList = path.split("/")
            found = False
            for i in separatedList[1:]:
                if i == "~":
                    temp = self._main
                elif i == ".":
                    pass
                elif i == "..":
                    if temp.parent:
                        temp = temp.parent
                    else:
                        print(f"{func}: {path}: no such file or directory")
                        return
                elif i != "." or i != "..":
                    for j in temp.children:
                        if j.name == i:
                            found = True
                            temp = j
                            break
            if found == False:
                print(f"{func}: {path}: No such file or directory")
                return None
            return temp
        elif "/" not in path:
            temp = None
            for i in self._currentNode.children:
                if i.name == path:
                    temp = i
                    return temp

    # ----------------------------------------------------------------------#
    # -------------------------helper functions-----------------------------#
    # ----------------------------------------------------------------------#
    def Quit(self):
        # this functions just prints the following line
        # the actually quitting happens in the main function
        print("Terminating current session. Bye...")

    def mkdir(self, dir):
        # checking if argument is correct or not
        if len(dir) == 0:
            print("mkdir: Too few arguments")
            return
        # if / is not present then i can just append a new child in the current directory
        if "/" not in dir:
            adddir(dir, self._currentNode)
            return
        elif "/" in dir:
            # if / is present then i have to check if the path
            # is correct or not and if it is corrcet than i
            # will get the location of the parent and append a
            # directory in the parent

            separatedList = dir.split("/")
            # checking if the directory exists or
            if len(separatedList) > 2:  # if len less than2 probably wrong input
                exists = findNode(self._currentNode, separatedList[1])
                c = 1
                while exists and c < len(separatedList) - 2:  # checking if dir exists
                    c += 1
                    exists = findNode(exists, separatedList[c])

                if exists:  # we found the parent node
                    adddir(separatedList[-1], exists)
                else:  # not found
                    dir = dir.removesuffix(f"/{separatedList[-1]}")
                    print(f"mkdir: {dir} : No such file or directory")
            else:  # len less than 2 ignore / and add to current.children
                adddir(dir.removeprefix("/"), self._currentNode)

    def ls(self, dir):
        # checking if a path is given or not
        if dir == "":  # will list the current node chilren
            for i in self._currentNode.children:
                if i.type == "directory":
                    print(f"-d-  {i.name}")
                elif i.type == "file":
                    print(f"-f-  {i.name}")
        elif "/" in dir:
            # if / is present than i have to
            # check if path is correct or not
            # if correct than i get the last child of the path and list its children
            separatedList = dir.split("/")
            exists = findNode(self._currentNode, separatedList[1])
            c = 1
            while exists and c != len(separatedList) - 1:  # checking if dir exists
                c += 1
                exists = findNode(exists, separatedList[c])

            if exists:  # we found the parent node now we iterate and print
                for i in exists.children:
                    if i.type == "directory":
                        print(f"-d-  {i.name}")
                    elif i.type == "file":
                        print(f"-f-  {i.name}")
            else:
                print(f"ls: {dir} : No such file or directory")
        else:
            exists = findNode(self._currentNode, dir)
            if exists:
                for i in exists.children:
                    if i.type == "directory":
                        print(f"-d-  {i.name}")
                    elif i.type == "file":
                        print(f"-f-  {i.name}")
            else:
                print(f"ls: {dir} : No such file or directory")

    def touch(self, dir, data):
        # checking if the arguments are correct or not
        if len(dir) == 0 and len(data) == 0:
            print("touch: Too few arguments")
            return
        if len(dir) == 0 and len(data) > 0:
            print("touch: Too few arguments")
            return
        if "/" not in dir:
            # if no / in path then i can simply append to the current node
            addfile(dir, data, self._currentNode)
            return
        elif "/" in dir:
            # if / in path then i have to check if path is correct or not
            # than i will find the parent and append the file node to its children
            if dir.count("/") == 1:
                addfile(dir.removeprefix("/"), data, self._currentNode)
            else:
                # checking here if path is correct or not
                separatedList = dir.split("/")
                exists = findNode(self._currentNode, separatedList[1])
                c = 1
                while exists and c != len(separatedList) - 2:  # checking if dir exists
                    c += 1
                    exists = findNode(exists, separatedList[c])

                if exists:
                    addfile(separatedList[-1], data, exists)
                else:
                    dir = dir.removesuffix(f"/{separatedList[-1]}")
                    print(f"touch: {dir} : No such directory")

    def cat(self, dir):
        # checking if arguments are corrcet
        if len(dir) == 0:
            print("cat: Too few arguments")
            return

        if "/" not in dir:
            # if / not in path than i simply find the file in direct children

            for i in self._currentNode.children:
                if i.name == dir:
                    # if it is a file then i print the content
                    # or if it is a directory than i give user a notice
                    if i.type == "directory":
                        print(f"cat: {dir}: is a directory")
                        return
                    elif i.type == "file":
                        print(i.data)
                        return
            print(f"cat: {dir} no such file")
        if "/" in dir:
            # checking here if path is correct or not
            separatedList = dir.split("/")
            exists = findNode(self._currentNode, separatedList[1])
            c = 1
            while exists and c != len(separatedList) - 1:  # checking if dir exists
                c += 1
                exists = findNode(exists, separatedList[c])

            if exists:  # we found the parent node now we iterate and print
                if exists.type == "directory":
                    print(f"cat: {separatedList[-1]}: is a directory")
                elif exists.type == "file":
                    print(exists.data)

            else:
                print(f"cat: {dir} : No such file or directory")

    def cd(self, dir):
        # checking if the arguments are correct
        if len(dir) == 0:
            print("cd: Too few arguments")
            return
        # checking if ~ . or .. is given as argument
        if len(dir) == 1:
            if dir == "~":
                self._currentNode = self._main
                return
            elif dir == "..":
                self._currentNode = self._currentNode.parent
                return
            elif dir == ".":
                return
        if "/" not in dir:
            # if / not in path then i simply check it in the direct children of current node
            for i in self._currentNode.children:
                if i.name == dir:
                    self._currentNode = i
                    return
            print(f"cd: {dir}: No such file or directory")

        if "/" in dir:
            # checking if / is given then i iterate over the path and see if correct or not
            # checking if path is correct or not
            separatedList = dir.split("/")
            for i in separatedList[1:]:
                if i == "`":
                    self._currentNode = self._main
                elif i == ".":
                    pass
                elif i == "..":
                    if self._currentNode.parent:
                        self._currentNode = self._currentNode.parent
                    else:
                        print(f"cd: {dir}: no such file or directory")
                        return
                elif i != "." or i != "..":
                    found = False
                    for j in self._currentNode.children:
                        if j.name == i:
                            found = True
                            self._currentNode = j
                            break
                    if found == False:
                        print(f"cd: {dir}: No such file or directory")
                        return

    def pwd(self):
        # if current node is / then it will simply return /
        if self._currentNode.name == "/":
            print("/")
            return
        # else it will save all the parents of the current node in temp
        temp = self._currentNode
        li = []
        while temp != None:
            li.append(temp.name)
            temp = temp.parent
        li = li[::-1]
        dir = li[0]
        # it will join all the string here in the for loop and finally it will print
        for i in li[1:]:
            dir += i
            if i != li[-1]:
                dir += "/"
        print(dir)
        return

    def rm(self, dir):
        # checking if correct arguments are given
        if len(dir) == 0:
            print("rm: Too few arguments")
            return

        if "/" not in dir:
            # if / not in path then i find it in direct child of the current node
            # and then i remove it from its children
            for i in self._currentNode.children:
                if i.name == dir:
                    self._currentNode.children.remove(i)
                    return
            print(f"rm: {dir}: no such file or directory")

        elif "/" in dir:
            # checking if file or directory exists
            separatedList = dir.split("/")
            temp = self._main
            for i in separatedList[1:]:
                found = False
                for j in temp.children:
                    if j.name == i:
                        found = True
                        temp = j
                        break
                if found == False:
                    print(f"rm: {dir}: No such file or directory")
                    return
            # if found then i remove it from the parent's childrne list
            temp.parent.children.remove(temp)

    def cp(self, source, dir):
        # checking for correct arguments
        if len(dir) == 0 or len(source) == 0:
            print("cp: Too few arguments")
            return
        # using helper function to find the source to copy
        source0 = self.findNodeFromstrEntireTree(source, "cp")
        # we found source
        if source0:
            # now we find the destinaion
            destination = self.findNodeFromstrEntireTree(dir, "cp")
            if destination:
                same = None
                for i in destination.children:
                    if source0.name == i.name:
                        same = i
                        break
                if same:
                    destination.children.remove(same)
                # making a deep copy and then simply appending it to the destinations's children
                destination.children.append(deepCopyTree(source0))
                return

            else:
                print(f"cp: {dir}: no such file or directory exists")
                return
        else:
            print(f"cp: {source}: no such file or directory exists")
            return

    def mv(self, source, dir):
        # checking if the arguments are correct
        if len(dir) == 0 or len(source) == 0:
            print("mp: Too few arguments")
            return
        # this function is almost same as copy file but
        # here we also remove the tree from the source unlike
        # in copy path(cp)
        source0 = self.findNodeFromstrEntireTree(source, "cp")
        # we found source
        if source0:
            # now we find the destinaion
            destination = self.findNodeFromstrEntireTree(dir, "cp")
            if destination:
                # adding to the destination
                destination.children.append(deepCopyTree(source0))
                # deleting the source
                source0.parent.children.remove(source0)
                return

            else:
                print(f"cp: {dir}: no such file or directory exists")
                return
        else:
            print(f"cp: {source}: no such file or directory exists")
            return

    def find(self, searchPath, search):
        # checking for correct arguments
        if len(searchPath) == 0 or len(search) == 0:
            print(f"find: to few arguments")
            return

        if searchPath == "/":
            # if / is the path meaning it will search in the complete tree
            searchPathNode = self._main
            currentNode = self._currentNode
            print("Search Results:\n")
            # using helper function to find all such nodes and appending
            # the references in a class variable list called _searchResult
            self.findNodePrinter(searchPathNode, search)
            # to print there paths i use the pwd method
            # temporarily changing the current node location and print printing the path
            for i in self._searchResult:
                self._currentNode = i
                self.pwd()
            print(f"\n{len(self._searchResult)} result(s) found")
            # reseting the _currentNode class variable that was changed
            self._currentNode = currentNode
            self._searchResult = []
            return

        # checking if searchpath actually exists or not
        searchPathNode = self.findNodeFromstrEntireTree(searchPath, "find")
        if searchPathNode:
            currentNode = self._currentNode
            print("Search Results:")
            self.findNodePrinter(searchPathNode, search)
            for i in self._searchResult:
                self._currentNode = i
                self.pwd()
            print(f"\n{len(self._searchResult)} results found")
            self._currentNode = currentNode
            self._searchResult = []
            return


def Main():
    fileSystem = VirtualFileSystem()

    print("=============================")
    print("DSA Project 3")
    print("-----------------------------")
    print("Virtual File System Emulator")
    print("=============================")

    exit = False
    while not exit:
        statement = input("Mujtaba: ~$ ")
        save = statement
        # special case of touch command since it has a content arguments enclosed
        # by "" signs and that needs to be processed differently when we use .split()
        # method
        if "'" in statement or '"' in statement:
            touchSplit = statement.split()
            if len(touchSplit) < 2:
                pass
            else:
                text = " ".join(touchSplit[2:])
                fileSystem.touch(touchSplit[1], text[1:-1])
                continue
        # spliting the command on " " spaces to identify the function
        statement = statement.split()

        # if length is only 1 meaning the functions can only be exit,pwd or ls
        if len(statement) == 1:
            if statement[0] == "exit":
                fileSystem.Quit()
                exit = True
            elif statement[0] == "pwd":
                fileSystem.pwd()
            elif statement[0] == "ls":
                fileSystem.ls("")
            else:
                print(f"No such internal or external command: {save}")
        # if length is 2 the it could be mkdir,ls,touch,cat,cd,rm
        elif len(statement) == 2:
            if statement[0] == "mkdir":
                fileSystem.mkdir(statement[1])
            elif statement[0] == "ls":
                fileSystem.ls(statement[1])
            elif statement[0] == "touch":
                fileSystem.touch(statement[1], "")
            elif statement[0] == "cat":
                fileSystem.cat(statement[1])
            elif statement[0] == "cd":
                fileSystem.cd(statement[1])
            elif statement[0] == "rm":
                fileSystem.rm(statement[1])
            else:
                print(f"No such internal or external command: {save}")
        # if length is 3 then the function can be one of find,mv or cp
        elif len(statement) == 3:
            if statement[0] == "find":
                fileSystem.find(statement[1], statement[2])
            elif statement[0] == "mv":
                fileSystem.mv(statement[1], statement[2])
            elif statement[0] == "cp":
                fileSystem.cp(statement[1], statement[2])
            else:
                print(f"No such internal or external command: {save}")

        else:
            print(f"No such internal or external command: {save}")


# calling the main function
Main()
