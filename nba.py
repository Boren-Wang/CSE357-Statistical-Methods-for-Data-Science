N = 1000 # the number of times the experiment is repeated

N_A = 0 # the number of times there is a tie after 4 games (2-2)
N_BA = 0 # the number of times there was a tie after 4 games and TOR won 4-3

import numpy

phi_score = 0
tor_score = 0

homes = ['TOR', 'TOR', 'PHI', "PHI", 'TOR', 'PHI', 'TOR']

for i in range(N):
    phi_score = 0
    tor_score = 0
    round = 1
    while phi_score<4 and tor_score<4:
        home = homes[round-1]
        p = 0.75 if home == "TOR" else 0.25 # the prob that TOR will win the round
        # p = 0.5
        res = numpy.random.binomial(1, p)
        # print(res)
        if res==1:
            tor_score += 1
        else:
            phi_score += 1
        # print("("+str(phi_score)+", "+str(tor_score)+")")
        if round == 4:
            if tor_score==2 and phi_score==2:
                N_A += 1
            else:
                break
        round+=1
    if tor_score==4 and phi_score==3:
        N_BA += 1

prob_A = N_A / N
prob_B_given_A = N_BA / N_A
# print("P(A): "+str(prob_A))
# print("P(B|A): "+str(prob_B_given_A))
print("For N = "+str(N)+", the simulated value for part(e) is "+str(prob_B_given_A))




