def MaximumDiscount(N, price):
    maxDiscount = 0

    price.sort(reverse = True)
    for i in range(N):
        if (i+1) % 3 == 0:
            maxDiscount += price[i]

    return(maxDiscount)
