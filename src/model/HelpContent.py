#   Project:        LinuxLogForensics
#   Author:         George Keith Watson
#   Date Started:   August 11, 2021
#   Copyright:      (c) Copyright 2021 George Keith Watson
#   Module:         view/Help.py
#   Purpose:        Help sub-system dialog.
#   Development:
#       2021-08-11:
#           This is the source module for all help content provided by this application.  It included the quick
#           content sensitive pop-up help content along with management of and access to the general help database.
#

from copy import deepcopy
from enum import Enum


class DropDownMenuNames(Enum):
    BACKUPS = 'Backups'
    INDEXES = "Folder Indexes"
    VIEWS = 'Views'
    TOOLS = 'Tools'
    SCHEDULING = 'Scheduling'
    ACTIVITY_LOGS = 'Activity Logs'
    CONFIGURATION = 'Configuration'
    HELP = "Help"

    def __str__(self):
        return self.value


class HelpText(Enum):
    LoadFile        = (" Load File for Forensic Details ", 'This feature is not implemented yet.  It will:\n\n'
                                          'Load a single file for detailed forensic examination, such as:\n'
                                          '\tIts meta-data,\n'
                                          '\tIts inode data,\n'
                                          '\tMetadata change history if in an ext file system,\n'
                                          '\tPossibly content change history if journaling of\n'
                                          '\t\tcontent has been switched on in an ext4\n'
                                          '\t\tfile system,\n'
                                          '\tExamination of the particular MIME type\'s internal\n'
                                          '\t\tstructure and embedded meta data, ...\n\n'
                                          'Proceed with selection of a file to view its content?\n')

    LoadRecentFile  =   (" Load Recent File ", "This feature is not implemented yet. It will:\n\n"
                                         "Show the list of files loaded for detailed examination during the current "
                                         "application run session and have an option to select from the list of all "
                                         "files ever loaded for such examination by user defined groups, usually "
                                         "grouped by what this application calls a 'Study'\n")

    SaveFileAs = (" Save File As ", "This feature is not implemented yet. It will:\n\n"
                                         "Allow the user to save the currently loaded file set under a group the user "
                                         "selects.  Groups include user defined studies, plain file sets, and "
                                         "arbitrary groupings named by the user.\n")

    ExportFile  = (" Export File As ... ", "This feature is not implemented yet. It will:\n\n"
                                         "Allow the user to export various information products generated by "
                                         "the user\'s work with this application into various formats. "
                                         "Reports, for instance, can be written into HTML, Office Document, or if "
                                         "simply tabular data, spreadsheet, database table, or plain CSV format.  "
                                         "If the content is hierarchical, JSON and XML will be available.  Forensically "
                                         "frozen file packages are also possible, but are available only through another "
                                         "feature of this Application, from the main menu: Archives -> Freeze Folder\n")

    ImportFile  = (" Import File As ... ", "This feature is not implemented yet.  It will:\n\n"
                                           "Import useful database tables from other database engines or from SQLite, "
                                           "this application's native database engine, into this application's "
                                           "database set.  This application includes various features allowing you "
                                           "to view the content of database tables and incorporate their content into "
                                           "your evidence studies.\n\n"
                                           "Import useful spreadsheets and CSV files in the same manner in which "
                                           "database tables are imported.\n\n"
                                           "Import JSON and XML documents into the data sets maintained and used "
                                           "by this application.  These are viewable and usable in a tree view in "
                                           "various features of this Application.\n\n"
                                           "Drag-and-Drop will be the standard method of inclusion of imported "
                                           "content into application data sets and reports.\n")

    SelectAndLockFolder     = (" Select and Lock a Folder ", "This feature is not implemented yet. It will:\n\n"
                                         "Perform an access control lock on any folder you select.\n"
                                         "An access control lock changes the access to the folder and all of its "
                                         "contents down to the bottom of the tree to be read-only for the owner, "
                                         "with no access provided to any other account other than the root account.  "
                                         "This is clearly desirable if you want to preserve and examine the "
                                         "contained files as evidence.\n\n"
                                         "This is done using the chmod function of the operating system, so if there "
                                         "is an issue changing the permissions, such as if some other "
                                         "user than the one currently logged in created and owns files in the folder, "
                                         "then this feature could fail.\n\n"
                                         "If it does, you will have the option to change ownership of the entire folder "
                                         "contents to your account, a feature which uses the super user account of your "
                                         "operating system and therefore requires you to enter your password.\n\n"
                                         "Once you own the entire folder contents, then you can change the access "
                                         "permissions at will.\n")

    FolderCopyToIsolation   =   (" Copy Folder to Isolation ", "This feature is not implemented yet. It will:\n\n"
                                         "Copy a folder completely to the Isolation Folder set aside for this purpose "
                                         "during configuration of the application.  Isolation of a folder is a first "
                                         "step toward preserving it for examination for files with content relevant to "
                                         "whatever issue interests you.  Once the contents of the folder are copied, "
                                         "this feature changes the file access permissions to incluce access only by "
                                         "the onwer and to include only read access.\n\n"
                                         "The application will also record all of the "
                                         "file meta-data when it copies files so that you can see the changes to "
                                         "it that are made when the operating system's standard file copy features are "
                                         "applied to it.  The changes typically made to forensically valuable file"
                                         "meta-data include its time stamps, so it is worth while to compare the "
                                         "two records.\n\n"
                                         "Once the copy is made, you can compare the meta data of each file in the "
                                         "original folder and its copy side by side and decide whether you would like "
                                         "to preserve the original meta data.  If you select this option, the "
                                         "application writes an SQLite database table keyed on the "
                                         "file path and containing as visible fields all of its meta data.  Because "
                                         "it is in a database table, all of the fields can be searched with SQL "
                                         "and with the standard browser for SQLite.\n\n"
                                         "You will be informed of where the table is for future use, and it "
                                         "will be available for content and meta-data search, filter, and reporting "
                                         "functions of this application.\n")

    FolderArchiveAndIndex   = ("Archive and Optionally Index a Folder ",
                                        "Make an archive file from the folder you select using your selection of "
                                         "archive formats.  It also makes a volume index of the folder, meaning "
                                         "it stores each file's descriptive information in a database table using "
                                         "the file and folder path as the key. Included as fields of the file's "
                                         "record are all file meta-data as well as MIME type information.\n\n"
                                         "Some of the "
                                         "meta-data is lost when you make a file archive using any of the currently "
                                         "standard formats, so simple archiving is not sufficient to reconstruct "
                                         "the file as evidence for use in important business decisions or as "
                                         "evidence available for governmental functions.\n\n"
                                         "You can also elect to generate and store your selection of file content "
                                         "hash signatures in each file's table record.  This provides a means of "
                                         "checking to detect changes in the file's content. \n\n"
                                         "The folder archive is written to a dedicated application Archives folder "
                                         "and the volume index table is written to the database the application "
                                         "uses for this purpose.  The table name in  in the database will be the "
                                         "full path of the selected folder with '_' replacing all slashes.  The "
                                         "archive and volume index are then available as a pair in this application's "
                                         "search and filter features, which are the source of "
                                         "evidence files for its report generation features.\n",
                               "Archive with Index")

    FolderIndexAndArchive   = ("Index and Optionally Archive a Folder",
                               "Make a volume index of the folder, meaning generate a database with a table "
                               "that stores each file's descriptive information using the file and folder "
                               "path as the key. Included as fields of each file's "
                               "record are all file meta-data in easily searchable forms "
                               "as well as MIME type information.\n\n"
                               "You also have the option of including your "
                               "selection of hash signatures for each file in its record.  For security and "
                               "for usability as evidence, this is necessary and does not add much to the "
                               "record size.  The hash signatures of each file can be used later for "
                               "verification that the file contents have not changed.\n\n"
                               "Optionally make an archive file from the folder you select to index using "
                               "your selection of archive formats.\n",
                            "Index with Archive")

    VerifyFolderWithIndex   = ("Verify a Folder with its Index",
                              "If you selected the option of generating and saving the hash signatures for the "
                              "files in a folder when you ran the Files->Build Index tool of the main menu, then "
                              "you can verify that the files in the folder indexed haven't changed using this feature. \n\n"
                              "The hash signatures of each file are computed from the current file with the same "
                              "name and at the same path location in the folder.  If there is a difference in any "
                              "of the signatures, then a report is generated listing the files that have changed "
                              "and listing the signatures of the original file and the current file. Only the file "
                              "content is included in the hash computation, not its meta-data or any other system "
                              "information on the file.\n\n"
                              "If the folder to check is on an external USB storage device, then plug it in before "
                              "proceeding.  If its index file is also on an external USB storage device, plug"
                              "it in also.\n\n"
                              "A folder selection dialog will appear next.  Select a folder where you "
                              "had volume indexes generated using the Files->Build Index tool.  A list of archive "
                              "indexes, the SQLite database files with extension '.db', in the folder will "
                              "appear next.  You can then select the index of the folder you would like to "
                              "have verified from it.\n\n"
                              "Would you like to proceed?\n",
                            "Verify Folder")

    def __str__(self):
        return self.value[0]


class HelpContent:

    def __init__(self, name: str, initialContent: dict=None, **keyWordArguments):
        """

        :param initial:             initial help content for an instance of HelpContent.
        :param keyWordArguments:    meta data for this help content.
        """
        if name is None or not isinstance(name, str):
            raise Exception("HelpDialog constructor - invalid name argument:\t" + str(name))
        if initialContent is None:
            initialContent = self.generateDefaultContent()
        self.validDescriptor = True
        if not isinstance(initialContent, dict):
            self.validDescriptor = False
        for key, value in initialContent.items():
            if not isinstance(key, str) or not isinstance(value, str):
                self.validDescriptor = False
                break
        if not self.validDescriptor:
            raise Exception("HelpDialog constructor - invalid descriptor argument:\t" + str(initialContent))
        self.name = name
        self.contentMap = deepcopy(initialContent)      #   thread safe

    def getContentMap(self):
        return self.contentMap

    def removeContent(self, topic):
        if topic is None or not isinstance(topic, str):
            raise Exception("HelpContent.removeContent - invalid topic argument:\t" + str(topic))
        if topic in self.contentMap:
            del(self.contentMap[topic])
            return topic
        return False

    def addContent(self, topic, helpText):
        if topic is None or not isinstance(topic, str):
            raise Exception("HelpContent.removeContent - invalid topic argument:\t" + str(topic))
        if helpText is None or not isinstance(helpText, str):
            raise Exception("HelpContent.removeContent - invalid helpText argument:\t" + str(helpText))
        if topic not in self.contentMap:
            self.contentMap[topic] = helpText
            return topic
        return False

    def addReplace(self, topic, helpText):
        if topic is None or not isinstance(topic, str):
            raise Exception("HelpContent.removeContent - invalid topic argument:\t" + str(topic))
        if helpText is None or not isinstance(helpText, str):
            raise Exception("HelpContent.removeContent - invalid helpText argument:\t" + str(helpText))
        self.contentMap[topic] = helpText

    def __setattr__(self, key, value):
        if key in self.__dict__:
            return False
        self.__dict__[key] = deepcopy(value)

    def list(self):
        print("\nHelpContent:\t" + self.name)
        for topic, helpText in self.contentMap.items():
            print("\t" + topic + ":\t" + helpText)