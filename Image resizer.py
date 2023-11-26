#Library
import tkinter                  #UI library
from tkinter import filedialog  
import cv2                      #For resizing image
from pathlib import Path        #Path library


#Varible
#List all the format that opencv support
supportedFormat = ["*.bmp", "*.dib",
                   "*.jpeg", "*.jpg", "*.jpe",
                   ".jp2",
                   "*.png",
                   "*.webp",
                   "*.avif",
                   "*.pbm", "*.pgm", "*.ppm", "*.pxm", "*.pnm",
                   "*.pfm",
                   "*.sr", "*.ras",
                   "*.tiff", "*.tif",
                   "*.exr",
                   "*.hdr", "*.pic"]
#Default input/output path
inputFolder = Path(__file__).parent
outputFolder = Path(__file__).parent


#UI functions
def selectInputFolder():
    global inputFolder
    inputFolder = Path(filedialog.askdirectory(initialdir=Path(__file__).parent))
    inputFolderName.config(text="Input folder: " + str(inputFolder))
    imageCount = 0
    for extension in supportedFormat:
        imageCount += len(list(inputFolder.glob(extension)))
    totalImage.config(text="Total image: " + str(imageCount))
    
def selectOuputFolder():
    global outputFolder
    outputFolder = Path(filedialog.askdirectory(initialdir=Path(__file__).parent))
    outputFolderName.config(text="Output folder: " + str(outputFolder))

def imageConversion():
    if inputFolder != None:
        images = []
        for extenstion in supportedFormat:
            images.extend(inputFolder.glob(extenstion))
        for image in images:
            outputName = str(Path.joinpath(outputFolder, Path(image).name + ".jpg"))
            image = cv2.imread(str(image))
            image = cv2.resize(image, (28,28))
            cv2.imwrite(outputName, image)


#UI
window = tkinter.Tk()
window.title("Image resizer")
window.geometry("350x150")

inputFolderButton = tkinter.Button(window,
                                   text="Select input folder",
                                   width=20,
                                   command=selectInputFolder)
outputFolderButton = tkinter.Button(window,
                                    text="Select output folder",
                                    width=20,
                                    command=selectOuputFolder)
startCoversion = tkinter.Button(window,
                                text="Start conversion",
                                width=20,
                                command=imageConversion)

inputFolderName = tkinter.Label(window,
                                text="Input folder: " + str(inputFolder),
                                width=100)
totalImage = tkinter.Label(window,
                           text="Total image: ~",
                           width=100)
outputFolderName = tkinter.Label(window,
                                 text="Output folder: " + str(outputFolder),
                                 width=100)

inputFolderButton.pack()
outputFolderButton.pack()
startCoversion.pack()
inputFolderName.pack()
totalImage.pack()
outputFolderName.pack()

window.mainloop()