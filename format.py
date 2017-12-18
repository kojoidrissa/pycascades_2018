#!python

#Makes Headers and Footers Bold
#I need to improve this code
def bold_headers_footers(target):
    '''
    OpenPyXL Workbook --> OpenPyXL Workbook

    Takes in an OpenPyXL Workbook object, identifies the Header & footer rows, sets their
    cell styles to bold
    '''

    worksheets = target.get_sheet_names()
    for sheet in worksheets:
        for row in target.get_sheet_by_name(sheet).rows:
            #ri = target.get_sheet_by_name(sheet).rows.index(row)
            if row[0].value == 'Company': #Header test 
                for cell in row:
                    cell.style.font.bold = True
                    elif type(row[0].value) == unicode and type(row[5].value) != unicode: #Footer test
                    #this code depends on the cell types BEFORE the worksheet is written/saved
                    #as such, it needs to run BEFORE the save. I'll need to get a better handle on
                    #the various datatypes; I also need to rexamine my method here. There should be
                    #a less fragile way to do this Footer test
                for cell in row[5:]:
                    cell.style.font.bold = True
    return target

##Checking the bolding BEFORE writing the file
def what_is_bold(target):
    '''
    OpenPyXL Workbook --> Printed output

    Takes in an OpenPyXL Workbook object, identifies the cells that are bold
    prints identifying information about those cells  
    '''
    worksheets = target.get_sheet_names()
    for sheet in worksheets:
        for row in target.get_sheet_by_name(sheet).rows:
            ri = target.get_sheet_by_name(sheet).rows.index(row)
            for cell in row:
                ci = row.index(cell)
                if cell.style.font.bold:
                    print "Sheet", sheet, "Row", ri, "Cell", ci, ", also known as Cell", cell.address, "is", cell.value, "and it's BOLD."

# #Finding Hours
# for sheet in worksheets[:-1]:
#   for cell in sheet[0]:
#       if cell.value == "DOE":
#           di = sheet[0].index(cell)
#       elif cell.value == "Project":
#           pi = sheet[0].index(cell)
#       elif cell.value == "Tot. Hours":
#           ti = sheet[0].index(cell)
#   for row in target.get_sheet_by_name(sheet).rows:
#       if row[5].value + row[6].value == row[7].value:
#           print "Match!", row[5].value,"+",row[6].value, "=",row[7].value,"."
#           # for cell in row:
#           #   cell.style.font.bold = True
#    #              elif type(row[0].value) == unicode and type(row[5].value) != unicode:
#        #    for cell in row[5:]:
#        #        cell.style.font.bold = True


#Results BEFORE Workbooks has been saved
#Row 1 is a header; Row 2 is content; Row 3 is a footer; Row 4 is a Spacer Row
#Note changes in Rows 3 & 4
'''
for row in target.get_sheet_by_name('Quality').rows[0:4]:
    for cell in row:
        print cell.address, type(cell.value)
        
A1 <type 'unicode'>
B1 <type 'unicode'>
C1 <type 'unicode'>
D1 <type 'unicode'>
E1 <type 'unicode'>
F1 <type 'unicode'>
G1 <type 'unicode'>
H1 <type 'unicode'>
I1 <type 'unicode'>
J1 <type 'unicode'>
A2 <type 'int'>
B2 <type 'int'>
C2 <type 'int'>
D2 <type 'unicode'>
E2 <type 'unicode'>
F2 <type 'int'>
G2 <type 'int'>
H2 <type 'int'>
I2 <type 'float'>
J2 <type 'float'>
A3 <type 'unicode'>
B3 <type 'unicode'>
C3 <type 'unicode'>
D3 <type 'unicode'>
E3 <type 'unicode'>
F3 <type 'int'>
G3 <type 'int'>
H3 <type 'float'>
I3 <type 'float'>
J3 <type 'float'>
A4 <type 'unicode'>
B4 <type 'unicode'>
C4 <type 'unicode'>
D4 <type 'unicode'>
E4 <type 'unicode'>
F4 <type 'unicode'>
G4 <type 'unicode'>
H4 <type 'unicode'>
I4 <type 'unicode'>
J4 <type 'unicode'>
'''

#Results AFTER Workbook has been saved
#Row 1 is a header; Row 2 is content; Row 3 is a footer; Row 4 is a Spacer Row
#Note changes in Rows 3 & 4
'''
for row in target.get_sheet_by_name('Quality').rows[0:4]:
    for cell in row:
        print cell.address, type(cell.value)
        
A1 <type 'unicode'>
B1 <type 'unicode'>
C1 <type 'unicode'>
D1 <type 'unicode'>
E1 <type 'unicode'>
F1 <type 'unicode'>
G1 <type 'unicode'>
H1 <type 'unicode'>
I1 <type 'unicode'>
J1 <type 'unicode'>
A2 <type 'int'>
B2 <type 'int'>
C2 <type 'int'>
D2 <type 'unicode'>
E2 <type 'unicode'>
F2 <type 'int'>
G2 <type 'int'>
H2 <type 'int'>
I2 <type 'float'>
J2 <type 'float'>
A3 <type 'NoneType'>
B3 <type 'NoneType'>
C3 <type 'NoneType'>
D3 <type 'NoneType'>
E3 <type 'NoneType'>
F3 <type 'int'>
G3 <type 'int'>
H3 <type 'float'>
I3 <type 'float'>
J3 <type 'float'>
A4 <type 'NoneType'>
B4 <type 'NoneType'>
C4 <type 'NoneType'>
D4 <type 'NoneType'>
E4 <type 'NoneType'>
F4 <type 'NoneType'>
G4 <type 'NoneType'>
H4 <type 'NoneType'>
I4 <type 'NoneType'>
J4 <type 'NoneType'>
'''

##So, a lot of the 'unicode' types that are used for blanks BEFORE the save, turn into 'NoneType' afterwards.
##The NoneType later makes sense, as that's what I used in the buffers.