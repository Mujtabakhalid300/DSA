#===================================
#===================================
# Name   : Mujtaba Khalid
# Roll no: 241547337
# Section: B
# Date   : 17-3-2023
#===================================
#===================================

class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selection = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        self.selectionTuple=()
        self.undoRedoStack = []
        self.undoRedoPointer = None
        
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''
        
        tempSheet = []
        for row in range(rows):
            tempRow = []
            for col in range(cols):
                tempRow.append(None)
            tempSheet.append(tempRow)
        self.sheet = tempSheet

#======================

#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        self.undoRedoStack.append(["cursor", self.cursor[0],self.cursor[1]])
        self.cursor = [row,col]

#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        self.undoRedoStack.append(["insert",self.cursor[0], self.cursor[1], self.sheet[self.cursor[0]][self.cursor[1]]])
        self.sheet[self.cursor[0]][self.cursor[1]] = val
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''
        self.undoRedoStack.append(["delete",self.cursor[0], self.cursor[1], self.sheet[self.cursor[0]][self.cursor[1]]])
        self.sheet[self.cursor[0]][self.cursor[1]] = None
        
#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        return self.sheet[self.cursor[0]][self.cursor[1]]        
#======================

#======================    
    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''
        self.undoRedoStack.append(["selection", self.selection])
        self.selection=[]
        startRow = self.cursor[0]
        startCol = self.cursor[1]
        endRow = row
        endCol = col
        self.selectionTuple = tuple(sorted([startRow,startCol,endRow,endCol]))
        if startRow==endRow and startCol==endCol:
            self.selection.append(self.sheet[startRow,startRow])
            return None
        else:
            for i in range(self.selectionTuple[0],self.selectionTuple[2]+1):
                for j in range(self.selectionTuple[1],self.selectionTuple[3]+1):
                    if self.sheet[i][j]:
                        self.selection.append(self.sheet[i][j])
        



#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        
        return self.selectionTuple
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''

        sum=0
        for i in self.selection:
            if i:
                sum+=i
        self.undoRedoStack.append(["sum",row, col, self.sheet[row][col]])
        self.sheet[row][col] = sum

#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''   
             
        prod=1
        for i in self.selection:
            if i:
                prod *= i
        self.undoRedoStack.append(["multiply",row, col, self.sheet[row][col]])
        self.sheet[row][col] = prod
#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
           
        sum=0

        for i in self.selection:
            if i:
                sum+=i
        avg = sum/(len(self.selection))
        self.undoRedoStack.append(["average",row, col, self.sheet[row][col]])
        self.sheet[row][col] = round(avg, 2)

#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''        
        
        self.undoRedoStack.append(["max",row, col, self.sheet[row][col]])
        self.sheet[row][col] = max(self.selection)
#======================

#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
    
        rowStr = "row/col"
        for i in range(len(self.selection)+1):
            rowStr+= f"      {i}"
        print(rowStr)
        for count,i in enumerate(self.sheet):
            tempStr = ""
            tempStr+= f"    {count}        "
            for j in i:
                if j:
                    spacer = 6-len(str(j))
                    space = " "
                    for i in range(spacer):
                        space = space + " "
                    tempStr+=f"{j}{space}"
                else:
                    tempStr+=f"       "

            print(tempStr)
 
        
        
#======================

            
#======================
#======================
#    BONUS
#======================
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        print(len(self.undoRedoStack))
        for i in self.undoRedoStack:
            print(i)
        if len(self.undoRedoStack
               )>0:
            if self.undoRedoPointer:
                self.undoRedoPointer = self.undoRedoPointer-1
                if 0<=abs(self.undoRedoPointer)<=len(self.undoRedoStack)-1:
                    item = self.undoRedoStack[self.undoRedoPointer]
                else:
                    return "YOU CAN NOT UNDO ANYMORE."
                if item[0]=="cursor":
                    self.cursor = [item[1],item[2]]
                elif item[0]=="insert":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "selection":
                    self.selection = item[1]
                elif item[0]== "sum":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "average":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "max":
                    self.sheet[item[1]][item[2]] =item[3]
            else:
                self.undoRedoPointer = -1
                item = self.undoRedoStack[self.undoRedoPointer]
                if item[0]=="cursor":
                    self.cursor = [item[1],item[2]]
                elif item[0]=="insert":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "selection":
                    self.selection = item[1]
                elif item[0]== "sum":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "average":
                    self.sheet[item[1]][item[2]] = item[3]
                elif item[0]== "max":
                    self.sheet[item[1]][item[2]] =item[3]
        else:
            print("KINDLY PERFORM SOME ACTIONS FIRST TO UNDO THEM.")
            

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

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
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    sheet.CreateSheet(10,10)
    sheet.Goto(0,0)
    sheet.Insert("a")
    sheet.Goto(0,1)
    sheet.Insert("b")
    sheet.Goto(1,0)
    sheet.Insert("c")
    sheet.Goto(1,1)
    sheet.Insert("d")
    sheet.Goto(2,0)
    sheet.Insert("e")
    sheet.Goto(2,1)
    sheet.Insert("f")
    sheet.Goto(0,2)
    sheet.Insert(1)
    sheet.Goto(0,3)
    sheet.Insert(2)
    sheet.Goto(0,4)
    sheet.Insert(3)
    sheet.Goto(1,2)
    sheet.Insert(4)
    sheet.Goto(1,3)
    sheet.Insert(5)
    sheet.Goto(1,4)
    sheet.Insert(6)
    sheet.Goto(2,2)
    sheet.Insert(7)
    sheet.Goto(2,3)
    sheet.Insert(784)
    sheet.Goto(2,4)
    sheet.Insert(9)
    sheet.Goto(7,7)
    sheet.Insert(78)
    sheet.Goto(0,2)
    sheet.Select(2,4)
    sheet.Goto(2,4)
    sheet.Select(0,2)
    sheet.Goto(2,2)
    sheet.Select(0,4)
    sheet.Goto(0,4)
    sheet.Select(2,2)
    print(sheet.GetSelection())
    sheet.Sum(2,6)
    sheet.Sum(2,7)
    sheet.Avg(2,8)
    sheet.Max(2,9)
    sheet.PrintSheet()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.Undo()
    sheet.PrintSheet()

    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # sheet.Undo()
    # print("\n\n\n-------------------------------------------")
    # for i in sheet.sheet:
    #     print(i)
    
    # sheet.CreateSheet(5,5)
    #
    # EXAMPLE LOOP:
    # ------------
    # while True:
    #     sheet.Goto(2,2)
    #     sheet.insert(4)
    #     sheet.Print()
    

if __name__ == '__main__':
    main()
    
    
#======================


