class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    #ef __str__(self):
        #return(self.__model+" "+self.__registration_number+" "+(str) self.__year))
class Service:
    def __init__(self, car_list):
        self.__car_list=car_list 

    def get_car_list(self):
        return self.__car_list
    def find_cars_by_year(self, year):
        self.year= year
        car_by_year_list=[]
        for i in self.get_car_list():
            if i.get_year()==self.year :
                car_by_year_list.append(i)
        if car_by_year_list==[]:
            return None
        else:
            return car_by_year_list




    def add_cars(self,new_car_list):
        self.new_car_list=new_car_list
        return self.get_car_list().append(self.new_car_list)

    def remove_cars_from_karnataka(self):
        for i in self.get_car_list():
            if i.get_model()[0:2]=="KA":
                self.get_car_list().remove(i)



car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
car_list2=[car2,car3]
s=Service(car_list)

s.add_cars(car_list2)
s.remove_cars_from_karnataka()
print(s.get_car_list()[1].get_year())
