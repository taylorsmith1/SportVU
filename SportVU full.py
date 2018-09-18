import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
locationList = []
from matplotlib import animation
import math
import matplotlib.patches as patches

#empty lists for later in the code
debug = [] #what debug will look like = (['-1,-1,87.54737,23.86569,10.28598', '1388,518947,64.66823,30.62035,0', '1388,601140,85.22813,49.15521,0', '1388,603106,88.9034,23.36837,0', '1388,696289,73.43097,32.33427,0', '1388,756880,86.7318,24.66779,0', '1415,511656,87.54607,19.54386,0', '1415,551112,88.07635,25.60749,0', '1415,567438,68.38883,29.64232,0', '1415,708860,85.70579,29.88771,0', '1415,793931,85.53059,46.0505,0', '-2,1,74.03399,.95034,0', '-2,2,49.05593,44.40467,0', '-2,3,5.66466,44.72798,0'], '0.04')
locations = [] #what locations will look like = ['-1,-1,87.9737,23.4282,10.01662', '1388,518947,64.59515,30.53716,0', '1388,601140,85.24362,49.17065,0', '1388,603106,88.82827,23.58246,0', '1388,696289,73.44262,32.35331,0', '1388,756880,86.97407,24.62815,0', '1415,511656,87.61413,19.55454,0', '1415,551112,88.42379,25.66908,0', '1415,567438,68.38909,29.56728,0', '1415,708860,85.74107,29.89637,0', '1415,793931,85.55584,46.00625,0', '-2,1,74.02454,.95388,0', '-2,2,49.05593,44.40467,0', '-2,3,5.66585,44.67947,0']
clock = [] #what clock will look like = '1.68', '1.64', '1.60', '1.56', '1.52', '1.48', '1.44', '1.40', '1.36', '1.32', '1.28', '1.24', '1.20', '1.16', '1.12', '1.08', '1.04', '1.00', '0.96', '0.92', '0.88', '0.84', '0.80', '0.76', '0.72', '0.68', '0.64', '0.60', '0.56', '0.52', '0.48', '0.44', '0.40', '0.36', '0.32', '0.28', '0.24', '0.20', '0.16', '0.12', '0.08', '0.04', '0.00'
clock_new = [] #what clock_new will look like = '1.68', '1.64', '1.60', '1.56', '1.52', '1.48', '1.44', '1.40', '1.36', '1.32', '1.28', '1.24', '1.20', '1.16', '1.12', '1.08', '1.04', '1.00', '0.96', '0.92', '0.88', '0.84', '0.80', '0.76', '0.72', '0.68', '0.64', '0.60', '0.56', '0.52', '0.48', '0.44', '0.40', '0.36', '0.32', '0.28', '0.24', '0.20', '0.16', '0.12', '0.08', '0.04', '0.00'
locations_new = [] #what locations_new will look like = ['-1,-1,87.9737,23.4282,10.01662', '1388,518947,64.59515,30.53716,0', '1388,601140,85.24362,49.17065,0', '1388,603106,88.82827,23.58246,0', '1388,696289,73.44262,32.35331,0', '1388,756880,86.97407,24.62815,0', '1415,511656,87.61413,19.55454,0', '1415,551112,88.42379,25.66908,0', '1415,567438,68.38909,29.56728,0', '1415,708860,85.74107,29.89637,0', '1415,793931,85.55584,46.00625,0', '-2,1,74.02454,.95388,0', '-2,2,49.05593,44.40467,0', '-2,3,5.66585,44.67947,0']
debug_new = [] #what debug_new will look like = (['-1,-1,87.54737,23.86569,10.28598', '1388,518947,64.66823,30.62035,0', '1388,601140,85.22813,49.15521,0', '1388,603106,88.9034,23.36837,0', '1388,696289,73.43097,32.33427,0', '1388,756880,86.7318,24.66779,0', '1415,511656,87.54607,19.54386,0', '1415,551112,88.07635,25.60749,0', '1415,567438,68.38883,29.64232,0', '1415,708860,85.70579,29.88771,0', '1415,793931,85.53059,46.0505,0', '-2,1,74.03399,.95034,0', '-2,2,49.05593,44.40467,0', '-2,3,5.66466,44.72798,0'], '0.04')

roster_all = [] #emplty list that will have all IDs w/ repeats
roster_H = [] #empty list that will have all home IDs w/o repeats
roster_home = [] #empty list that will have all home IDs w/ repeats
roster_A = [] #empty list that will have all away IDs w/o repeats
roster_away = [] #empty list that will have all away IDs w/ repeats

root = etree.parse('SportVU.XML').getroot() #parses into the SportVU.XML file and gets root

#distance variables set to zero for later in the code
BallDistance = 0
Player1Distance = 0
Player2Distance = 0
Player3Distance = 0
Player4Distance = 0
Player5Distance = 0
Player6Distance = 0
Player7Distance = 0
Player8Distance = 0
Player9Distance = 0
Player10Distance = 0

Ref1Distance = 0
Ref2Distance = 0
Ref3Distance = 0

Distance = 0
Distance2 = 0
Distance3 = 0
Distance4 = 0
Distance5 = 0
Distance6 = 0
Distance7 = 0
Distance8 = 0
Distance9 = 0
Distance10 = 0

timeOnLeft = 0
timeOnRight = 0
#time_skip uses user input to specify what part of the game to read data from. 


#locations from XML file
for coordinate in root.iter('moment'): #looks at the 'moment' section of the XML file
    location = coordinate.get('locations') #gets the coordinates from the 'locations' section of 'moment'
    lsplit = location.split(';') #splits each location at the ";" This pairs each coordinate with a sperate player. This is stored into the variable 'lsplit'
    locations.append(lsplit) #the variable lsplit is appended to the empty list 'locations'
    
#adding game clock to the locations list
for time in root.iter('moment'): #looks at the 'moment' section of the XML file
    game_clock = time.get('game-clock') #gets the data from the 'game-clock' and stores it in the variable game_clock.
    clock.append(game_clock) #appends the data from the variable game_clock to the list clock.
    
for a, b in zip(locations, clock): #zips the two lists locations and clock together
    time_point = a, b #the zipped lists are put into the variable time_point
    debug.append(time_point) #the variable time_point (which contains the two zipped lists) is appended to the masterlist 'debug'.
    
for player in root.iter('moment'): #looks at the 'moment' section of the XML file
    location = player.get('locations') #gets the coordinates from the 'locations' section of 'moment'
    lsplit = location.split(';') #splits each location at the ";" This pairs each coordinate with a sperate player. This is stored into the variable 'lsplit'
    locations.append(lsplit) #the variable lsplit is appended to the empty list 'locations'
    
    for x in lsplit:    

        if x[0:4] == '1388':  
            roster_all.append(x[5:11])
            roster_home.append(x[5:11])   
        if x[0:4] == '1415':    
            roster_all.append(x[5:11])
            roster_away.append(x[5:11])
            
    
#print(lsplit)
#print(locations)    
#print(locations_new)

#Creates a roster of all the player IDs w/ repeats
#appended to a master list and a team list
'''
for x in lsplit:    

    if x[0:4] == '1388':  
        roster_all.append(x[5:11])
        roster_home.append(x[5:11])   
    if x[0:4] == '1415':    
        roster_all.append(x[5:11])
        roster_away.append(x[5:11])
'''
#print(roster_all)            
#print(roster_home)
#print(roster_away)

#eliminates any repeated IDs to make a list with all the players on home team
for x in roster_home:
    if x not in roster_H:
        roster_H.append(x)
        
#print(roster_H)    

#eliminates any repeated IDs to make a list with all the players on away team
for x in roster_away:
    if x not in roster_A:
        roster_A.append(x)
#print(roster_H)    

HP1 = []
HP2 = []
HP3 = []
HP4 = []
HP5 = []

AP1 = []
AP2 = []
AP3 = []
AP4 = []
AP5 = []

#eliminates any repeated IDs to make a list with all the players on away team
for x in roster_away:
    if x not in roster_A:
        roster_A.append(x)
        
        
for y in range(0, len(locations)):
    for x in locations[y][1]:
        spit = locations[y][1].split(',')
    HP1.append(spit[1])
    for x in locations[y][2]:
        spit1 = locations[y][2].split(',')
    HP2.append(spit1[1])
    for x in locations[y][3]:
        spit2 = locations[y][3].split(',')
    HP3.append(spit2[1])
    for x in locations[y][4]:
        spit3 = locations[y][4].split(',')
    HP4.append(spit3[1])
    for x in locations[y][5]:
        spit4 = locations[y][5].split(',')
    HP5.append(spit4[1])   
    
    for x in locations[y][6]:
        spit5 = locations[y][6].split(',')
    AP1.append(spit5[1])
    for x in locations[y][7]:
        spit6 = locations[y][7].split(',')
    AP2.append(spit6[1])
    for x in locations[y][8]:
        spit7 = locations[y][8].split(',')
    AP3.append(spit7[1])
    for x in locations[y][9]:
        spit8 = locations[y][9].split(',')
    AP4.append(spit8[1])
    for x in locations[y][10]:
        spit9 = locations[y][10].split(',')
    AP5.append(spit9[1]) 

#print(HP1)

      
#print(roster_A)

#Initializes new lists and dictionaries for the following code
loc = [] #What loc will look like = ('72.74545', '35.91284'), (72.74545, 35.91284), (82.06767, 37.50055), (69.51486, 13.8965), (77.65809, 30.40215), (58.1465, 25.66116), (46.98763, 25.25215), (58.74507, 5.63265), (80.39471, 45.61375), (78.04007, 17.99373), ('73.18553', '35.8001'), (73.18553, 35.8001), (82.13756, 37.628), (69.87061, 13.81557), (77.8562, 30.43987), (58.19425, 25.61018), (47.39744, 25.19376), (59.33498, 5.58458), (80.54585, 45.68619), (78.2248, 18.01721), ('73.61678', '35.69096'), (73.61678, 35.69096), (82.20631, 37.75208), (70.23848, 13.72039), (78.025, 30.46916), (58.248, 25.5491)
player = [] #What player will look like = [603106.0, 696289.0, 696290.0, '756880', 756880.0, 567438.0, 708860.0, 720555.0, 793930.0, 601140.0, 603106.0, 696289.0, 696290.0, '756880', 756880.0, 567438.0, 708860.0, 720555.0, 793930.0
dic = {} #What dic will look like = 696289.0: [(46.01186, 33.38741), (45.99147, 33.40299), (45.9694, 33.41746), (45.94875, 33.43214), (45.92772, 33.4453), (45.90986, 33.45706), (45.89544, 33.46716), (45.88077, 33.47687), (45.87197, 33.48281), (45.86925, 33.49052), (45.87375, 33.49698), (45.87501, 33.50487), (45.87979, 33.50801), (45.88305, 33.50725), (45.88052, 33.51222), (45.88083, 33.50984), (45.88017, 33.50764), (45.87933, 33.50863), (45.88016, 33.50711), (45.88221, 33.50801), (45.88055, 33.50849), (45.87133, 33.51094), (45.86426, 33.51156), (45.85668, 33.51647), (45.84673, 33.52169), (45.83675, 33.52875), (45.82732, 33.53165), (45.82203, 33.53697), (45.8196, 33.54029), (45.81978, 33.53893)]
#Use index 1:10


count = 0
for y in range(0, len(locations)): #This for loop is set up so it runs through each index of the list locations_new    
    a = locations[y][1] #Gets player one for each index of the list locations_new   (EX. 1388,601140,33.63567,24.19006,0)
    b = locations[y][2] #Gets player two for each index of the list locations_new
    c = locations[y][3]
    d = locations[y][4]
    e = locations[y][5]
    f = locations[y][6]
    g = locations[y][7]
    h = locations[y][8]
    i = locations[y][9]
    j = locations[y][10]

    
    split = a.split(',') #Splits the variable "a" each time it sees a comma    (EX. ['1388', 601140.0, 47.39744, 25.19376, '0'] )
    bsplit = b.split(',')
    csplit = c.split(',')
    dsplit = d.split(',')
    esplit = e.split(',')
    fsplit = f.split(',')
    gsplit = g.split(',')
    hsplit = h.split(',')
    isplit = i.split(',')
    jsplit = j.split(',')
    
    
    
    loc.append((split[2], split[3])) #Appends each x, y pair to an empty list "loc" in the form of a tupple. (EX. (47.39744, 25.19376) )
    loc.append((bsplit[2], bsplit[3]))
    loc.append((csplit[2], csplit[3]))
    loc.append((dsplit[2], dsplit[3]))
    loc.append((esplit[2], esplit[3]))
    loc.append((fsplit[2], fsplit[3]))
    loc.append((gsplit[2], gsplit[3]))
    loc.append((hsplit[2], hsplit[3]))
    loc.append((isplit[2], isplit[3]))
    loc.append((jsplit[2], jsplit[3]))    
    
    player.append(split[1]) #Appends each player ID to an empty list "player"  (EX. 601140)
    player.append(bsplit[1])
    player.append(csplit[1])
    player.append(dsplit[1])
    player.append(esplit[1])
    player.append(fsplit[1])
    player.append(gsplit[1])
    player.append(hsplit[1])
    player.append(isplit[1])
    player.append(jsplit[1])

    #    zipped = zip(split[1], (split[2], split[3]))

    #    masterlist.append(zipped)



    #count += 1

count = 0       
for x in player:
    dic.setdefault(x , []).append(loc[count]) #The function setdefault() takes the player ID's (x) and sets each individual ID as a seperate key in the dictionary. Each index of "loc" is then appended to the respective player ID. The final product of this function is each player ID paired with each (x,y) coordinate.
    count += 1
    

for x in range(0, len(dic['756880']) - 1):
    X1 = dic['756880'][x][0]
    Y1 = dic['756880'][x][1]
    X2 = dic['756880'][x+1][0]
    Y2 = dic['756880'][x+1][1]
    
    X1 = float(X1) #Turns each X and Y coordinate into a float. When something is turned into a float it makes the item a decimal. 
    Y1 = float(Y1)
    X2 = float(X2)
    Y2 = float(Y2)
    
    X = (X2-X1) #Stores the second X coordinate - the first X coordinate into the variable 'X'
    Y = (Y2-Y1)
    
    Distance = Distance + (math.hypot(X, Y)) #Uses the math.hypot() function to find the average distance of each player during the game. 

#print(Distance)   
#print (set_player)

gdis = []
gdis1 = []
gdis2 = []
gdis3 = []
gdis4 = []
gdis5 = []
gdis6 = []
gdis7 = []
gdis8 = []
gdis9 = []

for y in roster_H:
    try:
        for x in range(0, len(dic[y]) - 1):
            X1 = dic[y][x][0]
            Y1 = dic[y][x][1]
            X2 = dic[y][x+1][0]
            Y2 = dic[y][x+1][1]
            
            X1 = float(X1) #Turns each X and Y coordinate into a float. When something is turned into a float it makes the item a decimal. 
            Y1 = float(Y1)
            X2 = float(X2)
            Y2 = float(Y2)
            
            X = (X2-X1) #Stores the second X coordinate - the first X coordinate into the variable 'X'
            Y = (Y2-Y1)
            if roster_H.index(y) == 0:
                Distance = Distance + (math.hypot(X, Y))
                gdis.append(Distance)
            if roster_H.index(y) == 1:
                Distance2 = Distance2 + (math.hypot(X, Y))
                gdis1.append(Distance2)
            if roster_H.index(y) == 2:
                Distance3 = Distance3 + (math.hypot(X, Y))
                gdis2.append(Distance3)                
            if roster_H.index(y) == 3:
                Distance4 = Distance4 + (math.hypot(X, Y))
                gdis3.append(Distance4)
            if roster_H.index(y) == 4:
                Distance5 = Distance5 + (math.hypot(X, Y))
                gdis4.append(Distance5)
            if roster_H.index(y) == 5:
                Distance5 = Distance5 + (math.hypot(X, Y))
                gdis5.append(Distance5)
            if roster_H.index(y) == 6:
                Distance6 = Distance6 + (math.hypot(X, Y))
                gdis6.append(Distance6)
            if roster_H.index(y) == 7:
                Distance7 = Distance7 + (math.hypot(X, Y))
                gdis7.append(Distance7)                
            if roster_H.index(y) == 8:
                Distance8 = Distance8 + (math.hypot(X, Y))
                gdis8.append(Distance8)
            if roster_H.index(y) == 9:
                Distance9 = Distance9 + (math.hypot(X, Y))
                gdis9.append(Distance9)
                
    except:
        if y not in dic:
            print([y], 'Not in Dictionary')

plt.plot(gdis)
plt.plot(gdis1)
plt.plot(gdis2)
plt.plot(gdis3)
plt.plot(gdis4)
plt.plot(gdis5)
plt.plot(gdis6)
plt.plot(gdis7)
plt.plot(gdis8)
plt.plot(gdis9)
plt.ylabel('Distance')
plt.show()


#BALL COORDIN


#BALL COORDINATES
#each player follows the same code as the ball, just different indicies. Therefore comments on this code are only nessary once. 
#four new empty lists are created for the following code
ball = []
ballList = []
ballCord = []
ballCordTime = []

for x in debug: #looks at each value in the list 'debug_new'
    ball.append(x[0][0]) #appends the first index of the first index of the list debug_new to the empty list 'ball'
    #It looks like ['-1,-1,x coordinate,y coordinate,z coordinate]
    #example = '-1,-1,75.91441,3.61214,4.35418'

for y in ball: #looks at each value in the list 'ball'
    split = y.split(',') #splits each value at the ',' just like above. This is stored into the variable 'split'
    ballList.append(split) #the variable split is appended to the empty list 'ballList' 
    #It looks like ['-1', '-1', x coordinate, y coordinate, 'z coordinate']. The '-1', '-1' states that these are the coordinates for the ball.
    #example = ['-1', '-1', 75.63154, 3.52432, '4.74702']
    
for a in ballList: #looks at each value in 'ballList'
    a[2] = float(a[2]) #turns the third index of 'ballList' into a float. A float is essentially a numerical value with decimals.
    a[3] = float(a[3]) #turns the fourth index of 'ballList' into a float.
    ballCord.append((a[2], a[3])) #appends the floats a[2] and a[3] to the list 'ballCord'. 
    #It looks like "(a[2], a[3]), (a[2], a[3])"
    #example = (75.63154, 3.52432)
    
for a, b in zip(ballCord, clock): #zips the list 'ballCord' (which contains the x and y coordinates of the ball) and clock_new together.
    location_time = a, b #the two zipped lists are put into the variable location_time
    ballCordTime.append(location_time) #the variable location_time is appended to 'ballCordTime'
    #it looks like ((x coordinate, y coordinate), 'time')
    #example = ((75.69035, 3.54136), '1190.20')

# print(ballCordTime)


#PLAYER 1 COORDINATES 
P1 = []
P1List = []
P1Cord = []
P1CordTime =[]
for x in debug:
    P1.append(x[0][1])
    
for y in P1:
    split = y.split(',')
    P1List.append(split)
    
for a in P1List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P1Cord.append((a[2], a[3]))
    
for a, b in zip(P1Cord, clock):
    location_time = a, b
    P1CordTime.append(location_time)
    
#print(P1CordTime)    
    
#PLAYER 2 COORDINATES

P2 = []
P2List = []
P2Cord = []
P2CordTime = []
for x in debug:
    P2.append(x[0][2])
    
for y in P2:
    split = y.split(',')
    P2List.append(split)
    
for a in P2List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P2Cord.append((a[2], a[3]))

for a, b in zip(P2Cord, clock):
    location_time = a, b
    P2CordTime.append(location_time)
    
    
#print(P2CordTime)
  
#PLAYER 3 COORDINATES

P3 = []
P3List = []
P3Cord = []
P3CordTime = []
for x in debug:
    P3.append(x[0][3])
    
for y in P3:
    split = y.split(',')
    P3List.append(split)
    
for a in P3List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P3Cord.append((a[2], a[3]))
    
for a, b in zip(P3Cord, clock):
    location_time = a, b
    P3CordTime.append(location_time)
    
#print(P3CordTime)

#PLAYER 4 COORDINATES

P4 = []
P4List = []
P4Cord = []
P4CordTime = []
for x in debug:
    P4.append(x[0][4])
    
for y in P4:
    split = y.split(',')
    P4List.append(split)
    
for a in P4List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P4Cord.append((a[2], a[3]))
    
for a, b in zip(P4Cord, clock):
    location_time = a, b
    P4CordTime.append(location_time)
    
#print(P4CordTime)

#PLAYER 5 COORDINATES

P5 = []
P5List = []
P5Cord = []
P5CordTime = []
for x in debug:
    P5.append(x[0][5])
    
for y in P5:
    split = y.split(',')
    P5List.append(split)
    
for a in P5List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P5Cord.append((a[2], a[3]))
    
for a, b in zip(P5Cord, clock):
    location_time = a, b
    P5CordTime.append(location_time)
    
    
#print(P5CordTime)

#PLAYER 6 COORDINATES

P6 = []
P6List = []
P6Cord = []
P6CordTime = []
for x in debug:
    P6.append(x[0][6])
    
for y in P6:
    split = y.split(',')
    P6List.append(split)
    
for a in P6List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P6Cord.append((a[2], a[3]))
    
for a, b in zip(P6Cord, clock):
    location_time = a, b
    P6CordTime.append(location_time)
    
#print(P6CordTime)

#PLAYER 7 COORDINATES

P7 = []
P7List = []
P7Cord = []
P7CordTime = []
for x in debug:
    P7.append(x[0][7])
    
for y in P7:
    split = y.split(',')
    P7List.append(split)
    
for a in P7List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P7Cord.append((a[2], a[3]))
    
for a, b in zip(P7Cord, clock):
    location_time = a, b
    P7CordTime.append(location_time)
    
#print(P7CordTime)

#PLAYER 8 COORDINATES

P8 = []
P8List = []
P8Cord = []
P8CordTime = []
for x in debug:
    P8.append(x[0][8])
    
for y in P8:
    split = y.split(',')
    P8List.append(split)
    
for a in P8List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P8Cord.append((a[2], a[3]))
    
for a, b in zip(P8Cord, clock):
    location_time = a, b
    P8CordTime.append(location_time)
    
#print(P8CordTime)

#PLAYER 9 COORDINATES

P9 = []
P9List = []
P9Cord = []
P9CordTime = []
for x in debug:
    P9.append(x[0][9])
    
for y in P9:
    split = y.split(',')
    P9List.append(split)
    
for a in P9List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P9Cord.append((a[2], a[3]))
    
for a, b in zip(P9Cord, clock):
    location_time = a, b
    P9CordTime.append(location_time)
    
#print(P9CordTime)

#PLAYER 10 COORDINATES            

P10 = []
P10List = []
P10Cord = []
P10CordTime = []
for x in debug:
    P10.append(x[0][10])
    
for y in P10:
    split = y.split(',')
    P10List.append(split)
    
for a in P10List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    P10Cord.append((a[2], a[3]))
    
for a, b in zip(P10Cord, clock):
    location_time = a, b
    P10CordTime.append(location_time)
    
#print(P10CordTime)

#ref coordinates taken out due to glitches in xml file

#REF 1 COORDINATES
'''
R1 = []
R1List = []
R1Cord = []
for x in debug:
    R1.append(x[1])
    
for y in R1:
    split = y.split(',')
    R1List.append(split)
    
for a in R1List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    R1Cord.append((a[2], a[3]))
    R1Cord.append(a[3])
    
#print(R1Cord)

#REF 2 COORDINATES

R2 = []
R2List = []
R2Cord = []
for x in debug:
    R2.append(x[1])
    
for y in R2:
    split = y.split(',')
    R2List.append(split)
    
for a in P1List:
    a[2] = float(a[2])
    a[3] = float(a[3])
    R2Cord.append((a[2], a[3]))
    
#print(R2Cord)

#REF 3 COORDINATES

R3, R3List, R3Cord = [], [], []
for x in debug:
    R3.append(x[1])
    
for y in R3:
    split = y.split(',')
    R3List.append(split)
    
for a in P1List:
    a[2], a[3] = float(a[2]), float(a[3])
    R3Cord.append((a[2], a[3]))
    
#print(R3Cord)
'''
    
#Distance variables are initialzed at the top of the code
#For each player/ball, it goes through the coordinate list and accesses the two consecutive points
#Then the distance is calculated and added to the total distance variable for that player/ball
    
#Calculates total distance traveled by ball
'''
for x in range (0, len(ballCord) - 1): #Goes through all the indices of BallCord List
    X1 = ballCord[x][0] 
    Y1 = ballCord[x][1]
    X2 = ballCord[x+1][0] #initializes the X2 variable as the x coordinate of the next index of the BallCord List
    Y2 = ballCord[x+1][1] #initializes the Y2 variable as the y coordinate of the next index of the BallCord List
    BallDistance = BallDistance + ( math.hypot(X2 - X1, Y2 - Y1)) #calculates the distance the ball traveled using pythagorean theorem
#print("Ball Distance: " + str(BallDistance))

#Calculates the distance traveled by Player1

for x in range (0, len(P1Cord) - 1):
    X1 = P1Cord[x][0]
    Y1 = P1Cord[x][1]
    X2 = P1Cord[x+1][0]
    Y2 = P1Cord[x+1][1]
    Player1Distance = Player1Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 1 Distance: " + str(Player1Distance))

#Calculates the distance traveled by Player2

for x in range (0, len(P2Cord) - 1):
    X1 = P2Cord[x][0]
    Y1 = P2Cord[x][1]
    X2 = P2Cord[x+1][0]
    Y2 = P2Cord[x+1][1]
    Player2Distance = Player2Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 2 Distance: " + str(Player2Distance))

#Calculates the distance traveled by Player3

for x in range (0, len(P3Cord) - 1):
    X1 = P3Cord[x][0]
    Y1 = P3Cord[x][1]
    X2 = P3Cord[x+1][0]
    Y2 = P3Cord[x+1][1]
    Player3Distance = Player3Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 3 Distance: " + str(Player3Distance))

#Calculates the distance traveled by Player4

for x in range (0, len(P4Cord) - 1):
    X1 = P4Cord[x][0]
    Y1 = P4Cord[x][1]
    X2 = P4Cord[x+1][0]
    Y2 = P4Cord[x+1][1]
    Player4Distance = Player4Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 4 Distance: " + str(Player4Distance))


#Calculates the distance traveled by Player5

for x in range (0, len(P5Cord) - 1):
    X1 = P5Cord[x][0]
    Y1 = P5Cord[x][1]
    X2 = P5Cord[x+1][0]
    Y2 = P5Cord[x+1][1]
    Player5Distance = Player5Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 5 Distance: " + str(Player5Distance))


#Calculates the distance traveled by Player6

for x in range (0, len(P6Cord) - 1):
    X1 = P6Cord[x][0]
    Y1 = P6Cord[x][1]
    X2 = P6Cord[x+1][0]
    Y2 = P6Cord[x+1][1]
    Player6Distance = Player6Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 6 Distance: " + str(Player6Distance))


#Calculates the distance traveled by Player7

for x in range (0, len(P7Cord) - 1):
    X1 = P7Cord[x][0]
    Y1 = P7Cord[x][1]
    X2 = P7Cord[x+1][0]
    Y2 = P7Cord[x+1][1]
    Player7Distance = Player7Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 7 Distance: " + str(Player7Distance))


#Calculates the distance traveled by Player8

for x in range (0, len(P8Cord) - 1):
    X1 = P8Cord[x][0]
    Y1 = P8Cord[x][1]
    X2 = P8Cord[x+1][0]
    Y2 = P8Cord[x+1][1]
    Player8Distance = Player8Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 8 Distance: " + str(Player8Distance))


#Calculates the distance traveled by Player9

for x in range (0, len(P9Cord) - 1):
    X1 = P9Cord[x][0]
    Y1 = P9Cord[x][1]
    X2 = P9Cord[x+1][0]
    Y2 = P9Cord[x+1][1]
    Player9Distance = Player9Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 9 Distance: " + str(Player9Distance))


#Calculates the distance traveled by Player10

for x in range (0, len(P10Cord) - 1):
    X1 = P10Cord[x][0]
    Y1 = P10Cord[x][1]
    X2 = P10Cord[x+1][0]
    Y2 = P10Cord[x+1][1]
    Player10Distance = Player10Distance + ( math.hypot(X2 - X1, Y2 - Y1))
#print("Player 10 Distance: " + str(Player10Distance))

#print("Team 1 Total Distance: " + str(Player1Distance + Player2Distance + Player3Distance + Player4Distance + Player5Distance))
#print("Team 2 Total Distance: " + str(Player6Distance + Player7Distance + Player8Distance + Player9Distance + Player10Distance))
''' 
#positional analysis
roster_all1 = []

for x in roster_all:
    if x not in roster_all1:
        roster_all1.append(x)

for x in range(0, len(set(roster_all)) - 1):
    for y in dic[roster_all[x]]:
        if float(y[1]) > 25 and float(y[0]) > 47: #checks to see if x coordinate is greater than 47 so that its offense and that y is greater than 25
            timeOnLeft = timeOnLeft + 1 #if the condition above is true, it adds one to timeOnLeft variable
        elif float(y[1]) < 25 and float(y[0]) > 47: #same as above except it checks to see if y is less than 25
            timeOnRight = timeOnRight + 1 #adds 1 to timeOnRight if condition is true
    percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100 #finds percentage that player is on the left side
    percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100 #finds percentage that player is on the right side
#    print ("Player " + str(roster_all1[x]) + " % time on Left: " + str(percentTimeLeft)) #prints the percentage    
#    print ("Player " + str(roster_all1[x]) + " % time on Right: " + str(percentTimeRight))
    #print ("")
    
#print (dic['601140'])
  
'''
for x in P1Cord:  #iterates through P1Cord
    if x[1] > 25 and x[0] > 47: #checks to see if x coordinate is greater than 47 so that its offense and that y is greater than 25
        timeOnLeft = timeOnLeft + 1 #if the condition above is true, it adds one to timeOnLeft variable
    elif x[1] < 25 and x[0] > 47: #same as above except it checks to see if y is less than 25
        timeOnRight = timeOnRight + 1 #adds 1 to timeOnRight if condition is true
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100 #finds percentage that player is on the left side
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100 #finds percentage that player is on the right side
print ("Player 1 % time on Left: " + str(percentTimeLeft)) #prints the percentage
print ("Player 1 % time on Right: " + str(percentTimeRight))
print ("")

for x in P2Cord:
    if x[1] > 25 and x[0] > 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] > 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 2 % time on Left: " + str(percentTimeLeft))
print ("Player 2 % time on Right: " + str(percentTimeRight))
print ("")


for x in P3Cord:
    if x[1] > 25 and x[0] > 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] > 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 3 % time on Left: " + str(percentTimeLeft))
print ("Player 3 % time on Right: " + str(percentTimeRight))
print ("")


for x in P4Cord:
    if x[1] > 25 and x[0] > 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] > 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 4 % time on Left: " + str(percentTimeLeft))
print ("Player 4 % time on Right: " + str(percentTimeRight))
print ("")

for x in P5Cord:
    if x[1] > 25 and x[0] > 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] > 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 5 % time on Left: " + str(percentTimeLeft))
print ("Player 5 % time on Right: " + str(percentTimeRight))
print ("")

for x in P6Cord:
    if x[1] > 25 and x[0] < 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] < 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 6 % time on Left: " + str(percentTimeLeft))
print ("Player 6 % time on Right: " + str(percentTimeRight))
print ("")

for x in P7Cord:
    if x[1] > 25 and x[0] < 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] < 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 7 % time on Left: " + str(percentTimeLeft))
print ("Player 7 % time on Right: " + str(percentTimeRight))
print ("")

for x in P8Cord:
    if x[1] > 25 and x[0] < 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] < 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 8 % time on Left: " + str(percentTimeLeft))
print ("Player 8 % time on Right: " + str(percentTimeRight))
print ("")

for x in P9Cord:
    if x[1] > 25 and x[0] < 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] < 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 9 % time on Left: " + str(percentTimeLeft))
print ("Player 9 % time on Right: " + str(percentTimeRight))
print ("")

for x in P10Cord:
    if x[1] > 25 and x[0] < 47:
        timeOnLeft = timeOnLeft + 1
    elif x[1] < 25 and x[0] < 47:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100  
        
print ("Player 10 % time on Left: " + str(percentTimeLeft))
print ("Player 10 % time on Right: " + str(percentTimeRight))
print ("")
'''
'''
for x in dic:
    print(x.itervalues())

for x in dic:
    if x[1] > 25:
        timeOnLeft = timeOnLeft + 1
    else:
        timeOnRight = timeOnRight + 1
percentTimeLeft = ((timeOnLeft)/(timeOnLeft + timeOnRight)) * 100       
percentTimeRight = ((timeOnRight)/(timeOnLeft + timeOnRight)) * 100 
'''

distanceList = []
count = 0

    
    
    


#Distance Graph



#PLOT
fig = plt.figure() #initializes the figure

ax = plt.axes(xlim = (0,120), ylim = (0,50)) #defines limits for graph of players, ball, and refs 

#Goals
leftGoal = plt.Circle((5,25), radius = 0.75, fc = 'w', ec = 'orange', lw = 3) #left goal
rightGoal = plt.Circle((89,25), radius = 0.75, fc = 'w', ec = 'orange', lw = 3) #right goal

plt.gca().add_patch(leftGoal)
plt.gca().add_patch(rightGoal)

#Line to Backboards
leftLine = plt.plot([4.1,4.15], [25,25], color = 'k', lw = 4)
rightLine = plt.plot([89.85,89.9], [25,25], color = 'k', lw = 4)


#Backboards
leftPost = plt.plot([4,4], [22,28], color = 'k', lw = 2)  #left backboard
rightPost = plt.plot([90,90],[22,28], color = 'k', lw = 2) #right backboard

#Court Lines
halfCourt = plt.plot([47,47], [0,50], color = 'k', lw = 2) #line for halfcourt 
leftSide = plt.plot([0,0], [0,50], color = 'k', lw = 4) #left sideline
rightSide = plt.plot([94,94], [0,50], color = 'k', lw = 4) #right sideline
topSide = plt.plot([0,94], [50,50], color = 'k', lw = 4) #top sideline
bottomSide = plt.plot([0,94], [0,0], color = 'k', lw = 4) #bottom sideline


#Rectangles
#Left 
bottomLeft = plt.plot([0,19], [19,19], color = 'k', lw = 2) 
topLeft = plt.plot([0,19], [31,31], color = 'k', lw = 2) 
rightLeft = plt.plot([19,19], [19,31], color = 'k', lw = 2)

#Right
bottomRight = plt.plot([75,94], [19,19], color = 'k', lw = 2)
topRight = plt.plot([75,94], [31,31], color = 'k', lw = 2)
leftRight = plt.plot([75,75], [19,31], color = 'k', lw = 2)


#Hash Lines
#Sidelines
leftBottom = plt.plot([28,28], [0,3], color = 'k', lw = 2)
leftTop = plt.plot([28,28], [47,50], color = 'k', lw = 2)
rightBottom = plt.plot([66,66], [0,3], color = 'k', lw = 2)
rightTop = plt.plot([66,66], [47,50], color = 'k', lw = 2)

#Left Rectangle
hash1Bottom = plt.plot([7,8], [18.67,18.67], color = 'k', lw = 9)
hash2Bottom = plt.plot([11.08,11.08], [18.33,18.9], color = 'k', lw = 2)
hash3Bottom = plt.plot([14.25,14.25], [18.33,18.9], color = 'k', lw = 2)
hash4Bottom = plt.plot([17.42,17.42], [18.33,18.9], color = 'k', lw = 2)
hash1Top = plt.plot([7,8], [31.33,31.33], color = 'k', lw = 9)
hash2Top = plt.plot([11.08,11.08], [31.1,31.67], color = 'k', lw = 2)
hash3Top = plt.plot([14.25,14.25], [31.1,31.67], color = 'k', lw = 2)
hash4Top = plt.plot([17.42,17.42], [31.1,31.67], color = 'k', lw = 2)

#Right Rectangle
hash1Bottom = plt.plot([86,87], [18.67,18.67], color = 'k', lw = 9)
hash2Bottom = plt.plot([82.92,82.92], [18.33,18.9], color = 'k', lw = 2)
hash3Bottom = plt.plot([79.75,79.75], [18.33,18.9], color = 'k', lw = 2)
hash4Bottom = plt.plot([76.58,76.58], [18.33,18.9], color = 'k', lw = 2)
hash1Top = plt.plot([86,87], [31.33,31.33], color = 'k', lw = 9)
hash2Top = plt.plot([82.92,82.92], [31.1,31.67], color = 'k', lw = 2)
hash3Top = plt.plot([79.75,79.75], [31.1,31.67], color = 'k', lw = 2)
hash4Top = plt.plot([76.58,76.58], [31.1,31.67], color = 'k', lw = 2)

#Three-Point Lines
#Left
bottomLine = plt.plot([0,5], [4.25,4.25], color = 'k', lw = 2)
topLine = plt.plot([0,5], [45.75,45.75], color = 'k', lw = 2)
leftArc = patches.Arc((5, 25), 41.5, 41.5, angle = 0.0, theta1 = 270.0, theta2 = 90.0,  linewidth = 2, fill=False, zorder=2)

ax.add_patch(leftArc)

#Right 
bottomLine = plt.plot([89,94], [4.25,4.25], color = 'k', lw = 2)
topLine = plt.plot([89,94], [45.75,45.75], color = 'k', lw = 2)
rightArc = patches.Arc((89, 25), 41.5, 41.5, angle = 0.0, theta1 = 90.0, theta2 = 270.0,  linewidth = 2, fill=False, zorder=2)

ax.add_patch(rightArc)

#Circles
#Center
centerCircle = plt.Circle((47,25), radius = 6, fc = 'w', lw = 2) 
plt.gca().add_patch(centerCircle)
#Left
for p in [
    patches.Wedge((19, 25), 6, 270, 90, fill = False, edgecolor = None, lw = 2), 

#Right  
    patches.Wedge((75, 25), 6, 90, 270, fill = False, edgecolor = None, lw = 2)

]:
    ax.add_patch(p)
fig.savefig('wedge.png', dpi=90, bbox_inches='tight')


#Three-Point Lines
#Left

#Right
line, = plt.plot([],[], color = 'darkorange', marker = 'o', markersize = 18)
line2,= plt.plot([],[], color = 'lightblue', marker = 'o', markersize = 24)
line3, = plt.plot([],[], color = 'lightblue', marker = 'p', markersize = 24)
line4, = plt.plot([],[], color = 'lightblue', marker = '^', markersize = 24)
line5, = plt.plot([],[], color = 'lightblue', marker = 's', markersize = 24)
line6, = plt.plot([],[], color = 'lightblue', marker = 'd', markersize = 24)
line7, = plt.plot([],[], color = 'darkred', marker = 'o', markersize = 24)
line8, = plt.plot([],[], color = 'darkred', marker = 'p', markersize = 24)
line9, = plt.plot([],[], color = 'darkred', marker = '^', markersize = 24)
line10, = plt.plot([],[], color = 'darkred', marker = 's', markersize = 24)
line11, = plt.plot([],[], color = 'darkred', marker = 'd', markersize = 24)
line12, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)
line13, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)
line14, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)

#LEGEND
gHP1,= plt.plot([96],[41], color = 'lightblue', marker = 'o', markersize = 14)
gHP2, = plt.plot([96],[38], color = 'lightblue', marker = 'p', markersize = 14)
gHP3, = plt.plot([96],[35], color = 'lightblue', marker = '^', markersize = 14)
gHP4, = plt.plot([96],[32], color = 'lightblue', marker = 's', markersize = 14)
gHP5, = plt.plot([96],[28], color = 'lightblue', marker = 'd', markersize = 14)
gAP1, = plt.plot([96],[19], color = 'darkred', marker = 'o', markersize = 14)
gAP2, = plt.plot([96],[16], color = 'darkred', marker = 'p', markersize = 14)
gAP3, = plt.plot([96],[13], color = 'darkred', marker = '^', markersize = 14)
gAP4, = plt.plot([96],[10], color = 'darkred', marker = 's', markersize = 14)
gAP5, = plt.plot([96],[7], color = 'darkred', marker = 'd', markersize = 14)

#renames player, ball, and ref location lists into shorter variables 
#initializes the game clock and gives it a location on the animation
#the text is the thing changing so desired location is specified
gc = plt.text(2,2, "Game clock = ", fontsize = 20)


#renames player, ball, and ref location lists into shorter variables 
aHP1 = plt.text(98,40, "Home player 1 = ")
aHP2 = plt.text(98,37, "Home player 2 = ")
aHP3 = plt.text(98,34, "Home player 3 = ")
aHP4 = plt.text(98,31, "Home player 4 = ")
aHP5 = plt.text(98,28, "Home player 5 = ")

aAP1 = plt.text(98,18, "Away player 1 = ")
aAP2 = plt.text(98,15, "Away player 2 = ")
aAP3 = plt.text(98,12, "Away player 3 = ")
aAP4 = plt.text(98,9, "Away player 4 = ")
aAP5 = plt.text(98,6, "Away player 5 = ")


#renames player, ball, and ref location lists into shorter variables 
Lball = ballCord
Lp1 = P1Cord
Lp2 = P2Cord
Lp3 = P3Cord
Lp4 = P4Cord
Lp5 = P5Cord
Lp6 = P6Cord
Lp7 = P7Cord
Lp8 = P8Cord
Lp9 = P9Cord
Lp10 = P10Cord
'''Lr1 = R1Cord
Lr2= R2Cord
Lr3 = R3Cord
'''



    
#for each player (a-n) x (x1) and y (y1) locations are paired with each person. At the end the x and y coordinates are yeilded. The zip() function creates a tupple out of, in this case, 14 seperate lists.
#For example the input could look something like a = [1, 2, 3] and b = [4, 5, 6]. The zip() function would combine them to look like [(1,4), (2, 5), (3, 6)]

def point_data():
   for a, b, c, d, e, f, g, h, i, j, k in zip(Lball, Lp1, Lp2, Lp3, Lp4, Lp5, Lp6, Lp7, Lp8, Lp9, Lp10):
      x1= a[0]
      y1= a[1]
      x2= b[0]
      y2= b[1]
      x3= c[0]
      y3= c[1]
      x4= d[0]
      y4= d[1]
      x5= e[0]
      y5= e[1]
      x6= f[0]
      y6= f[1]
      x7= g[0]
      y7= g[1]
      x8= h[0]
      y8= h[1]
      x9= i[0]
      y9= i[1]
      x10= j[0]
      y10= j[1]
      x11= k[0]
      y11= k[1] 
      yield x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11
        
  

def animate(point_data): 
    x1, y1 = point_data[0], point_data[1] 
    x2, y2, x3, y3 = point_data[2], point_data[3], point_data[4], point_data[5]
    x4, y4, x5, y5 = point_data[6], point_data[7], point_data[8], point_data[9]
    x6, y6, x7, y7 = point_data[10], point_data[11], point_data[12], point_data[13]
    x8, y8, x9, y9 = point_data[14], point_data[15], point_data[16], point_data[17]
    x10, y10, x11, y11 = point_data[18], point_data[19], point_data[20], point_data[21]
    
    


    line.set_data(x1, y1) 
    line2.set_data(x2, y2)
    line3.set_data(x3, y3) 
    line4.set_data(x4, y4)
    line5.set_data(x5, y5)
    line6.set_data(x6, y6)
    line7.set_data(x7, y7)
    line8.set_data(x8, y8) 
    line9.set_data(x9, y9)
    line10.set_data(x10, y10)
    line11.set_data(x11, y11)
   
def clock_data():
    for a in clock: #use clock_new to match the user input
        yield a

def t_animate(clock_data): #animates the game clock to match the real time
    a = clock_data
    gc.set_text("Game clock = " + a) #will look like 'Game clock = 1200.00' with the number changing as real time changes
    
    
def HP1D():
    for b in HP1:
        yield b
        

def H1_animate(HP1D):
    b = HP1D
    aHP1.set_text("Home player 1 = " + b)
    
def HP2D():
    for a in HP2:
        yield a

def H2_animate(HP2D):
    a = HP2D
    aHP2.set_text("Home player 2 = " + a)
    
def HP3D():
    for a in HP3:
        yield a

def H3_animate(HP3D):
    a = HP3D
    aHP3.set_text("Home player 3 = " + a)
    
def HP4D():
    for a in HP4:
        yield a

def H4_animate(HP4D):
    a = HP4D
    aHP4.set_text("Home player 4 = " + a)
    
def HP5D():
    for a in HP5:
        yield a

def H5_animate(HP5D):
    a = HP5D
    aHP5.set_text("Home player 5 = " + a)
    
    
def AP1D():
    for a in AP1:
        yield a

def A1_animate(AP1D):
    a = AP1D
    aAP1.set_text("Away player 1 = " + a)
    
def AP2D():
    for a in AP2:
        yield a

def A2_animate(AP2D):
    a = AP2D
    aAP2.set_text("Away player 2 = " + a)
    
def AP3D():
    for a in AP3:
        yield a

def A3_animate(AP3D):
    a = AP3D
    aAP3.set_text("Away player 3 = " + a)
    
def AP4D():
    for a in AP4:
        yield a

def A4_animate(AP4D):
    a = AP4D
    aAP4.set_text("Away player 4 = " + a)
    
def AP5D():
    for a in AP5:
        yield a

def A5_animate(AP5D):
    a = AP5D
    aAP5.set_text("Away player 5 = " + a)


    
#animates the player, ball, and ref locations in the XML file. 
#The interval depicts the amount of time before a new location is displayed. For example if interval = 500 the markers would move more slowly around the graph 
anim = animation.FuncAnimation(fig, animate, point_data, interval = 40, repeat = True)


#animates the game clock to show real time
#The interval matches the resolution of the SportVU system
anim1 = animation.FuncAnimation(fig, t_animate, clock_data, interval = 40, repeat = True) 

anim2 = animation.FuncAnimation(fig, H1_animate, HP1D, interval = 40, repeat = True)
anim3 = animation.FuncAnimation(fig, H2_animate, HP2D, interval = 40, repeat = True)
anim4 = animation.FuncAnimation(fig, H3_animate, HP3D, interval = 40, repeat = True)
anim5 = animation.FuncAnimation(fig, H4_animate, HP4D, interval = 40, repeat = True)
anim6 = animation.FuncAnimation(fig, H5_animate, HP5D, interval = 40, repeat = True)

anim7 = animation.FuncAnimation(fig, A1_animate, AP1D, interval = 40, repeat = True)
anim8 = animation.FuncAnimation(fig, A2_animate, AP2D, interval = 40, repeat = True)
anim9 = animation.FuncAnimation(fig, A3_animate, AP3D, interval = 40, repeat = True)
anim10 = animation.FuncAnimation(fig, A4_animate, AP4D, interval = 40, repeat = True)
anim11 = animation.FuncAnimation(fig, A5_animate, AP5D, interval = 40, repeat = True)

plt.show() #animates everything