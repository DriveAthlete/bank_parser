import psycopg2


def update(inf):
    con = psycopg2.connect(
        database='bank_final',
        user='bank',
        password='12345',
        host='localhost',
        port='5432'
    )
    cur = con.cursor()
    string = "UPDATE currency_currency SET value = '{name}'  WHERE id = '1'".format(name=inf['USDEUR'])
    cur.execute(string)
    con.commit()
    string = "UPDATE currency_currency SET value = '{name}'  WHERE id = '3'".format(name=inf['USDGBP'])
    cur.execute(string)
    con.commit()
    string = "UPDATE currency_currency SET value = '{name}'  WHERE id = '4'".format(name=inf['USDRUB'])
    cur.execute(string)
    con.commit()
    string = "UPDATE currency_currency SET value = '{name}'  WHERE id = '5'".format(name=inf['USDBTC'])
    cur.execute(string)
    con.commit()
    con.close()
