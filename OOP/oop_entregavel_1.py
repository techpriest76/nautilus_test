#descrive the AUS 
#must contain: kind of vehicle,sensors, dimensions, year of construction, +1 other characteristic
#must have the following methods
#   |- show the AUVs in a table
#   |- show the robots individually
#   |- Rank them from newest to oldest
#   |- +1 method

class vehicle:
    def __init__(self,name,sensor,year,battery,thruster,title):
        self.thruster=thruster
        self.title=title
        self.name=name
        self.sensor=sensor
        self.year=year
        self.battery=battery

    def display(self):
        print('Name:',self.name)
        print('Kind of sensors:',self.sensor)
        print('Year:',self.year)
        print('Battery:',self.battery)
        print('N of thrusters:',self.thruster)
        print(' ')

    def display_table(self):
        print(self.name,'|',self.sensor,'|',self.year,'|',self.battery,'|',self.thruster)
    
class AUVS:
    def __init__(self,many):
        self.many=many

    def table(self):
        print('TABLE sorted by date (newest to oldest)\n')
        print('Name  |                      Sensors                     | Year |       Battery    | N. of thrusters')
        self.many.sort(reverse=True, key=lambda vehicle:vehicle.year)
        for i in self.many:
            i.display_table()
        print(' ')
    
    def list_names(self):
        self.many.sort(reverse=True, key=lambda vehicle:vehicle.year)
        print('models from newest to oldest')
        for i in self.many:
            print(i.name)
        print(' ')

    def papers(self):
        print('Papers: ')
        for i in self.many:
            print(i.title)

################## SETUP ################################

######## VEHICLES CHARACTERISTICS #######################

auv1=vehicle('BrHUE','               MTi-G-AHRS, Bii-7141             ',2020,'LiPo 5,2K mAh 4S','6','Progress and Fabrication of UFRJ Nautilus’ AUV: Lua') 
auv2=vehicle('Lua  ','DVL A50, BAR30, MTi-G-AHRS, 3DM-CX5-10, Bii-7141',2022,'LiPo 10k mAh 4S ','8','Design and Implementation of UFRJ Nautilus’ AUV: BrHUE 2020')

################ LIST OF VEHICLES #######################
auvs=[auv1,auv2]

################## VEHICLE POPULATION DEFINITION ########
table_d=AUVS(auvs)

################# DISPLAY ##############################
 
#displays vehicles on a table sorted by year
print('----------- table of vehicles -------------')
table_d.table()

#displays each vehicle individually
print('----------- each vehicle individually -----')
auv1.display() 
auv2.display()

#displays vehicle names by year
print('----------- vehicles by year ---------------')
table_d.list_names()

#display papper title
print('----- papers in which the AUVs appear ------')
table_d.papers()
