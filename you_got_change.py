def give_change(amount): 
   dollar = amount
   bill_dict = [(100, '$100 bill'), (50, '$50 bill'), (20, '$20 bill'), (10, '$10 bill'), (5, '$5 bill'), (1, '$1 bill'),] 
   dollars = []
   while dollar > 0:
        for face, money in bill_dict:
            while dollar >= face:
                dollars.append(money)
                dollar -= face
   results_lst = [0,0,0,0,0,0]
   results_lst[5] = len([x for x in dollars if x == '$100 bill'])
   results_lst[4] = len([x for x in dollars if x == '$50 bill'])
   results_lst[3] = len([x for x in dollars if x == '$20 bill'])
   results_lst[2] = len([x for x in dollars if x == '$10 bill'])
   results_lst[1] = len([x for x in dollars if x == '$5 bill'])
   results_lst[0] = len([x for x in dollars if x == '$1 bill'])
   return tuple(results_lst)


print(give_change(365)) # (0,1,1,0,1,3)
print(give_change(217)) # (2,1,1,0,0,2)