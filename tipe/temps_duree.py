def temps_duree(tab_notes):
   t2,n2 = tab_notes[1]
   ecart = t2
   l=[]
   long_l=0
   for temps,note in tab_notes:
      if long_l == 0 or N_prec != note:
         l.append((ecart,note))
         long_l += 1
      else:
         dt,N = l[long_l - 1]
         l[long_l - 1] = (dt + ecart,N)
      N_prec = note
   return l
