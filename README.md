# pictureTextCrop

This application can be run by installing the python package dependencies using pip and then simply unzipping the source archive, pictureTextCrop.tar.gz into a new directory that you create to contain the application and its files.  The python packages required, available at PyPI.org, include one rather large one, PyQt5.  The complete list of packages required is: PyQt5, pytesseract , and Pillow.

Once unzipped, go into the pictureTextCrop folder, and locate the pictureTextCrop.py source file. To start the application, execute the following on the command line:

$ python3 pictureTextCrop.py


Introduction:

This application is a simple tool which allows you to interactively extract text from image files by dragging from the top-left corner of a crop rectangle to the bottom-right corner. When you release the mouse button the text inside the rectangle is printed to the console and a record of the conversion and its result is made in the SQLite3 database, TextExtraction.db, in the CropLog table. Each record of this table records the date and time of the extraction in its timeStamp field, the full path to the file on your disk of the image file in the filePath field, the coordinates of the crop in the coordinates field, and the text of the crop in the text field. The value of storing all extractions in a database table is simply that you can then search large numbers of images containing particular text using SQL.

The image formats recognized are those recognized by the PyQy5 QImageReader class, which includes those associated with the following file extensions:

    'bmp', 'cur', 'gif', 'icns', 'ico', 'jpeg', 'jpg', 'mng', 'pbm', 'pgm', 'png', 'ppm', 'svg', 'svgz', 'tga', 'tif', 'tiff', 'wbmp', 'webp', 'xbm', 'xpm'

The application main window displays a list on the left which will contain the paths of the image files identified when you select folders to scan.  In the right half of the dialog will be a space which shows the image selected when you click on a file path in the list.  The dialog can be resized to accommodate your needs.

To extract text from an image, select the checkbox located to the left of it and click on the "Select Image Text" button in the button-bar at the top. You can select multiple files and a text selection dialog will be stacked up for each. Press the left mouse button at the top left of a rectangle containing the text you want to extract and then drag to the lower right corner. When you release the button the extracted text is printed to the console and a record of the extraction and its result is made in the SQLite3 database. You can do this as many times as you like for each image. A separate CropLog record will be made for each.

Batch Mode:

If you click on the "Batch Process" button in the tool bar the application will extract all of the text from each of the files in the folder scan list. This process can take some time, my own trials on my ordinary laptop resulting in a pace of more than 5 seconds per image, sometimes 15 or so. With only 50 images, the process could take up to 10 minutes. The resulting extracted text will be placed into the BatchMaster table in the SQLite3 database. The fields written in each record in include the extraction TimeStamp, the FolderPath, the FileName, the Text, and the file metadata in the Info field. Views for reviewing the file metadata and other components saved in convenient formats are planned.


MIME Information Collection:

Coming Soon.

When processing digital evidence you must be careful to preserve the file metadata, especially the time stamps. 
Know how operating systems treat timestamps and permissions when you copy files and how your archiving applications do as well. 


If you would like to support this project, you can contribute here: https://www.buymeacoffee.com/keithmichah

