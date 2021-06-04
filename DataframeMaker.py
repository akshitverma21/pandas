import pandas as pd
from datetime import datetime
def inputTaker():
    goods = input("Enter essential goods name ,"
                  "goods=vegetables or fruits")
    choiceExcel=input("Do you want dataframe in excel ? "
                      "Press y")
    if choiceExcel=='y'or choiceExcel=='Y':
        return excel_out(dataframeMaker(goods))
    else:
        return dataframeMaker(goods)


def dataframeMaker(goods):
    dict1 = {}
    numpgoods = int(input("Enter num of particular goods"))
    pgoodlist = []
    for n in range(numpgoods):
        pgood = input("enter particular good's name "
                      "pgood=tomato , reddish ,cabbage etc")
        pgoodlist.append(pgood)
    dict1.update({goods: pgoodlist})

    ratelist = []
    for n in range(numpgoods):
        prate = input(f"enter {pgoodlist[n]} rate")
        ratelist.append(prate)
    dict1.update({"rate": ratelist})
    print(dict1)

    return pd.DataFrame(dict1)

def excel_out(mydf):
# we have to use wruter just becouse the rate is coming as text in excel ,
# options=options={'strings_to_numbers': True}) makes string numbers to int
    writer = pd.ExcelWriter(f"{datetime.now().strftime('%H%M%S')}mydf.xlsx",
                            engine='xlsxwriter',
                            options={'strings_to_numbers': True})

    mydf.to_excel(writer,index=False,float_format="%.2f")
    writer.close()  # when using pd.ExcelWriter it has to be closed or opened in context manager

if __name__ == '__main__':

    mydf = inputTaker()
