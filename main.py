import random

class Dog:

    def __init__(self, name, dna=None,mother=None, father=None, color_coat=None, color_eyes=None, coat_type=None):
        self.name = name
        self.color_coat = color_coat
        self.color_eyes = color_eyes
        self.coat_type = coat_type
        self.mother = mother
        self.father = father
        self.siblings = []
        self.offspring = []
        self.dna = dna
        self.mutated = False


        if self.dna is None:
            self.color_coat = "unknown"
            self.color_eyes = "unknown"
            self.coat_type = "unknown"
            self.sex = "unknown"
            # If no DNA is specified, randomly generate it
            self.dna = self.generate_dna()
        else:
            self.color_coat = self.dna_to_color_coat(self.dna[:3])
            self.color_eyes = self.dna_to_color_eyes(self.dna[3:6])
            self.coat_type = self.dna_to_coat_type(self.dna[6:9])
            self.sex = self.dna_to_sex(self.dna[9:11])

        self.color_coat = self.dna_to_color_coat(self.dna[:3])
        self.color_eyes = self.dna_to_color_eyes(self.dna[3:6])
        self.coat_type = self.dna_to_coat_type(self.dna[6:9])
        self.sex = self.dna_to_sex(self.dna[9:11])

    def __str__(self):
        if self.name == None:
            self.name = "GIVE THIS DOG A NAME"
        return self.name

    def generate_dna(self):

        if self.mother is not None and self.father is not None:
            # Determine the DNA sequence for the coat color based on the parents' DNA
            mother_coat_dna = self.mother.dna[:3]
            father_coat_dna = self.father.dna[:3]
            coat_dna = ""
            for i in range(3):
                if random.random() < 0.5:
                    coat_dna += mother_coat_dna[i]
                else:
                    coat_dna += father_coat_dna[i]

            # Determine the DNA sequence for the eye color based on the parents' DNA
            mother_eyes_dna = self.mother.dna[3:6]
            father_eyes_dna = self.father.dna[3:6]
            eyes_dna = ""
            for i in range(3):
                if random.random() < 0.5:
                    eyes_dna += mother_eyes_dna[i]
                else:
                    eyes_dna += father_eyes_dna[i]

            # Determine the DNA sequence for the coat type based on the parents' DNA
            mother_coat_type_dna = self.mother.dna[6:]
            father_coat_type_dna = self.father.dna[6:]
            coat_type_dna = ""
            for i in range(3):
                if random.random() < 0.5:
                    coat_type_dna += mother_coat_type_dna[i]
                else:
                    coat_type_dna += father_coat_type_dna[i]

            mother_sex_dna = self.mother.dna[9:]
            father_sex_dna = self.father.dna[9:]
            sex_dna = ""
            for i in range(2):
                if random.random() < 0.5:
                    sex_dna += mother_sex_dna[i]
                else:
                    sex_dna += father_sex_dna[i]

            return coat_dna + eyes_dna + coat_type_dna + sex_dna
        else:
            # If no mother or father is specified, randomly generate the DNA
            if random.random() < 0.2:
                self.dna = "".join(random.choices(["B", "b", "Y"], k=9))
                choices = ["Z", "X"]
            else:
                self.dna = "".join(random.choices(["B", "b"], k=9))
                choices = ["Z", "X"]
            self.dna += "".join(random.choices(choices, k=1))
            if "Z" in self.dna:
                choices.remove("Z")
                self.dna += "".join(random.choices(choices, k=1))
            else:
                self.dna += "".join(random.choices(choices, k=1))


        return self.dna

    def dna_to_sex(self,dna):
        sex_mapping ={
            "XX": "Female",
            "XZ": "Male",
            "ZX": "Male",
            "ZZ": "Error",
        }
        return sex_mapping.get(dna, "unknown")


    def dna_to_color_coat(self, dna):
        color_coat_mapping = {
            "BBB": "black",
            "BbB": "black",
            "bBB": "black",
            "BBb": "black",
            "Bbb": "brown",
            "bBb": "brown",
            "bbB": "brown",
            "bbb": "white",
            "YYY": "blue",
            "bYY": "red",
            "YYb": "red",
            "YbY": "red",
            "YYB": "Rare Merle",
            "BYY": "Rare Merle",
            "YBY": "Rare Merle",
            "bbY": "white",
            "bYb": "white",
            "Ybb": "white",
            "YBB": "black",
            "BYB": "black",
            "BBY": "black",
            "BbY": "Merle",
            "bBY": "Merle",
            "BYb": "Merle",
            "bYB": "Merle",
            "YBb": "Merle",
            "YbB": "Merle",

        }
        return color_coat_mapping.get(dna, "unknown")

    def dna_to_color_eyes(self, dna):
        color_eyes_mapping = {
            "BBB": "blue",
            "BbB": "blue",
            "bBB": "blue",
            "BBb": "blue",
            "Bbb": "brown",
            "bBb": "brown",
            "bbB": "brown",
            "bbb": "green",
            "YYY": "golden",
            "bYY": "yellow",
            "YYb": "yellow",
            "YbY": "yellow",
            "YYB": "Dark Green",
            "BYY": "Dark Green",
            "YBY": "Dark Green",
            "bbY": "green",
            "bYb": "green",
            "Ybb": "green",
            "YBB": "blue",
            "BYB": "blue",
            "BBY": "blue",
            "BbY": "light brown",
            "bBY": "light brown",
            "BYb": "light brown",
            "bYB": "light brown",
            "YBb": "light brown",
            "YbB": "dark brown",
        }
        return color_eyes_mapping.get(dna, "unknown")

    def dna_to_coat_type(self, dna):
        coat_type_mapping = {
            "BBB": "Short",
            "BbB": "Short",
            "bBB": "Short",
            "BBb": "Short",
            "Bbb": "Long",
            "bBb": "Long",
            "bbB": "Long",
            "bbb": "Medium",
            "YYY": "Silky",
            "bYY": "Bushy",
            "YYb": "Bushy",
            "YbY": "Bushy",
            "YYB": "Very Long",
            "BYY": "Very long",
            "YBY": "Very Long",
            "bbY": "Medium",
            "bYb": "Medium",
            "Ybb": "Medium",
            "YBB": "Short",
            "BYB": "Short",
            "BBY": "Short",
            "BbY": "Curly",
            "bBY": "Curly",
            "BYb": "Curly",
            "bYB": "Curly",
            "YBb": "Curly",
            "YbB": "Curly",
        }
        return coat_type_mapping.get(dna, "unknown")

    def set_sibling(self, sibling):
        if sibling.name != self.name and sibling.name not in self.siblings:
            self.siblings.append(sibling.name)
        # Check if the sibling has a mother or father
        if sibling.mother:
            # Add the offspring of the sibling's mother as siblings
            for offspring in sibling.mother.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)
        if sibling.father:
            # Add the offspring of the sibling's father as siblings
            for offspring in sibling.father.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)
        # Check if the current dog has a mother or father
        if self.mother:
            # Add the offspring of the mother as siblings
            for offspring in self.mother.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)
        if self.father:
            # Add the offspring of the father as siblings
            for offspring in self.father.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)

    def get_sibling(self):
        return self.siblings

    def set_mother(self, mother):
        self.mother = mother

    def get_mother(self):
        return self.mother

    def getcolor_coat(self):
        return self.color_coat

    def set_father(self, father):
        self.father = father

    def get_father(self):
        return self.father

    def set_offspring(self, offspring):
        self.offspring.append(offspring)

    def get_offspring(self):
        return self.offspring

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def breed(self, partner,name=None,repeat=None):
        # Combine the DNA of the two parents to create the DNA of the offspring
        try:
            # Combine the DNA of the two parents to create the DNA of the offspring
            if self.sex == "Male" and partner.sex == "Male" or self.sex == "Female" and partner.sex == "Female":
                raise ValueError("You can't breed two dogs of the same sex together")
        except ValueError as error:
            print(error)
            return
        try:
            if "R" in self.dna or "R" in partner.dna:
                raise ValueError("You can't breed a Retarded & Inbred dog")
        except ValueError as error:
            print(error)
            return
        # Create a new Dog object with the mother and father specified
        offspring = Dog(name, mother=self, father=partner)
        # Add the offspring to the list of offspring for both the mother and father
        self.offspring.append(offspring)
        partner.offspring.append(offspring)

        # Add the previous offspring of both parents as siblings to the new dog,
        # excluding the new dog itself
        siblings = []
        if partner.mother:
            siblings += partner.mother.offspring
        if partner.father:
            siblings += partner.father.offspring
        if self.mother:
            # Add the offspring of the mother as siblings
            for offspring in self.mother.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)
        if self.father:
            # Add the offspring of the father as siblings
            for offspring in self.father.offspring:
                if offspring.name != self.name and offspring.name not in self.siblings:
                    self.siblings.append(offspring.name)
        for sibling in siblings:
            if sibling != offspring:
                offspring.set_sibling(sibling)

        if random.random() < 0.1:
            offspring.mutate()

        if random.random() < 0.3:
            offspring.inbreeding()

        # Return the offspring
        return offspring

    def mutate(self):
        """Introduce a mutation in the DNA sequence of the dog with a very low probability."""
        # Check if the mutate method has already been called
        if self.mutated == True:
            print("The dog has already mutated. The mutate method can only be called once.")
            return

        dna_sequence = list(self.dna)
        i = random.randint(0, len(dna_sequence) - 3)
        dna_sequence[i] = self.random_dna_letter()
        self.dna = "".join(dna_sequence)
        self.color_coat = self.dna_to_color_coat(self.dna[:3])
        self.color_eyes = self.dna_to_color_eyes(self.dna[3:6])
        self.coat_type = self.dna_to_coat_type(self.dna[6:9])
        print(f"A random mutation happened during {self.name} breeding")
        print(dna_sequence[i],"at",i)
        self.mutated = True

    def random_dna_letter(self):
        """Return a random letter from the DNA alphabet."""
        return random.choice(["B", "b", "Y"])

    def inbreeding(self):

        if self.father in self.mother.siblings or self.father in self.mother.offspring or self.mother in self.father.offspring:
            self.dna += "R"
            print("this dog is inbred and retarded")




def Custom_Dog():

    dna = ""
    # THIS IS FOR THE COAT COLOR DNA SPECIFICATION
    print("CHOOSE BETWEEN THE OPTIONS OF COAT COLORS AVAILABLE")
    print("1 - Black")
    print("2 - Brown")
    print("3 - White")
    print("4 - Merle")
    print("5 - Rare Merle")
    print("6 - Red")
    print("7 - Blue")
    color_coat = str(input("Write the number of the option you desire"))
    while True:
        # Black
        if color_coat == "1":
            color_coat_dna = "".join(random.choices(["BBb", "BbB","bBB","BBB","BBY","BYB","YBB"], k=1))
            break
        # Brown
        if color_coat == "2":
            color_coat_dna = "".join(random.choices(["Bbb", "bBb", "bbB"], k=1))
            break
        # White
        if color_coat == "3":
            color_coat_dna = "".join(random.choices(["bYb", "Ybb", "bbY", "bbb"], k=1))
            break
        # Merle
        if color_coat == "4":
            color_coat_dna = "".join(random.choices(["YBb", "BbY", "bYB", "YbB", "bBY", "BYb"], k=1))
            break
        # Rare Merle
        if color_coat == "5":
            color_coat_dna = "".join(random.choices(["YYB", "YBY", "BYY"], k=1))
            break
        # Red
        if color_coat == "6":
            color_coat_dna = "".join(random.choices(["YYb", "bYY", "YbY"], k=1))
            break
        # Blue
        if color_coat == "7":
            color_coat_dna = "".join(random.choices(["YYY"], k=1))
            break
        else:
            print("Wrong value, please assign a new one")
            color_coat = str(input("Write the number of the option you desire"))

    # THIS IS FOR THE EYE COLOR DNA SPECIFICATION

    print("CHOOSE BETWEEN THE OPTIONS OF EYE COLOR AVAILABLE")
    print("1 - Blue")
    print("2 - Brown")
    print("3 - Green")
    print("4 - light brown")
    print("5 - Dark Green")
    print("6 - Yellow")
    print("7 - Golden")
    eye_color = str(input("Write the number of the option you desire"))
    while True:
        # Blue
        if eye_color == "1":
            eye_color_dna = "".join(random.choices(["BBb", "BbB", "bBB", "BBB", "BBY", "BYB", "YBB"], k=1))
            break
        # Brown
        if eye_color == "2":
            eye_color_dna = "".join(random.choices(["Bbb", "bBb", "bbB"], k=1))
            break
        # White
        if eye_color == "3":
            eye_color_dna = "".join(random.choices(["bYb", "Ybb", "bbY", "bbb"], k=1))
            break
        # Merle
        if eye_color == "4":
            eye_color_dna = "".join(random.choices(["YBb", "BbY", "bYB", "YbB", "bBY", "BYb"], k=1))
            break
        # Rare Merle
        if eye_color == "5":
            eye_color_dna = "".join(random.choices(["YYB", "YBY", "BYY"], k=1))
            break
        # Red
        if color_coat == "6":
            eye_color_dna = "".join(random.choices(["YYb", "bYY", "YbY"], k=1))
            break
        # Blue
        if eye_color == "7":
            eye_color_dna = "".join(random.choices(["YYY"], k=1))
            break
        else:
            print("Wrong value, please assign a new one")
            eye_color = str(input("Write the number of the option you desire"))
    # THIS IS FOR coat type DNA SPECIFICATION

    print("CHOOSE BETWEEN THE OPTIONS OF COAT TYPES AVAILABLE")
    print("1 - Short")
    print("2 - Long")
    print("3 - Medium")
    print("4 - Curly")
    print("5 - Very Long")
    print("6 - Bushy")
    print("7 - Silky")
    type_coat = str(input("Write the number of the option you desire"))
    while True:
        # Black
        if type_coat == "1":
            type_coat_dna = "".join(random.choices(["BBb", "BbB", "bBB", "BBB", "BBY", "BYB", "YBB"], k=1))
            break
        # Brown
        if type_coat == "2":
            type_coat_dna = "".join(random.choices(["Bbb", "bBb", "bbB"], k=1))
            break
        # White
        if type_coat == "3":
            type_coat_dna = "".join(random.choices(["bYb", "Ybb", "bbY", "bbb"], k=1))
            break
        # Merle
        if type_coat == "4":
            type_coat_dna = "".join(random.choices(["YBb", "BbY", "bYB", "YbB", "bBY", "BYb"], k=1))
            break
        # Rare Merle
        if type_coat == "5":
            type_coat_dna = "".join(random.choices(["YYB", "YBY", "BYY"], k=1))
            break
        # Red
        if type_coat == "6":
            type_coat_dna = "".join(random.choices(["YYb", "bYY", "YbY"], k=1))
            break
        # Blue
        if type_coat == "7":
            type_coat_dna = "".join(random.choices(["YYY"], k=1))
            break
        else:
            print("Wrong value, please assign a new one")
            type_coat = str(input("Write the number of the option you desire"))


    # THIS IS FOR coat type DNA SPECIFICATION

    print("CHOOSE BETWEEN THE SEX OPTIONS AVAILABLE")
    print("1 - Male")
    print("2 - Female")

    sex = str(input("Write the number of the option you desire"))
    while True:
        # Black
        if sex == "1":
            sex_dna = "".join(random.choices(["XZ","ZX"], k=1))
            break
        # Brown
        if sex == "2":
            sex_dna = "".join(random.choices(["XX"], k=1))
            break
        else:
            print("Wrong value, please assign a new one")
            sex = str(input("Write the number of the option you desire"))

    dna = color_coat_dna + eye_color_dna + type_coat_dna + sex_dna

    dog_name = str(input("Insert new custom dog name here: "))
    NewDog = Dog(dog_name, dna)
    
    return NewDog

