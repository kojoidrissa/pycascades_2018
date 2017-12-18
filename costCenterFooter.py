def costCenterFooter(functable):
    '''
    list of lists --> dict

    Takes in a functional area table (functable), finds it's unique set of Cost Centers,
    then uses that list to create a series of key:value pairs in the format
        {'cc1': [sumDOE, sumProj, totHours, DOEUtil, ProjUtil]...'ccN': [sumDOE, sumProj, totHours, DOEUtil, ProjUtil]}
    Here in the 'footer' branch, I'm trying to JUST return  the footer dictionary, not append it to the table
    the 'create_tabs' function will handle that, using the key of each pair to append the appropriate value list
    '''

    #Creating list of unique cost Centers
    ccList = []
    for i in functable:
        ccList.append(i[1])
    ccUnique = set(ccList)
    
    ##Here in the 'footer' branch, I'm trying to return JUST the footer dictionary, not appending it to the table
    ##The goal is to end up with {'cc1':[doeTotal, projTotal}, 'cc2:'[doeTotal, projTotal]...} and return it
    ##to a new "functFooter" variable, which would be called into the 'create_tabs' function and used to 
    ##calculate the footer row for each cost center
    footer = {}

    #I'm semi-automating the size of the footer, based on needing it to:
    #be the same length as the rows in the input functable;
    #needing it to be blank, but have room to add 5 elements to the end of it
    #   sumDoe, sumProj, totHours, (sumDoe/totHours), & (sumProj/totHours)
    ftrBuffr = len(functable[0]) - 5
    for cc in ccUnique:
        ccDict = {str(cc): [None for i in range(ftrBuffr)]} #list comprehension here
        sumDoe = 0
        sumProj = 0
        for row in functable:
            if row[1] == cc:
                sumDoe = sumDoe + row[-5]
                sumProj = sumProj + row[-4]
        #StackOverflow helped with code below: http://stackoverflow.com/a/3419217;
        #In a later refactor, I should see if the .update method would work here too
        ccDict[str(cc)].extend([sumDoe, sumProj])
        totHours = float(sumDoe + sumProj)
        ccDict[str(cc)].extend([totHours, (sumDoe/totHours), (sumProj/totHours)])    
        footer.update(ccDict) #using the .update method as per http://stackoverflow.com/a/1165836
    return footer