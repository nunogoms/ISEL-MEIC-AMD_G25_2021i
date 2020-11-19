class DatasetInstance:
    def __init__(self, ocular_age, tear_rate, disease_name, lens_type):
        self.ocular_age = ocular_age
        self.tear_rate = tear_rate
        self.disease_name = disease_name
        self.lens_type = lens_type

    def __init__(self,list):
        self.ocular_age = list[0]
        self.tear_rate = list[1]
        self.disease_name = list[2]
        self.lens_type = list[3]
