class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    @property
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return (isinstance(other, BMI) and
                self.weight == other.weight and
                self.height == other.height)

# Example usage:
if __name__ == "__main__":
    person1 = BMI(70, 1.75)  # Weight: 70 kg, Height: 1.75 m
    person2 = BMI(65, 1.70)  # Weight: 65 kg, Height: 1.70 m

    print("Person 1 BMI:", person1.BMI_Value)
    print("Person 2 BMI:", person2.BMI_Value)
    print("Are they equal?", person1 == person2)
