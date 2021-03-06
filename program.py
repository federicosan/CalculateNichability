
import csv
import math
import sys

def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

def SetPath():
    downloadsPath = '/Users/adam/Downloads/Search Term of '
    argString = ""
    print(sys.argv[1-3])
    file = " ".join(sys.argv).replace('program.py ', '')
    # for arg in sys.argv:
    #
    #     if arg != "program.py":
    #         arg + " "

    ans = downloadsPath + file + ".csv"
    return ans



def Main():
    print(sys.argv[1:])
    totalReviews = 0
    totalRevenue = 0
    count = 0

    # path = SetPath()
    path = '/Users/adam/Downloads/Search Term of rain stick.csv'

    print("searching for file at: " + path)

    with open(path) as csvfile:
        if (type(csvfile == 'io.TextIOWrapper')):
            for i in range(7):
                csvfile.__next__()
        else:
            for i in range(7):
                csvfile.next()

        reader = csv.DictReader(csvfile)
        for row in reader:
            formattedRevenue = str(row['Est. Revenue']).replace(',', '').replace('$', '').replace('<', '')
            formattedReview = str(row['# of Reviews']).replace(',', '')
            if(formattedReview == "N.A."  or formattedRevenue == "N.A."):
                continue
            elif(int(formattedReview) <= 50):
                revenue = int(formattedRevenue)
                review = int(formattedReview)
                totalRevenue += revenue
                totalReviews += review
                count += 1

    AvgRevenue = totalRevenue / count
    AvgReview = totalReviews / count
    fullnessPercentage = (AvgReview / AvgRevenue) * 100
    score = str((500 - round(fullnessPercentage * 100)) * .2)
    print("Niche Score: " + score)
    input("press any key to continue...")

if __name__ == "__main__":
    Main()




