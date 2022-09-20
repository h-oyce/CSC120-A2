class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, itemID, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.itemID: int
        self.description: str
        self.processor_type: str
        self.hard_drive_capacity: int
        self.memory: int
        self.operating_system: str
        self.year_made: int
        self.price: float

  ## search how to check to make sure the correct computer is being updated

    def changeOS(self, itemID, updatedOS):
        if updatedOS == str:
            if itemID == self.itemID:
                self.operating_system == updatedOS
                print([self.itemID] + "has been updated to" + [updatedOS])
            else: 
                print("Could not identify computer")

        else:
            print("Updating OS has failed")
