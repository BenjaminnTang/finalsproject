import time
import random
appleShare = random.randint(200,300)
alphabetShare = random.randint(1300,1400)
berkshireShare = random.randint(338000,339000)
purchasedStocks = []
costStock = []



def ending(ownedMoney):
  print("You purchased: "+ str(purchasedStocks))
  print("Cost of each transaction: "+str(costStock))
  redo = input("Would you like to purchase another stock (Y/N):  ")
  if redo == "Y":
    stockType = input("What stock would you like to buy? Your options are APPL BRKA GOOG:  ")
    stockChoose(stockType,ownedMoney)
  elif redo == "N":
    print("You purchased: "+ str(purchasedStocks))
    print("Amount of money in stock (this is subject to change with market fluctuation): "+str(costStock))
    print("THANK YOU FOR PURCHASING WITH US")

def stockChoose(stockType,ownedMoney):
  if stockType == "APPL":
    APPL(ownedMoney)
  elif stockType == "BRKA":
    BRKA(ownedMoney)
  elif stockType == "GOOG":
    GOOG(ownedMoney)
  else:
    print("INVALID FOOD")



def APPL(ownedMoney):
  if ownedMoney < appleShare:
    print("You do not have enough money!")
    ending(ownedMoney)
  elif ownedMoney >= appleShare:

    ableShares = float(ownedMoney/appleShare)
    print("APPL shares are worth: $"+ str(appleShare))
    print("You can buy "+ str(ableShares)+ " shares of APPL stock.")
    sharePurchase = float(input("How many shares would you like to purchase:  "))
    if sharePurchase >= 1:
      print("Purchase pending. Please wait...")
      amountStock = sharePurchase*appleShare
      purchasedStocks.append("APPL: "+ str(sharePurchase))
      costStock.append(amountStock)
      ownedMoney = ownedMoney-amountStock
      print("You now have: $" + str(ownedMoney))
      time.sleep(3)
      ending(ownedMoney)
    elif sharePurchase < 1:
      print("That is too small of a fraction.")

def BRKA(ownedMoney):
  if ownedMoney < berkshireShare:
    print("You do not have enough money!")
    ending(ownedMoney)
  elif ownedMoney >= berkshireShare:
    ableShares = float(ownedMoney/berkshireShare)
    print("BRK.A shares are worth: $"+ str(berkshireShare))
    print("You can buy "+ str(ableShares)+ " shares of BRKA stock.")
    sharePurchase = float(input("How many shares would you like to purchase:  "))
    if sharePurchase >= 1:
      print("Purchase pending. Please wait...")
      amountStock = sharePurchase*berkshireShare
      purchasedStocks.append("BRKA: "+ str(sharePurchase))
      costStock.append(amountStock)
      ownedMoney = ownedMoney-amountStock
      print("You now have: $" + str(ownedMoney))
      time.sleep(3)
      ending(ownedMoney)
    elif sharePurchase < 1:
      print("That is too small of a fraction.")

def GOOG(ownedMoney):
  if ownedMoney < alphabetShare:
    print("You do not have enough money!")
    ending(ownedMoney)
  elif ownedMoney >= alphabetShare:
    ableShares = float(ownedMoney/alphabetShare)
    print("GOOG shares are worth: $"+ str(alphabetShare))
    print("You can buy "+ str(ableShares)+ " shares of GOOG stock.")
    sharePurchase = float(input("How many shares would you like to purchase:  "))
    if sharePurchase >= 1:
      print("Purchase pending. Please wait...")
      amountStock = sharePurchase*alphabetShare
      purchasedStocks.append("GOOG: "+ str(sharePurchase))
      costStock.append(amountStock)
      ownedMoney = ownedMoney-amountStock
      print("You now have: $" + str(ownedMoney))
      time.sleep(3)
      ending(ownedMoney)
    elif sharePurchase < 1:
      print("That is too small of a fraction.")


print("Welcome to Stock Management")
time.sleep(1)
portfolio = int(input("How much money to put in your account:  $"))
ownedMoney = portfolio
stockType = input("What would you like to buy? Your options are APPL BRKA GOOG:  ")
stockChoose(stockType,ownedMoney)

