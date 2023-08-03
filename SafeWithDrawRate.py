import math

inf  = 10**9
def timeToZero( wr, ri, pr ):
       p = 100
       y = 0
       wr = wr
       ri = (1 + ri/100.0)
       pr = (1 + pr/100.0)
       #pdb.set_trace()
       pfr = [] # pf return  post withdrawal each year
       p  = p -wr
       while( p > 0 ):
          p1 = p*pr
          p2 = p1 - wr
          pfr.append( p2*1.0/p )
          if ( len(pfr) > 1 ):
              # check if slope is negative
              if ( pfr[-1] > pfr[-2] ) :
                 return inf
          p = p2
          wr = wr*ri
          y = y+1
       return y

def timeToZeroFormula ( wr, ri , pr ) :
    # ri -> rate of increase of withdrawals annualy
    # pr -> constant portfolio returns
    # wr -> wr % per year starting from year i1
     ri = ri * 1.0/100
     pr = pr * 1.0/100
     wr = wr * 1.0/100
     if (pr-ri)>= wr:
         return  inf 
     return int ( math.log( 1 - ((pr-ri)/wr))/math.log((1+ri)/(1+pr)) )


def Swr(  pr, ri   ) :
    # calulcate the SWR given pr, ri
    # pr -> constant portfolio returns
    # ri -> rate of increase of withdrawals annualy
    wrMin = 0
    wrMax = 100
    c = 0
    while ( 1 ) :
       c = c+1
       tmin = timeToZero( wrMin, ri, pr )
       tmax =  timeToZero( wrMax , ri, pr )
       wrMid = (wrMax+ wrMin)/2.0
       tmid  = timeToZero( wrMid , ri, pr )
       import pdb
       #pdb.set_trace()
       #print( locals() )
       if (tmin == inf and  tmax < inf ):
           if tmid == inf:
              wrMin  =  wrMid
           else:
              wrMax = wrMid

       if ( (wrMax-wrMin) <= 0.02  or c>50):
            #print( " {}  {}".format( wrMin,wrMax) )
            #pdb.set_trace()
            return (wrMax)


#for pr in np.arange(8,12,0.1):
    #print ( " pr {} , TimeToZero = {} years ".format( pr , timeToZero( wr,ri,pr) ))
#print ( timeToZero( 2.22,5,7) )
#print ( Swr( 11, 8 ) )
print(  "Swr for (8% pf , 6% wr increase a year ) = {} % of intial  PF ".format( Swr ( 8,6) ) )
print ( "PF growing at 6%, with withdrwals growing at 7%/yr and initial widhdrawal rate at 3% of PF lasts for {} years ".format( timeToZero( 3 ,7, 6 ) ) )
print( "PF growing at 7%,  with withdrawals growing at 8%/yr and initial withdrwal rate at 4% of PF lasts for {} years ".format( timeToZeroFormula( 4 ,8, 7 ) ) ) 

