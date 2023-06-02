import random
from os.path import exists
#===================================
#===================================
# Name   : Mujtaba Khalid
# Roll no: 241547337
# Section: B
# Date   : 
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
#------------------------------------

class TextEditor:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.doc = None        # The root of everything. See page 3 for details
        
        #======================
        # Insert your Member
        #   variables here (if any):
        self.cursor = [-1,-1,None,None]
        self.head = None
        self.tail=None
        
        #----------------------
        
    def randomChar(self):
        
        my_string = "ABCDEFGHIJKLMNOPQRSTUVW1234567890"
        return random.choice(my_string)
        #======================
    def loop(self):
        temp=self.doc
        i=0
        while temp !=None:
            t = temp.data
            j=0
            while t != None:
                j+=1
                t=t.next
            i+=1
            temp=temp.next
    
    def reverseLoop(self):
        temp = self.doc
        while temp.next!=None:
            temp=temp.next
        
        tail = temp

        temp2 = tail
        i=0
        while temp2!=None:
            t = temp2.data
            j=0
            while t != None:
                j+=1
                t=t.next
            i+=1
            temp2=temp2.prev
    def crazyLoop(self):
        temp = self.doc
        while temp.next != None:
            temp=temp.next
        temp = temp.data
        while temp.next!=None:
            temp=temp.next
        tail = temp
        while tail:
            tail=tail.prev
            
            




    
        
#======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        # ignores invalid inputs
        if row<0 or col<0:
            print("INVALID ARGUMENTS.")
            return
        
        # if doc is empty and no linked list exists
        if self.cursor ==[-1,-1,None,None]:
            for i in range(row+1):
                tempGreenNode = Node(None)
                if self.head ==None:
                    self.head = tempGreenNode
                    self.tail = tempGreenNode
                else:
                    tempGreenNode.prev = self.tail
                    self.tail.next = tempGreenNode
                    self.tail = tempGreenNode
            
            self.doc=self.head
            pinkNodehead=None
            pinkNodeTail = None
            for j in range(col+1):
                tempPinkNode = Node(" ")
                if pinkNodehead==None:
                    pinkNodehead=tempPinkNode
                    pinkNodeTail=tempPinkNode
                else:
                    tempPinkNode.prev=pinkNodeTail
                    pinkNodeTail.next=tempPinkNode
                    pinkNodeTail=tempPinkNode
            pinkNodehead.prev=self.tail
            self.tail.data = pinkNodehead
            self.cursor=[row,col, pinkNodeTail,self.tail]
        # if doc is not empty meaning it has some data in it already
        else:
        # checking if the row exists already or not
            r=0
            temp=self.doc
            rowExists=False
            while temp:
                if r==row:
                    rowExists = True
                    rowRequried = temp
                    break

                r+=1
                
                temp= temp.next
            # else:
            #     rowExists=True
            #     rowRequried=self.doc
                
            
            # if row exits already then we check if the column node exits
            colexists=False
            if rowExists:
                c = 0
                
                head = rowRequried.data
                while head:
                    if c == col:
                        colexists=True
                        finalCurrentNode= head
                        break
                    c+=1
                    head = head.next
                # else:
                #     colexists=True
                #     finalCurrentNode=
            
           
            # now we know if the row or col exits
            # this way we can calculate if we need to make changes to the 
            # green nodes only or also the pink nodes
            # if row exits we only need to change the pink nodes
            # if row doesnt exits we need to make the pink nodes and
            # also the green nodes
            if rowExists and colexists:

                # both row and col exits we only need to set the cursor
                
                self.cursor[0] = row
                self.cursor[1] = col
                self.cursor[2] = finalCurrentNode

            #if the row exist and column does not
            elif rowExists and not colexists:
                if rowRequried.data==None:   #this means the pink node list is None
                    pinkNodehead=None
                    pinkNodeTail = None
                    for j in range(col+1):
                        tempPinkNode = Node(" ")
                        if pinkNodehead==None:
                            pinkNodehead=tempPinkNode
                            pinkNodeTail=tempPinkNode
                        else:
                            tempPinkNode.prev=pinkNodeTail
                            pinkNodeTail.next=tempPinkNode
                            pinkNodeTail=tempPinkNode
                    pinkNodehead.prev=rowRequried
                    rowRequried.data = pinkNodehead
                    self.cursor=[row,col,pinkNodeTail,rowRequried]
                else:   #some data exists in the linked list
                    currentLength = 0
                    temp = rowRequried.data
                    while temp:
                        currentLength+=1
                        if temp.next==None:
                            pinkTail=temp

                        temp=temp.next

                    colLengthRequired = col-currentLength
                    
                    pinkNodehead=None
                    pinkNodeTail=None
                    for k in range(colLengthRequired+1):
                        tempPinkNode = Node(" ")
                        if pinkNodehead==None:
                            pinkNodehead=tempPinkNode
                            pinkNodeTail=tempPinkNode
                        else:
                            tempPinkNode.prev=pinkNodeTail
                            pinkNodeTail.next=tempPinkNode
                            pinkNodeTail=tempPinkNode
                    pinkNodehead.prev = pinkTail
                    pinkTail.next = pinkNodehead

                    self.cursor=[row,col,pinkNodeTail,rowRequried]

            # elif not rowExists and not colexists:
            elif not rowExists:
                currentRowsLength = 0
                temp = self.doc
                while temp!=None:
                    currentRowsLength+=1
                    temp=temp.next
                
                rowLengthRequired = row-currentRowsLength
                greenNodeHead = None
                greenNodeTail = None
                for i in range(rowLengthRequired+1):
                    tempGreenNode=Node(None)
                    if greenNodeHead==None:
                        greenNodeHead=tempGreenNode
                        greenNodeTail=tempGreenNode
                    else:
                        tempGreenNode.prev = greenNodeTail
                        greenNodeTail.next = tempGreenNode
                        greenNodeTail= tempGreenNode
                greenNodeHead.prev = self.tail
                self.tail.next = greenNodeHead
                self.tail = greenNodeTail
                pinkNodehead=None
                pinkNodeTail=None
                for i in range(col+1):
                    tempPinkNode=Node(" ")
                    if pinkNodehead==None:
                        pinkNodehead=tempPinkNode
                        pinkNodeTail=tempPinkNode
                    else:
                        tempPinkNode.prev = pinkNodeTail
                        pinkNodeTail.next = tempPinkNode
                        pinkNodeTail = tempPinkNode
                pinkNodehead.prev = self.tail
                self.tail.data = pinkNodehead
                self.cursor=[row,col,pinkNodeTail,self.tail]
        
#======================

#======================
    def forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''

        if self.cursor[0]<0 or self.cursor[1]<0:
            print("INVALID ARGUMENTS.")
            return
        
        currentNode=self.cursor[2]
        if currentNode.next!=None:
            self.cursor[1] = self.cursor[1]+1
            self.cursor[2] = currentNode.next
        else:
            if self.cursor[3].next:
                self.cursor[0] = self.cursor[0]+1
                self.cursor[1] = 0
                self.cursor[2] = self.cursor[3].next.data
                self.cursor[3] = self.cursor[3].next 
            else:
                print("NO NEXT LINE")
                return





        
        
#======================

#======================
    def back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''

        if self.cursor[0]<0 or self.cursor[1]<0:
            print("INVALID ARGUMENTS.")
            return
        
        currentNode=self.cursor[2]
        if currentNode.prev!=None:
            if currentNode.prev.data != currentNode:
                self.cursor[1] = self.cursor[1]-1
                self.cursor[2] = currentNode.prev
            else: # current node is the first pink node
                if currentNode.prev.prev !=None:
                    prevGreenNode = currentNode.prev.prev
                    if prevGreenNode.data==None:
                        print("PREVIOUS LINE IS EMPTY!")
                        return
                    temp = prevGreenNode.data
                    c=0
                    while temp.next!=None:
                        c+=1
                        temp= temp.next
                    newCursorPinkNode= temp
                    self.cursor[0]=self.cursor[0]-1
                    self.cursor[1] = c
                    self.cursor[2]= newCursorPinkNode
                    self.cursor[3] = prevGreenNode
                else:
                    print("YOU HAVE REACHED THE START OF THE DOCUMENT.")
                    return
    
#======================

#======================
    def home(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        if self.cursor[0]<0 or self.cursor[1]<0:
            print("INVALID ARGUMENTS.")
            return 
        self.cursor[0] = self.cursor[0]
        self.cursor[1] = 0
        temp = self.cursor[2]
        while temp.prev.data!=temp:
            temp=temp.prev
        newCurrentPinkNode = temp
        self.cursor[2]=newCurrentPinkNode

        
#======================

#======================
    def end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        if self.cursor[0]<0 or self.cursor[1]<0:
            print("INVALID ARGUMENTS.")
            return 
        
        currentPinkNode=self.cursor[2]
        c=self.cursor[1]
        temp = currentPinkNode
        while temp.next != None:
            c+=1
            temp = temp.next
        currentPinkNode=temp
        self.cursor[1] = c
        self.cursor[2] = currentPinkNode


        
#======================

#======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''
        # creating a linked list with the given string
        listOfChar = list(string)
        pinkNodeHead = None
        pinkNodeTail = None
        
        for i in listOfChar:
            tempPinkNode = Node(i)
            if pinkNodeHead==None:
                pinkNodeHead=tempPinkNode
                pinkNodeTail = tempPinkNode
            else:
                tempPinkNode.prev = pinkNodeTail
                pinkNodeTail.next = tempPinkNode
                pinkNodeTail = tempPinkNode
        if self.cursor[0]<0 or self.cursor[1]<0:
            # doc is empty
            self.doc= Node(None)
            pinkNodeHead.prev = self.doc
            self.doc.data = pinkNodeHead
            self.cursor=[0,0,pinkNodeHead,self.doc]
            self.tail=self.doc
        else:
            # doc is not empty it has some nodes in it
            # checking if we are inserting in between nodes or at the end of the pink list
            currentPinkNode=self.cursor[2]
            if currentPinkNode.next!=None:
                pinkNodeTail= currentPinkNode.next
                currentPinkNode.next.prev = pinkNodeTail
                pinkNodeHead.prev= currentPinkNode
                currentPinkNode.next = pinkNodeHead
                

            else:
                pinkNodeHead.prev= currentPinkNode
                currentPinkNode.next = pinkNodeHead
            self.cursor[1]=self.cursor[1]+len(listOfChar)
            self.cursor[2] = pinkNodeTail
                

            





#======================

#======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''

        if self.cursor[0]<0 or self.cursor[1]<0:
            print("INVALID ARGUMENTS.")
            return 
        
        if self.cursor[2]!=self.cursor[2].prev.data:
            tempRow= self.cursor[3]
            tempdata = tempRow.data
            numC=0
            while tempdata!=None:
                numC+=1
                tempdata=tempdata.next
            c=self.cursor[1]
            
            firstNode=self.cursor[2].prev
            temp=self.cursor[2]
            if numC<=c+num:
                rollBack=True
            else:
                rollBack=False
            while num!=0 and temp.next!=None:
                temp=temp.next
                num-=1
            
            if rollBack:
                self.cursor[2]=firstNode
                firstNode.next = None
            else:            
                temp.prev = firstNode
                firstNode.next = temp
                self.cursor[2]=temp
        else:
            pass

            


        
        
#======================

#======================
    def countCharacters(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            total number of characters in the document, basically
               the total number of pink nodes in the document.
        '''
        
        temp = self.doc
        characters = 0
        while temp!=None:
            temp2 = temp.data
            while temp2!=None:
                characters+=1
                temp2=temp2.next
            temp= temp.next
        return characters
#======================

#======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer number of non-empty lines in the document
        '''
        
        temp=self.doc
        lines = 0
        while temp!=None:
            if temp.data!=None:
                lines+=1
            temp=temp.next
        return lines
#======================


#======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''
        
        temp = self.doc
        while temp!=None:
            temp2 = temp.data
            char=""
            while temp2!=None:
                if temp2==self.cursor[2]:
                    char= char+"|"
                char= char + temp2.data
                temp2=temp2.next
            
            print(char)
            temp=temp.next
#======================

            
#======================
#======================
#    BONUS
#======================
    def undo(self):
        '''
        Undos the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        temp = self.doc
        with open(fileName, "w") as f:
            while temp!=None:
                temp2=temp.data
                temp3=""
                while temp2!=None:
                    temp3+=temp2.data
                    temp2=temp2.next
                temp3+="\n"
                f.write(temp3)
                temp=temp.next

#----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        if not exists(fileName):
            print("FILE DOES NOT EXISTS")
            return
        
        with open(fileName, "r") as f:
            
            data = f.read()
            data = data.split("\n")

        for i in data:
            greenNodeHead = None
            greenNodeTail = None
            for i in data:
                tempGreenNode=Node(None)
                if greenNodeHead==None:
                    greenNodeHead=tempGreenNode
                    greenNodeTail=tempGreenNode
                    # pink node creation
                    pinkNodeHead = None
                    pinkNodeTail =None
                    if i:
                        for j in i:
                            tempPinkNode=Node(j)
                            if pinkNodeHead==None:
                                pinkNodeHead=tempPinkNode
                                pinkNodeTail=tempPinkNode
                            else:
                                tempPinkNode.prev = pinkNodeTail
                                pinkNodeTail.next = tempPinkNode
                                pinkNodeTail=tempPinkNode
                        pinkNodeHead.prev = greenNodeHead
                        greenNodeHead.data = pinkNodeHead
                    
                else:
                    tempGreenNode.prev = greenNodeTail
                    greenNodeTail.next = tempGreenNode
                    greenNodeTail = tempGreenNode
                    #pink node creation
                    
                    pinkNodeHead = None
                    pinkNodeTail =None
                    if i:
                        for j in i:
                            tempPinkNode=Node(j)
                            if pinkNodeHead==None:
                                pinkNodeHead=tempPinkNode
                                pinkNodeTail=tempPinkNode
                            else:
                                tempPinkNode.prev = pinkNodeTail
                                pinkNodeTail.next = tempPinkNode
                                pinkNodeTail=tempPinkNode
                        pinkNodeHead.prev = greenNodeTail
                        greenNodeTail.data = pinkNodeHead
        self.doc =greenNodeHead
#----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.
 
        Parameters:
            substring to look for
        
        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''
        
        raise NotImplementedError
            
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    editor = TextEditor()
    print("Welcome to DS Text Editor\nEnter commands at the prompt")

    q=False
    while not q:
        statement = input()
        li=statement.split()
        if li[0]=="goto":
            editor.goto(int(li[1]),int(li[2]))
        elif li[0]=="forward":
            editor.forward()
        elif li[0]=="back":
            editor.back()
        elif li[0]=="home":
            editor.home()
        elif li[0]=="end":
            editor.end
        elif li[0]=="insert":
            str0 = ""
            for i in li[1:]:
                str0+=i
            editor.insert(str0)
        elif li[0]=="delete":
            editor.delete(int(li[1]))
        elif li[0]=="countCharacters":
            print(editor.countCharacters())
        elif li[0]=="countLines":
            print(editor.countLines())
        elif li[0]=="printDoc":
            editor.printDoc()
        elif li[0]=="quit":
            print("THANKS FOR USING MY PROGRAM.")
            q=True
        elif li[0]=="save":
            editor.save(li[1])
        elif li[0]=="load":
            editor.load(li[1])
        elif li[0]=="find":
            print("UNIMPLEMENTED")
        else:
            print("WRONG COMMAND.")


    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
   
if __name__ == '__main__':
    main()
    
#======================


