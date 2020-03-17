#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# BDunbar, 2020-March-15, started adding code for the TODO's in Starter Code
# BDunbar, 2020-March-16, debugged code using suggestions from Douglas Klos
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:

    """
    # TODOne Add Code to the CD class
    # Constructor
    def __init__(self, cd_id, cd_title, cd_artist):
        # Attributes
        self.__cdID = cd_id
        self.__cdTitle = cd_title
        self.__cdArtist = cd_artist
        
    # Properties
    @property
    def cdID(self):
        return self.__cdID
    @cdID.setter
    def cdID(self, value):
        self.__cdID = int(value)
            
    @property
    def cdTitle(self):
        return self.__cdTitle
    @cdTitle.setter
    def cdTitle(self, value):
        self.__cdTitle = value
    
    @property
    def cdArtist(self):
        return self.__cdArtist
    @cdArtist.setter
    def cdArtist(self, value):
        self.__cdArtist = value

# -- PROCESSING -- #
class DataProcessor:
    """Processes data to and from file:

    properties:

    methods:
        add_cd(cd_id, cd_title, cd_artist, table): -> table (a list of CD Objects with appended new cd)
        remove_cd(table, cdNum): -> table (a list of CD Objects with chosen cd removed)
    """
    @staticmethod
    def add_cd(cd_id, cd_title, cd_artist, table):
        """Method to add cd entries to the inventory

        Args:
            cd_id (string): ID for the cd
            cd_title (string): Title of the new CD
            cd_artist (string): Artist of the new CD
            table (list of CD Objects): a list of CD Objects (2D structure) for the cd inventory

        Returns:
            table (list of objs): a list of CD Objects (2D structure) for the cd inventory, after data has been added
        """
        new_cd = CD(cd_id, cd_title, cd_artist)
        table.append(new_cd)
        return table
    
    @staticmethod
    def remove_cd(table, cdNum):
        """Method to remove cd entries from the inventory

        Args:
            table (list of objects): a list of CD Objects (2D structure) for the cd inventory
            cdNum: the ID of the cd to be removed

        Returns:
            table (list of objs): a list of objects (2D structure) for the cd inventory, after data has been removed
        """

        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row.cdID == cdNum:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return table
    
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODOne Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, table):
        """Method to manage data ingestion from file to a list of dictionaries
        
        Args:
            file_name: name of file that the data is saved to
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
            
        Returns:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.
        """
        try:
            with open (file_name, 'rb') as objFile:
                table = pickle.load(objFile)
                return table
        except FileNotFoundError:
            print("The file {} could not be loaded, because it could not be found.\n".format(file_name))
            return table
        
    # TODOne Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, table):
        """Method to write data to the CD Inventory file, saving the data to the file
        
        Args:
            file_name: name of file that the data is saved to
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
            
        Returns:
            None.
        """
        with open(file_name, 'wb') as objFile:
            pickle.dump(table, objFile)

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODOne add docstring
    """Handles Input / Output
    
    properties:
        
    methods:
        print_menu(): -> None
        menu_choice(): -> None
        show_inventory(table): -> None
        get_cd_info(): -> (item_id, item_title, item_artist)
    
    """
    # TODOne add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
        
    # TODOne add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODOne add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objs): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by: {})'.format(row.cdID, row.cdTitle, row.cdArtist))
        print('======================================')
        
    # TODOne add code to get CD data from user
    @staticmethod
    def get_cd_info():
        """Gets information for a new cd entry
         
        Args:
            None.
            
        Returns:
            item_id (string): ID for the cd
            item_title (string): Title of the new CD
            item_artist (string): Artist of the new CD
        """
        item_id = input('Enter ID: ').strip()
        while True:
            try:
                int(item_id)
                break
            except ValueError:
                item_id = input('\nOops! That is not a number. Please enter a numeric ID: ').strip()
            
        item_title = input('What is the CD\'s title? ').strip()
        item_artist = input('What is the Artist\'s name? ').strip()
        return item_id, item_title, item_artist


# -- Main Body of Script -- #
# TODOne Add Code to the main body
    # Load data from file into a list of CD objects on script start
    # Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
    
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)

# start main loop
while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...\n')
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user add data to the inventory
    elif strChoice == 'a':
        # ask user for new ID, CD Title and Artist
        lstOfCDObjects = DataProcessor.add_cd(*IO.get_cd_info(), lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top
        
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user delete data from inventory
    elif strChoice == 'd':
        # display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # ask user which ID to remove
        intIDDel = input('Which ID would you like to delete? ').strip()
        while True:
            try:
                int(intIDDel)
                break
            except ValueError:
                intIDDel = input('\nOops! That is not a number. Please enter a numeric ID: ').strip()
                
        # search thru table and delete CD
        lstOfCDObjects = DataProcessor.remove_cd(lstOfCDObjects, intIDDel)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top
    # let user save inventory to file
    elif strChoice == 's':
        # display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # process choice
        if strYesNo == 'y':
            # save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top
    else:
        print('General Error')

