import csv
f=open ("ProAbuseRedditsEval(1).csv")
csv_f = csv.reader(f)
i=1
count=0
text_file = open("Writing_for_new_comp.csv","w")
#add alcohol names
alist = ["marijuana","blunt","dope",
"ganja", "grass","herb", "joint", "bud",
"mary jane"," pot", "reefer", "green", "trees",
"smoke", "sinsemilla", "skunk", "weed","smoked","swallowed",
"hashish","Boom", "gangster", "hash", "hash oil", "hemp",
"heroin","smack", "horse", "brown sugar", "dope", "junk", "skag",
"skunk", "white horse", "China white","antihistamine","injected","snorted",
"opium","Laudanum", "paregoric","big O", "black stuff", "block", "gum","hop",
"cocaine","blow", "bump", "candy", "Charlie", "coke", "crack", "flake",
"rock", "snow", "toot","AMPHETAMINE","Biphetamine","Dexedrine","bennies",
"black beauties","crosses", "hearts", "LA turnaround", "speed", "truck drivers",
"uppers","METHAMPHETAMINE","Desoxyn","meth", "ice", "crank", "chalk", "crystal",
"fire", "glass", "go fast", "speed","MDMA","METHYLENEDIOXYMETHAMPHETAMINE",
"Ecstasy", "Adam", "clarity", "Eve", "lovers' speed", "Molly", "peace", "uppers",
"FLUNITRAZEPAM","Rohypnol","date rape drug","forget me pill", "Mexican Valium", "R2", "roach",
"Roche", "roofies", "roofinol", "rope", "rophies","GHB","Gamma-hydroxybutyrate","Georgia home boy",
"grievous bodily harm", "liquid ecstasy", "soap", "scoop", "goop", "liquid X","chewed","KETAMINE",
"Ketalar SV",   "cat Valium", "spec ial k", "vitamin k", "PCP", "ANALOGS", "Phencyclidine", "angel dust", "boat", "hog", "love boat",
"peace pill","SALVIA DIVINORUM","Salvia", "Shepherdess’s Herb", "Maria Pastora", "magic mint", "Sally-D","DEXTROMETHORPHAN", "DXM",
"Robotripping", "Robo", "Triple C","LSD","Lysergic acid diethylamide","acid", "blotter", "cubes", "microdot", "yellow sunshine",
"blue heaven","absorbed","MESCALINE","Buttons", "cactus", "mesc", "peyote","PSILOCYBIN","Magic mushrooms", "purple passion",
"shrooms", "little smoke","ANABOLIC STEROIDS","Anadrol", "Oxandrin", "Durabolin", "Depo-Testosterone", "Equipoise",
"roids", "juice", "gym candy", "pumpers","INHALANTS","Solvents","butane", "propane", "aerosol propellants", "nitrous oxide",
"nitrites","isoamyl", "isobutyl", "cyclohexyl","laughing gas", "poppers", "snappers", "whippets"
         ]
#add recovery words
alist2= ["recovery","recover","tradition","addict","Withdrawal","treatment","Abstinence",
"Acetaminophens","ACOA","Addiction Assessment","Addiction Treatment","Addiction","Addictive Personality",
"Adverse Reaction","Affinity","Age at Onset","Agonist","Alcoholics Anonymous","AA","Alkaloids",
"Amphetamine","Analgesic","Antagonist","AOD","AODA","Aspirin","Barbiturate","Benzodiazepine",
"Bioavailability","Biofeedback","Blood Alcohol Level","Blood Alcohol Concentration","Buprenorphine",
"Step","NA","Narcotics","Anonymous","didnt","years","tradition","started","God","ought",
"alcoholics","caffeine","carcinogen","casual factors","ceiling effect","Center for Substance Abuse Treatment",         
"CSAT","Central nervous system","CNS","Cirhosis","Clinical Opiate Withdrawal Scale","cows",
"codeine","codependence","cold turkey","compulsions","conditioning","craving","crisis intervention",
"cross dependence","cross tolerance","doc","denial","depressants","depression","detoxification","Detoxification ",
"Disease","Dopamine","downers","drug misuse","drug tolerance","dui","dwi","dysphoria",
"Dysynergy","Enabling","opioid","habit","endorphins","ethanol","euphoria","excepient","help"
         ]
bl=0
asd=0
bl2=0
k=0

for row in csv_f:
    if (i==1):
        for col in row:
            text_file.write(col+",")
    else:
        temp=""
        for k in row:
            temp = k.lower()
        #print ("This is temp:"+temp)
        for j in range (len(alist)):
            if (temp.count(alist[j].lower())>0):
                bl=bl+(temp.count(alist[j].lower())/(len(temp)))
        for cnt in range(len (alist2)):
            if (temp.count(alist2[cnt].lower())>0):
                bl2=bl2+((temp.count(alist2[cnt].lower())>0)/(len(temp)))
    
    text_file.write(str(bl)+","+str(bl2)+"\n")
    count=0
    bl=0
    bl2=0
    i=i+1
    #k=k+1
    #print (temp)

#print (asd)

#f1.close()
f.close()

f=open ("RecoveryPosts(1).csv")
csv_f = csv.reader(f)
i=1
count=0
#text_file = open("Writing_for_new_comp.csv","w")
bl=0
asd=0
bl2=0
k=0
for row in csv_f:
    if (i==1):
        #for col in row:
        text_file.write("Recovery,Subreddits")
    else:
        temp=""
        for k in row:
            temp = k.lower()
        #print ("This is temp:"+temp)
        for j in range (len(alist)):
            if (temp.count(alist[j].lower())>0):
                bl=bl+(temp.count(alist[j].lower())/(len(temp)))
        for cnt in range(len (alist2)):
            if (temp.count(alist2[cnt].lower())>0):
                bl2=bl2+((temp.count(alist2[cnt].lower())>0)/(len(temp)))
    
            
    text_file.write(str(bl)+","+str(bl2)+"\n")
    count=0
    bl=0
    bl2=0
    i=i+1
    #k=k+1
    #print (temp)

#print (asd)
text_file.close()
#f1.close()
f.close()
