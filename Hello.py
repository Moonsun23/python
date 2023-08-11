import datetime

print('💜🤍🤍🤍💜           💜💜            💜💜💜💜         💜💜💜💜             💜🤍🤍🤍💜          /////')
print('💜🤍🤍🤍💜     💜🤍🤍🤍💜      💜🤍🤍🤍💜    💜🤍🤍🤍💜          💜🤍🤍🤍💜          | o  o |')
print('💜💜💜💜💜   💜🤍🤍🤍🤍💜    💜💜💜💜        💜💜💜💜                  💜🤍💜            (|  ^  |)')
print('💜🤍🤍🤍💜   💜💜💜💜💜💜    💜🤍🤍🤍💜    💜🤍🤍🤍💜                  💜                 | [_] |  ')
print('💜🤍🤍🤍💜   💜🤍🤍🤍🤍💜    💜🤍🤍🤍💜    💜🤍🤍🤍🤍💜              💜                  -----')

print('                  +---+')
print('                  |     |')
print('            +---+---+')
print('            |     |     | ')
print('       +---+---+---+                 /\_/\           -----')
print('      |     |     |     |              (  `  `   )       / Hello \ ')
print('+---+---+---+---+                (   -    )     <  Junior  | ')
print('|     |     |     |     |                |   |   |       \ Coder!/ ')
print('+---+---+---+---+                (__|__)          -----   ')


current_datetime = datetime.datetime.now()

soju_p= 3000
soju_q=2

chicken_p=12000
chicken_q=1


total = (soju_p * soju_q) + (chicken_p * chicken_q)
tax = (int)(total * 0.10)
gwase= total - tax

pay = (int)(gwase + tax)
tmt = 50000
change = tmt - pay

print(f'''
[음식나라]
--------------------------
소주          {soju_q}          {soju_p * soju_q}
너나치킨    {chicken_q}     {chicken_p * chicken_q}
--------------------------
과세합계                            {gwase}
부가세                                {tax}
--------------------------
총합계                                {pay}
받은금액                             {tmt}
잔돈                                    {change} 
--------------------------
{current_datetime.strftime('%Y-%m-%d %H:%M:%S')}


''')


