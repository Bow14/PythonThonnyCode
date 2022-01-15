email = 'thegmailinquestion.@uvu.edu'
atposition = email.find('@')
dotposition = email.find('.', atposition)
if atposition >=0 and dotposition >=0:
    print('valid')
else:
    print('Invalid')