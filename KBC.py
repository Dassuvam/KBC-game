name=input("Please enter your name: ")
print(f"---Namaskar {name}---","Welcome to our show KBC (Kyun banega crorepati!)",sep="\n")
print("Main Amitab bacchan nahin hun lekin apka swagat karta hun.")
prize=0
questions=[("1.What is the capital of India?","c"),("2.What is the northest state of India?","a"),("3.Which state has the highest number of temples in India?","d"),("4.Who was the first prime minister of India?","c"),("5.When gandhiji was born?","a"),("6.National Institute of Nutrition is located in which of the following place?","b"),("7.Who invented Computer?","d"),("8.How many cards are there in a complete pack of cards?","b"),("9.Which one is not amongst the Seven Wonders of the World?","c"),("10.Which is the biggest water animal?","a")]

print("Please choose the correct option of the questions given below")

print()
#First question
print("Pehla sawaal apke screen par ")
print(f"{questions[0][0]}","a.Bhubaneswar        b.Bhopal","c. New Delhi         d.Goa",sep="\n")
a1=input()

if a1==questions[0][1]:
    prize=prize+1000 #prize=1000
    print("Congratulations you won 1000 rupees")
else:
    print(f"Sorry! you only won {prize} rupees.")

#Second question
if prize==1000:
    print()
    print("Dusra sawaal apke screen par ")
    print(f"{questions[1][0]}","a.Jammun and Kashmir        b.Arunachal pradesh","c.Punjab                    d.Sikkim",sep="\n")
    a2=input()
    if a2==questions[1][1]:
        prize=prize+5000 #prize=6000
        print("Congratulations you won 5000 rupees")
    else:
        print(f"Sorry! you only won {prize} rupees.")

#Third question
if prize==6000:
    print()
    print("Tisra sawaal apke screen par ")
    print(f"{questions[2][0]}","a.Andhra Pradesh        b.Arunachal Pradesh","c. Odisha               d.Tamilnadu",sep="\n")
    a3=input()
    if a3==questions[2][1]:
        prize=prize+10000 #prize=16000
        print("Congratulations you won 16000 rupees")
    else:
        print(f"Sorry! you only won {prize} rupees.")

#Fourth question
if prize==16000:
    print()
    print("Chautha sawaal apke screen par ")
    print(f"{questions[3][0]}","a.Rajiv Gandhi                b.Atal Bihari Vajpayee","c.Dr. Jawaharlal Nehru        d.Dr. Rajendra Prashad",sep="\n")
    a4=input()
    if a4==questions[3][1]:
        prize=prize+50000 #prize=66000
        print("Congratulations you won 66000 rupees")
    else:
        print(f"Sorry! you only won {prize} rupees.")

#Fifth question
if prize==66000:
    print()
    print("Panchwa sawaal apke screen par ")
    print(f"{questions[4][0]}","a.1869        b.2021","c. 1857         d.1987",sep="\n")
    a5=input()
    if a5==questions[4][1]:
        prize=prize+100000 #prize=166,000
        print("Congratulations you won 100000 rupees")
    else:
        print(f"sorry! you only won {prize} rupees.")


#Sixth question
if prize==166000:
    print()
    print("Chatha sawaal apke screen par ")
    print(f"{questions[5][0]}","a.Bangalore         b.Hyderabad","c.Gandhinagar       d.Mumbai",sep="\n")
    a6=input()
    if a6==questions[5][1]:
        prize=prize+150000 #prize=316,000
        print("Congratulations you won 150000 rupees")
    else:
        print(f"sorry! you only won {prize} rupees.")


#Seventh question

if prize==316000:
    print()
    print("Satwa sawaal apke screen par ")
    print(f"{questions[6][0]}","a.Benjamin Franklin         b.Schuyler Wheeler","c.Thomas Edition            d.Charles Babbage",sep="\n")
    a7=input()
    if a7==questions[6][1]:
        prize=prize+300000 #prize=616,000
        print("Congratulations you won 300000 rupees")
        
    else:
        print(f"sorry! you only won {prize} rupees.")



#Eighth question
print()
if prize==616000:
    print()
    print("Athwa sawaal apke screen par ")
    print(f"{questions[7][0]}","a.78         b.52","c.50         d.36",sep="\n")
    a8=input()
    if a8==questions[7][1]:
        prize=prize+600000 #prize=1,216,000
        print("Congratulations you won 600,000 rupees")
        
    else:
        print(f"sorry! you only won {prize} rupees.")




#Ninth question
if prize==1216000:
    print()
    print("Nawa sawaal apke screen par ")
    print(f"{questions[8][0]}","a.The Statue of Jupiter Olympusb             b.The Pharos of Alexandriac","c.Great Wall of China                        d.The Pyramids of Egypt",sep="\n")
    a9=input()
    if a9==questions[8][1]:
        prize=prize+1000000 #prize=2,216,000
        print("Congratulations you won 10,00,000 rupees")
        
    else:
        print(f"sorry! you only won {prize} rupees.")


 #Tenth question
if prize==2216000:
    print()
    print("Daswa sawaal apke screen par ")
    print(f"{questions[9][0]}","a.The Antarctic blue whale             b.Shark","c.The orca                             d.Jellyfish",sep="\n")
    a10=input()
    if a10==questions[9][1]:
        prize=prize+2000000 #prize=4,216,000
        print("Congratulations you won 20,00,000 rupees")
    else:
        print(f"sorry! you only won {prize} rupees.")
    print()
    print(f"You won total{prize} amount.")