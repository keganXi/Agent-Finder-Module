# ScrapCars/scrap_cars_modules/agent_finder/get_agent_module.py

"""
    NOTE:
        - This module (get_agent_module.py) is used for 
          finding the agent that best matches the 
          user's cars valuation.
"""

class FindAgent:
    """
        Functions:
            # store_db_data() 
            # agent_algorithm()
            -----------------------------------------------
            store_db_data():
                - To store the Database field (price_per_kg)
                  into a list.

            agent_algorithm():
                - To get the highest price per kg an agent is 
                  offering through a reversed Insertion algorithm.   
    """
    
    def __init__(self, _db):
        """
            @params
                _db - To pass in a datbase.
        """
        self._db = _db 
        # Initializer for price per kg data.
        self.price_per_kg_store = []

    def store_db_data(self):
        """
            IMPORTANT:
                - The database thats being iterated through
                  calls the foreign key pointed to the 
                  agent registration database and getting the 
                  price per kg from there.
        """
        # Iterates through the database (self._db) 
        # and store's the data in a list object (self.price_per_kg_store).
        for ar_db in self._db:
            # Condition checks if the agent's account is active.
            if ar_db.agent_reg_db.account_active == True and ar_db.agent_reg_db.card_status == False:
                self.price_per_kg_store.append(ar_db.agent_reg_db.price_per_kg)
                print("\n\n\nTest List: {0}\n\n\n".format(str(self.price_per_kg_store))) # Debugging purposes only.

    def agent_algorithm(self):
        """
            @returns
                self.price_per_kg_store - returns the first
                                          index element of the
                                          list which is the highest
                                          price per kg an agent is offering.
                _result - returns a None object if the list (self.price_per_kg)
                         is empty.
        """
        for index in range(1, len(self.price_per_kg_store)):
            # For Debugging purposes only
            # and should be removed before production.
            print("\n\n\nprice per kg list: {0}\n\n\n".format(str(self.price_per_kg_store))) # Debugging purposes only.
            value = self.price_per_kg_store[index]
            i = index - 1
            while i>=0:
                if value > self.price_per_kg_store[i]:
                    self.price_per_kg_store[i+1] = self.price_per_kg_store[i]
                    self.price_per_kg_store[i] = value
                    i = i - 1
                else:
                    break
        # For Debugging purposes only
        # and should be removed before production.
        print("\n\n\nAfter Algorithm is executed: {0}\n\n\n".format(str(self.price_per_kg_store))) # Debugging purposes only.
        if len(self.price_per_kg_store) == 0:
            _result = None
            return _result
        else:
            return self.price_per_kg_store[0]

    
