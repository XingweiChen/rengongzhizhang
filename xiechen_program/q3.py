pstr = ["high cost performance","Great place","Have a good time","quite special","good place","easy of access","Very worth a visit", "tickets are cheap", "convenient traffic", "overall feels good", "worth to see", "very convenient traffic", "very fun", "a good place", "The ticket is cost-effective", "the overall feeling is good", "the place worth going", "the view is good", "the overall is not bad", "feel good", "the scenery is very good", "the scenery is not bad", "I like it very much", "Really good", "It's worth seeing", "The ticket is not expensive", "The ticket is very cheap", "The scenery is not bad", "The price is very good", "It's still very good", "The scenery is very good", "The environment is great", "The scenery is OK", "The air is very fresh", "Very worth seeing", "Very worth going", "Good view", "Good traffic"," Value this price", "good value for money"]

nstr = ["low cost performance", "I don't prefer it", "Nothing fun", "Nothing special", "Nothing good-looking", "Traffic is not very convenient", "Nothing special", "Tickets are too expensive", "Traffic inconvenient", "The overall feeling is bad", "Nothing to play", "Never come again", "Nothing to see", "Feeling bad", "Tickets are a bit expensive", "very bad", "The scenery is bad", "There is nothing to watch", "I don't like it", "The price is a bit expensive", "cost performance is too low", "I feel not good", "not high cost performance", "Not very fun", "Tickets are not cheap ", "traffic is not convenient", "the scenery is not good", "nothing to play", "too commercial", "tickets are expensive", "fare is a bit expensive", "nothing to see", "price not cheap", "price is very high", "ticket too expensive", "The traffic is not good", "The ticket is too expensive", "The scenery is very poor", "Not worth the price", "The traffic is bad"]

pdct = {}
ndct = {}
pndct = {}

for strs in pstr:
    strs = strs.lower()
    for s in strs.split():
        if s in pdct:
            pdct[s] += 1
        else:
            pdct[s] = 1
        if s in pndct:
            pndct[s] += 1
        else:
            pndct[s] = 1

for strs in nstr:
    strs = strs.lower()
    for s in strs.split():
        if s in ndct:
            ndct[s] += 1
        else:
            ndct[s] = 1
        if s in pndct:
            pndct[s] += 1
        else:
            pndct[s] = 1

for k in pndct:
    if k in pdct:
        pdct[k] /= pndct[k]
    if k in ndct:
        ndct[k] /= pndct[k]

in_str = input().split()
ptot, ntot = 1, 1
for s in in_str:
    ptot *= pdct[s] if s in pdct else 0.5
    ntot *= ndct[s] if s in ndct else 0.5

if ptot > ntot:
    print(1)
else:
    print(0)
