from tkinter import *

root = Tk()
# Window Label
root.title('CryptoCompare')
# Window Default Dimensions
root.geometry('{}x{}'.format(600, 375))

#************************************************************************************

import urllib.request
import json
import collections



# BASE CODE FOR GETTING COIN DATA FROM COINMARKETCAP
'''
cryptolist = ['bitcoin','bitcoin-cash','ethereum','litecoin','ripple','monero']
for cryptoitem in cryptolist:
    r = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+cryptoitem+'/')
    r_body = r.read()

# https://docs.python.org/3/library/json.html
    j = json.loads(r_body.decode("utf-8"))
    #newdict = r.json()
    #listtodict = newdict[0]

    #listofkeys = ['id','name','symbol','rank','price_usd','market_cap_usd','available_supply','total_supply','max_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated']
    #for item in listofkeys:
    #    print(item, '= ', listtodict[item])
    print('\n')
    iter=0
    for item in j:
        foo = list(item.keys())
        #bar = list(item.values())
        for itemkey in foo:
            print(itemkey + ':')
            print(list(item.values())[iter])
            print('\n')
            iter+=1
'''

'''
# USING REQUESTS MODULE - TEST CODE
import requests
cryptolist = ['bitcoin','bitcoin-cash','ethereum','litecoin','ripple','cardano','stellar','neo','monero']
for cryptoitem in cryptolist:
  r = requests.get(url='https://api.coinmarketcap.com/v1/ticker/'+cryptoitem+'/')

  newdict = r.json()
  listtodict = newdict[0]

  listofkeys = ['id','name','symbol','rank','price_usd','market_cap_usd','available_supply','total_supply','max_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated']
  for item in listofkeys:
    print(item, '= ', listtodict[item])
  print('\n')
'''
#***************************************************************************************
'''
# USING REQUESTS MODULE - TEST CODE
def updatestats():
    for cryptoitem in cryptolist:
        r = requests.get(url='https://api.coinmarketcap.com/v1/ticker/'+cryptoitem+'/')

        newdict = r.json()
        listtodict = newdict[0]
'''
#*****************************************************************************************

# Create Drop Down Menu
# OptionMenu(master, variable, *values)

# List of options for drop down menu. Add more by looking up url on coinmarketcap
# and adding to the 'COINS' list.
COINS = [
    "Bitcoin",
    "Bitcoin-Cash",
    "Ethereum",
    "LiteCoin",
    "Ripple",
    "Cardano",
    "Stellar",
    "Neo",
    "Monero"
]

variable = StringVar(root)
variable.set(COINS[0]) # default value
w = OptionMenu(root, variable, *COINS)
variable1 = StringVar(root)
variable1.set(COINS[1]) # default value
v = OptionMenu(root, variable1, *COINS)
variable2 = StringVar(root)
variable2.set(COINS[2]) # default value
x = OptionMenu(root, variable2, *COINS)
variable3 = StringVar(root)
variable3.set(COINS[3]) # default value
y = OptionMenu(root, variable3, *COINS)
variable4 = StringVar(root)
variable4.set(COINS[4]) # default value
z = OptionMenu(root, variable4, *COINS)



#*****************************************************************************************


# create all of the main containers
row1 = Frame(root, width=250, height=50, pady=3)
row2 = Frame(root, width=250, height=50, pady=3)
#row3 = Frame(root, width=250, height=50, pady=3)

# Create Main Containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

row1.grid(row=0, sticky="ew")
row2.grid(row=1, sticky="ew")
#row3.grid(row=2, sticky="ew")


# Widget Initiation - Top Frame
stat_label = Label(row1, text='Stat')
coin1_label = OptionMenu(row1, variable, *COINS)
coin2_label = OptionMenu(row1, variable1, *COINS)
coin3_label = OptionMenu(row1, variable2, *COINS)
coin4_label = OptionMenu(row1, variable3, *COINS)
coin5_label = OptionMenu(row1, variable4, *COINS)

# Widget Layout - Top Frame
stat_label.grid(row=0, column=0)
coin1_label.grid(row=0, column=1)
coin2_label.grid(row=0, column=2)
coin3_label.grid(row=0, column=3)
coin4_label.grid(row=0, column=4)
coin5_label.grid(row=0, column=5)


# Widget Initiation - Center Frame
coinid = Label(row1, text='Coin ID')
coinid1 = Label(row1, text='')
coinid2 = Label(row1, text='')
coinid3 = Label(row1, text='')
coinid4 = Label(row1, text='')
coinid5 = Label(row1, text='')

coinname = Label(row1, text='Coin Name')
coinname1 = Label(row1, text='')
coinname2 = Label(row1, text='')
coinname3 = Label(row1, text='')
coinname4 = Label(row1, text='')
coinname5 = Label(row1, text='')

coinsym = Label(row1, text='Coin Symbol')
coinsym1 = Label(row1, text='')
coinsym2 = Label(row1, text='')
coinsym3 = Label(row1, text='')
coinsym4 = Label(row1, text='')
coinsym5 = Label(row1, text='')

coinrank = Label(row1, text='Coin Rank')
coinrank1 = Label(row1, text='')
coinrank2 = Label(row1, text='')
coinrank3 = Label(row1, text='')
coinrank4 = Label(row1, text='')
coinrank5 = Label(row1, text='')

coinprice = Label(row1, text='Price')
coinprice1 = Label(row1, text='')
coinprice2 = Label(row1, text='')
coinprice3 = Label(row1, text='')
coinprice4 = Label(row1, text='')
coinprice5 = Label(row1, text='')

coinmktcap = Label(row1, text='Market Cap')
coinmktcap1 = Label(row1, text='')
coinmktcap2 = Label(row1, text='')
coinmktcap3 = Label(row1, text='')
coinmktcap4 = Label(row1, text='')
coinmktcap5 = Label(row1, text='')

coinavlsup = Label(row1, text='Avail. Supply')
coinavlsup1 = Label(row1, text='')
coinavlsup2 = Label(row1, text='')
coinavlsup3 = Label(row1, text='')
coinavlsup4 = Label(row1, text='')
coinavlsup5 = Label(row1, text='')

cointotsup = Label(row1, text='Total Supply')
cointotsup1 = Label(row1, text='')
cointotsup2 = Label(row1, text='')
cointotsup3 = Label(row1, text='')
cointotsup4 = Label(row1, text='')
cointotsup5 = Label(row1, text='')

coinmaxsup = Label(row1, text='Max. Supply')
coinmaxsup1 = Label(row1, text='')
coinmaxsup2 = Label(row1, text='')
coinmaxsup3 = Label(row1, text='')
coinmaxsup4 = Label(row1, text='')
coinmaxsup5 = Label(row1, text='')

coinpctchg1h = Label(row1, text='% Chg. 1hr.')
coinpctchg1h1 = Label(row1, text='')
coinpctchg1h2 = Label(row1, text='')
coinpctchg1h3 = Label(row1, text='')
coinpctchg1h4 = Label(row1, text='')
coinpctchg1h5 = Label(row1, text='')

coinpctchg24h = Label(row1, text='% Chg. 24hr.')
coinpctchg24h1 = Label(row1, text='')
coinpctchg24h2 = Label(row1, text='')
coinpctchg24h3 = Label(row1, text='')
coinpctchg24h4 = Label(row1, text='')
coinpctchg24h5 = Label(row1, text='')

coinpctchg7d = Label(row1, text='% Chg. 7d')
coinpctchg7d1 = Label(row1, text='')
coinpctchg7d2 = Label(row1, text='')
coinpctchg7d3 = Label(row1, text='')
coinpctchg7d4 = Label(row1, text='')
coinpctchg7d5 = Label(row1, text='')

coinlastupdate = Label(row1, text='Last Update')
coinlastupdate1 = Label(row1, text='')
coinlastupdate2 = Label(row1, text='')
coinlastupdate3 = Label(row1, text='')
coinlastupdate4 = Label(row1, text='')
coinlastupdate5 = Label(row1, text='')


# Widget Layout
coinid.grid(row=1, column=0)
coinid1.grid(row=1, column=1)
coinid2.grid(row=1, column=2)
coinid3.grid(row=1, column=3)
coinid4.grid(row=1, column=4)
coinid5.grid(row=1, column=5)

coinname.grid(row=2, column=0)
coinname1.grid(row=2, column=1)
coinname2.grid(row=2, column=2)
coinname3.grid(row=2, column=3)
coinname4.grid(row=2, column=4)
coinname5.grid(row=2, column=5)

coinsym.grid(row=3, column=0)
coinsym1.grid(row=3, column=1)
coinsym2.grid(row=3, column=2)
coinsym3.grid(row=3, column=3)
coinsym4.grid(row=3, column=4)
coinsym5.grid(row=3, column=5)

coinrank.grid(row=4, column=0)
coinrank1.grid(row=4, column=1)
coinrank2.grid(row=4, column=2)
coinrank3.grid(row=4, column=3)
coinrank4.grid(row=4, column=4)
coinrank5.grid(row=4, column=5)

coinprice.grid(row=5, column=0)
coinprice1.grid(row=5, column=1)
coinprice2.grid(row=5, column=2)
coinprice3.grid(row=5, column=3)
coinprice4.grid(row=5, column=4)
coinprice5.grid(row=5, column=5)

coinmktcap.grid(row=6, column=0)
coinmktcap1.grid(row=6, column=1)
coinmktcap2.grid(row=6, column=2)
coinmktcap3.grid(row=6, column=3)
coinmktcap4.grid(row=6, column=4)
coinmktcap5.grid(row=6, column=5)

coinavlsup.grid(row=7, column=0)
coinavlsup1.grid(row=7, column=1)
coinavlsup2.grid(row=7, column=2)
coinavlsup3.grid(row=7, column=3)
coinavlsup4.grid(row=7, column=4)
coinavlsup5.grid(row=7, column=5)

cointotsup.grid(row=8, column=0)
cointotsup1.grid(row=8, column=1)
cointotsup2.grid(row=8, column=2)
cointotsup3.grid(row=8, column=3)
cointotsup4.grid(row=8, column=4)
cointotsup5.grid(row=8, column=5)

coinmaxsup.grid(row=9, column=0)
coinmaxsup1.grid(row=9, column=1)
coinmaxsup2.grid(row=9, column=2)
coinmaxsup3.grid(row=9, column=3)
coinmaxsup4.grid(row=9, column=4)
coinmaxsup5.grid(row=9, column=5)

coinpctchg1h.grid(row=10, column=0)
coinpctchg1h1.grid(row=10, column=1)
coinpctchg1h2.grid(row=10, column=2)
coinpctchg1h3.grid(row=10, column=3)
coinpctchg1h4.grid(row=10, column=4)
coinpctchg1h5.grid(row=10, column=5)

coinpctchg24h.grid(row=11, column=0)
coinpctchg24h1.grid(row=11, column=1)
coinpctchg24h2.grid(row=11, column=2)
coinpctchg24h3.grid(row=11, column=3)
coinpctchg24h4.grid(row=11, column=4)
coinpctchg24h5.grid(row=11, column=5)

coinpctchg7d.grid(row=12, column=0)
coinpctchg7d1.grid(row=12, column=1)
coinpctchg7d2.grid(row=12, column=2)
coinpctchg7d3.grid(row=12, column=3)
coinpctchg7d4.grid(row=12, column=4)
coinpctchg7d5.grid(row=12, column=5)

coinlastupdate.grid(row=13, column=0)
coinlastupdate1.grid(row=13, column=1)
coinlastupdate2.grid(row=13, column=2)
coinlastupdate3.grid(row=13, column=3)
coinlastupdate4.grid(row=13, column=4)
coinlastupdate5.grid(row=13, column=5)


# calc function updates the stats based on the dropdown menu selections
def calc():
    itemone = variable.get()
    itemtwo = variable1.get()
    itemthree = variable2.get()
    itemfour = variable3.get()
    itemfive = variable4.get()
    '''
    cryptolist = []
    cryptolist.append(itemone)
    cryptolist.append(itemtwo)
    '''
# Here is where we look up values for the first dropdown menu item
    r = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+itemone+'/')
    r_body = r.read()
    j = json.loads(r_body.decode("utf-8"))
# Here is where we update all of the items in column 1
    coinid1.config(text = str(j[0]['id']))
    coinname1.config(text = str(j[0]['name']))
    coinsym1.config(text = str(j[0]['symbol']))
    coinrank1.config(text = str(j[0]['rank']))
    coinprice1.config(text = str(j[0]['price_usd']))
    coinmktcap1.config(text = str(j[0]['market_cap_usd']))
    coinavlsup1.config(text = str(j[0]['available_supply']))
    cointotsup1.config(text = str(j[0]['total_supply']))
    coinmaxsup1.config(text = str(j[0]['max_supply']))
    coinpctchg1h1.config(text = str(j[0]['percent_change_1h']))
    if float(j[0]['percent_change_1h']) < 0:
        coinpctchg1h1.config(fg='Red')
    else:
        coinpctchg1h1.config(fg='Green')
    coinpctchg24h1.config(text = str(j[0]['percent_change_24h']))
    if float(j[0]['percent_change_24h']) < 0:
        coinpctchg24h1.config(fg='Red')
    else:
        coinpctchg24h1.config(fg='Green')
    coinpctchg7d1.config(text = str(j[0]['percent_change_7d']))
    if float(j[0]['percent_change_7d']) < 0:
        coinpctchg7d1.config(fg='Red')
    else:
        coinpctchg7d1.config(fg='Green')
    coinlastupdate1.config(text = str(j[0]['last_updated']))

# Here is where we look up values for the second dropdown menu item
    s = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+itemtwo+'/')
    s_body = s.read()
    k = json.loads(s_body.decode("utf-8"))
# Here is where we update all of the items in column 2
    coinid2.config(text = str(k[0]['id']))
    coinname2.config(text = str(k[0]['name']))
    coinsym2.config(text = str(k[0]['symbol']))
    coinrank2.config(text = str(k[0]['rank']))
    coinprice2.config(text = str(k[0]['price_usd']))
    coinmktcap2.config(text = str(k[0]['market_cap_usd']))
    coinavlsup2.config(text = str(k[0]['available_supply']))
    cointotsup2.config(text = str(k[0]['total_supply']))
    coinmaxsup2.config(text = str(k[0]['max_supply']))
    coinpctchg1h2.config(text = str(k[0]['percent_change_1h']))
    if float(k[0]['percent_change_1h']) < 0:
        coinpctchg1h2.config(fg='Red')
    else:
        coinpctchg1h2.config(fg='Green')
    coinpctchg24h2.config(text = str(k[0]['percent_change_24h']))
    if float(k[0]['percent_change_24h']) < 0:
        coinpctchg24h2.config(fg='Red')
    else:
        coinpctchg24h2.config(fg='Green')
    coinpctchg7d2.config(text = str(k[0]['percent_change_7d']))
    if float(k[0]['percent_change_7d']) < 0:
        coinpctchg7d2.config(fg='Red')
    else:
        coinpctchg7d2.config(fg='Green')
    coinlastupdate2.config(text = str(k[0]['last_updated']))

# Here is where we look up values for the third dropdown menu item
    t = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+itemthree+'/')
    t_body = t.read()
    l = json.loads(t_body.decode("utf-8"))
# Here is where we update all of the items in column 2
    coinid3.config(text = str(l[0]['id']))
    coinname3.config(text = str(l[0]['name']))
    coinsym3.config(text = str(l[0]['symbol']))
    coinrank3.config(text = str(l[0]['rank']))
    coinprice3.config(text = str(l[0]['price_usd']))
    coinmktcap3.config(text = str(l[0]['market_cap_usd']))
    coinavlsup3.config(text = str(l[0]['available_supply']))
    cointotsup3.config(text = str(l[0]['total_supply']))
    coinmaxsup3.config(text = str(l[0]['max_supply']))
    coinpctchg1h3.config(text = str(l[0]['percent_change_1h']))
    if float(l[0]['percent_change_1h']) < 0:
        coinpctchg1h3.config(fg='Red')
    else:
        coinpctchg1h3.config(fg='Green')
    coinpctchg24h3.config(text = str(l[0]['percent_change_24h']))
    if float(l[0]['percent_change_24h']) < 0:
        coinpctchg24h3.config(fg='Red')
    else:
        coinpctchg24h3.config(fg='Green')
    coinpctchg7d3.config(text = str(l[0]['percent_change_7d']))
    if float(l[0]['percent_change_7d']) < 0:
        coinpctchg7d3.config(fg='Red')
    else:
        coinpctchg7d3.config(fg='Green')
    coinlastupdate3.config(text = str(l[0]['last_updated']))

# Here is where we look up values for the fourth dropdown menu item
    u = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+itemfour+'/')
    u_body = u.read()
    m = json.loads(u_body.decode("utf-8"))
# Here is where we update all of the items in column 2
    coinid4.config(text = str(m[0]['id']))
    coinname4.config(text = str(m[0]['name']))
    coinsym4.config(text = str(m[0]['symbol']))
    coinrank4.config(text = str(m[0]['rank']))
    coinprice4.config(text = str(m[0]['price_usd']))
    coinmktcap4.config(text = str(m[0]['market_cap_usd']))
    coinavlsup4.config(text = str(m[0]['available_supply']))
    cointotsup4.config(text = str(m[0]['total_supply']))
    coinmaxsup4.config(text = str(m[0]['max_supply']))
    coinpctchg1h4.config(text = str(m[0]['percent_change_1h']))
    if float(m[0]['percent_change_1h']) < 0:
        coinpctchg1h4.config(fg='Red')
    else:
        coinpctchg1h4.config(fg='Green')
    coinpctchg24h4.config(text = str(m[0]['percent_change_24h']))
    if float(m[0]['percent_change_24h']) < 0:
        coinpctchg24h4.config(fg='Red')
    else:
        coinpctchg24h4.config(fg='Green')
    coinpctchg7d4.config(text = str(m[0]['percent_change_7d']))
    if float(m[0]['percent_change_7d']) < 0:
        coinpctchg7d4.config(fg='Red')
    else:
        coinpctchg7d4.config(fg='Green')
    coinlastupdate4.config(text = str(m[0]['last_updated']))

# Here is where we look up values for the fifth dropdown menu item
    v = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+itemfive+'/')
    v_body = v.read()
    n = json.loads(v_body.decode("utf-8"))
# Here is where we update all of the items in column 2
    coinid5.config(text = str(n[0]['id']))
    coinname5.config(text = str(n[0]['name']))
    coinsym5.config(text = str(n[0]['symbol']))
    coinrank5.config(text = str(n[0]['rank']))
    coinprice5.config(text = str(n[0]['price_usd']))
    coinmktcap5.config(text = str(n[0]['market_cap_usd']))
    coinavlsup5.config(text = str(n[0]['available_supply']))
    cointotsup5.config(text = str(n[0]['total_supply']))
    coinmaxsup5.config(text = str(n[0]['max_supply']))
    coinpctchg1h5.config(text = str(n[0]['percent_change_1h']))
    if float(n[0]['percent_change_1h']) < 0:
        coinpctchg1h5.config(fg='Red')
    else:
        coinpctchg1h5.config(fg='Green')
    coinpctchg24h5.config(text = str(n[0]['percent_change_24h']))
    if float(n[0]['percent_change_24h']) < 0:
        coinpctchg24h5.config(fg='Red')
    else:
        coinpctchg24h5.config(fg='Green')
    coinpctchg7d5.config(text = str(n[0]['percent_change_7d']))
    if float(n[0]['percent_change_7d']) < 0:
        coinpctchg7d5.config(fg='Red')
    else:
        coinpctchg7d5.config(fg='Green')
    coinlastupdate5.config(text = str(n[0]['last_updated']))

'''
    listofkeys = ['id','name','symbol','rank','price_usd','market_cap_usd','available_supply','total_supply',
                  'max_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated']
    listofspecs1 = [coinid1, coinname1, coinsym1, coinrank1, coinprice1, coinmktcap1, coinavlsup1, cointotsup1,
                    coinmaxsup1, coinpctchg1h1, coinpctchg24h1, coinpctchg7d1, coinlastupdate1]
'''
'''
    for cryptoitem in cryptolist:
        r = urllib.request.urlopen(url='https://api.coinmarketcap.com/v1/ticker/'+cryptoitem+'/')
        r_body = r.read()

# https://docs.python.org/3/library/json.html
        j = json.loads(r_body.decode("utf-8"))
    #newdict = r.json()
    #listtodict = newdict[0]

    #listofkeys = ['id','name','symbol','rank','price_usd','market_cap_usd','available_supply','total_supply','max_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated']
    #for item in listofkeys:
    #    print(item, '= ', listtodict[item])
        print('\n')
        print(type(j))
        print(j)
        iter=0
        for item in j:
            foo = list(item.keys())
        #bar = list(item.values())
            for itemkey in foo:
                print(itemkey + ':')
                print(list(item.values())[iter])
                print('\n')
                iter+=1
'''
# Update Prices on Launch
calc()

# Button Labels and Commands
calcButton = Button(row2, text="UPDATE", command = calc)
calcButton.grid(row=1, column=1)

exitButton = Button(row2, text="EXIT",command=lambda: exit())
exitButton.grid(row=1, column=2)

'''
lbl = Label(row3)
lbl.grid(row=2, column=2)
'''

root.mainloop()



