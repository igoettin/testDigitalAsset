


def checkInput(input):
    if not isinstance(input,int) and not isinstance(input,float):
        return False
    else:
        return True

if __name__ == "__main__":
    print "Welcome, please type the values for each of the following variables: "
    print ""
    BTC = input("BTC:")
    Gold = input("Gold:")
    ThirtyYrRR = input("30-Year Risk Rate [Enter as a whole percentage (e.g. 5 for 5% not .05)]: ")
    CurrentEarnings = input("Current Earnings Growth in Equity Markets: [Enter as a whole percentage (e.g. 5 for 5% not .05)]: ")
    nYears = input("n. Years:")
    DigitalAssetPrice = input("Digital Asset Price: ")
    PercentDigitalAssetMrktShr = input("% of Digital Asset Market Share: [Enter as a whole percentage (e.g. 5 for 5% not .05)]: ")
    OneYrDigitalAssetGrowth = input("1 Year Digital Asset Growth:")
    OneYrBTCGrowth = input("1 Year BTC Growth:")

    print "\n\nTrace of the equation follows: "
    X = float(BTC)/float(Gold)
    print "(%f / %f) = %f" % (BTC,Gold,X)
    Y = X/100.0
    print "%f / 100 = %f" % (X,Y)
    ThirtyYrRR /= float(100)
    Z = Y/float(ThirtyYrRR) 
    print "%f / %f = %f" % (Y,ThirtyYrRR,Z)
    A = Z*float(100)
    print "%f * 100 = %f" % (Z,A)
    B = A/float(30)
    print "%f / 30 Years = %f" % (A,B)
    print "The multiple of digital asset growth vs real asset growth is %f" % (B)
    CurrentEarnings /= float(100)
    ADAGR = B * CurrentEarnings
    print "%f * %f = %f" % (B,CurrentEarnings,ADAGR)
    PercentDigitalAssetMrktShr /= float(100)
    ADAGR += 1
    G = (ADAGR * float(nYears)) * (float(DigitalAssetPrice)) * (float(PercentDigitalAssetMrktShr))
    print "(%f * %f) * (%f) * (%f)" % (ADAGR, nYears, DigitalAssetPrice, PercentDigitalAssetMrktShr)
    DigitalAssetPrinceNYears = G * (float(OneYrDigitalAssetGrowth)/float(OneYrBTCGrowth))
    print "%f * (%f / %f)" % (G,OneYrDigitalAssetGrowth,OneYrBTCGrowth)
    print "The Digital Asset Price in n. Years is %f" % (DigitalAssetPrinceNYears)





