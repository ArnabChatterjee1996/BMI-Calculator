class Person:

    """
    This class defines the attributes of a person.
    """

    def __init__(self,gender,height,weight):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = None
        self.bmi_category = None
        self.health_risk = None

    def set_bmi(self,bmi):
        self.bmi = bmi
    def set_bmi_category(self,bmi_category):
        self.bmi_category = bmi_category
    def set_health_risk(self,health_risk):
        self.health_risk = health_risk

    def get_details(self):
        return {
            "Gender":self.gender,
            "HeightCm":self.height,
            "WeightKg":self.weight,
            "BMI":self.bmi,
            "BMICategory":self.bmi_category,
            "HealthRisk":self.health_risk
        }

    def __repr__(self):
        return "Height : {} , Weight : {} Gender : {} ".format(self.height,
                                                              self.weight,
                                                              self.gender)

    def repr_with_bmi(self):
        print("Height : {}, Weight : {}, Gender : {}, " \
               "BMI : {}, BMI Category {}, Health Risk {}".format(self.height,
                                                               self.weight,
                                                               self.gender,
                                                               self.bmi,
                                                               self.bmi_category,
                                                               self.health_risk))

class BMI:
    """
    This class calculates the BMI for all the people in the data set.

    methods :

        -> calculate_bmi
        -> calculate_bmi_category
        -> calculate_health_risk
        -> calculate
        -> print_person_list

    """

    def __init__(self):
        self.data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                     {"Gender": "Male", "HeightCm": 161, "WeightKg":
                         85}, {"Gender": "Male", "HeightCm": 180, "WeightKg": 77}, {"Gender": "Female", "HeightCm": 166,
                                                                                    "WeightKg": 62},
                     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
                                                                             "HeightCm": 167, "WeightKg": 82}]
        self.person_object_list = []
        try:
            for item in self.data:
                self.person_object_list.append(Person(item['Gender'],item['HeightCm'],item['WeightKg']))
        except Exception as e:
            print("There's some problem with data . Exception occurred in adding people to "
                  "person_object_list . Exception : {}".format(e))

        self.bmi_map = {
            (0,18.4):('Underweight','Malnutrition'),
            (18.5,24.9):('Normal weight','risk'),
            (25,29.9):('Overweight','Low risk'),
            (30,34.9):('Moderately obese','Enhanced risk'),
            (35,39.9):('Severely obese','High risk'),
            (40,1000):('Very severely obese','Very high risk'),
        }

    def calculate_bmi(self,person):
        """
        This function calculates the BMI of a person

        Return True if the value is calculated correctly
        False if any data is missing or there is some problem with the calculation

        params : Person object [Must be containing height and weight , gender is optional]

        >>> bmi = BMI()
        >>> bmi.calculate_bmi(Person("Male",171,96))
        True
        """
        try:
            height_in_metres = (person.height / 100)
            weight_in_kg = person.weight

            bmi_calculated = round(weight_in_kg / (height_in_metres*height_in_metres),2)
            person.set_bmi(bmi_calculated)
            return True
        except Exception as e:
            print("There's some problem with calculation . Exception occurred in getting BMI for person"
                  " : {} . Exception : {}".format(person,e))
            return False

    def calculate_bmi_category(self, person):
        """
        This function calculates the BMI category of a person

        Return True if the value is calculated correctly
        False if any data is missing or there is some problem with the calculation

        params : Person object [Must be containing height and weight , gender is optional]

        """
        try:
            bmi_person = person.bmi
            if bmi_person is None:
                print("Calculate BMI and then try calculating the BMi category")
                return False
            else:
                for key,value in self.bmi_map.items():
                    if bmi_person >= key[0] and bmi_person < key[1]:
                        person.set_bmi_category(value[0])

                if person.bmi_category is None:
                    print("BMI category data not available for BMI : {}".format(bmi_person))
                    return False

            return True
        except Exception as e:
            print("There's some problem with calculation . Exception occurred in getting BMI Category"
                  " for person : {} . Exception : {}".format(person, e))
            return False

    def calculate_health_risk(self, person):
        """
        This function calculates the Health Risk of a person

        Return True if the value is calculated correctly
        False if any data is missing or there is some problem with the calculation

        params : Person object [Must be containing height and weight , gender is optional]

        """
        try:
            bmi_person = person.bmi
            if bmi_person is None:
                print("Calculate BMI and then try calculating the health risk")
                return False
            else:
                for key, value in self.bmi_map.items():
                    if bmi_person >= key[0] and bmi_person < key[1]:
                        person.set_health_risk(value[1])

                if person.bmi_category is None:
                    print("Health Risk data not available for BMI : {}".format(bmi_person))
                    return False

            return True
        except Exception as e:
            print("There's some problem with calculation . Exception occurred in getting Health Risk"
                  " for person : {} . Exception : {}".format(person, e))
            return False

    def calculate(self):
        for person in self.person_object_list:
            bmi_data_add = self.calculate_bmi(person)
            bmi_category_add = self.calculate_bmi_category(person)
            health_risk_add = self.calculate_health_risk(person)

            if not bmi_data_add:
                print("BMI data addition failed for person : {} . Check logs for more info".format(person))
            if not bmi_category_add:
                print("BMI category addition failed for person : {} . Check logs for more info".format(person))
            if not health_risk_add:
                print("Health Risk addition failed for person : {} . Check logs for more info".format(person))

    def print_person_list(self):
        for person in self.person_object_list:
            person.repr_with_bmi()

if __name__ == "__main__":
    ####################################
    ##### This block is to test the code
    # import doctest
    # doctest.testmod()
    ####################################
    bmi_object = BMI()
    bmi_object.calculate()
    bmi_object.print_person_list()









