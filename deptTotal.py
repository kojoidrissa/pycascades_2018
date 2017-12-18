def deptTotal(footer, tabname):
    '''
    dict, string --> dict

    Takes in a dictionary (footer) in the following form: 
        footer = {'cc1': [None * 6, DOETotal, ProjTotal, TotHours, DOEUtil, ProjUtil],...'ccN':[None * 6, DOETotal, ProjTotal, TotHours, DOEUtil, ProjUtil]}
    which is the footer for a Functional Area and a string (tabname);

    returns a dict of the same format, with the totals being for the entire Functional Area:
        deptTotal = {'tabname': [None * 6, DOETotal, ProjTotal, TotHours, DOEUtil, ProjUtil]}

    '''
    deptBuffr = len(footer.values()[0]) - 5
    deptotal = {tabname: [None for i in range(deptBuffr)]} #creates the empty spaces in the dictionary

    dt_doe = 0
    dt_prj = 0

    for v in footer.itervalues():
        dt_doe = dt_doe + v[-5] #as currently configured, DOETotal is the -5th element in the footer
        dt_prj = dt_prj + v[-4] #as currently configured, ProjTotal is the -4th element in the footer

    deptotal[tabname].extend([dt_doe, dt_prj]) #adds the departmental DOE & Proj totals to the dictionary
    totHours = float(dt_doe + dt_prj)
    deptotal[tabname].extend([totHours, dt_doe/totHours, dt_prj/totHours]) #adds departmental Total hours & Util. % to dictionary

    return deptotal