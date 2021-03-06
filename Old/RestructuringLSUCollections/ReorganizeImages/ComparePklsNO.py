import pickle 

def pickleOpen(p):
    file=open(p,'rb')
    data = pickle.load(file)
    file.close()
    return data



# Read in the list of all files before moving  
homeDir='/Users/ChatNoir/Google Drive/Herbiarum_Notes/ImageSpreadSheets/'


dupFiles = pickleOpen(homeDir+'no_duplicate_Aug12.pkl')
dupDict = dict((k.upper(), v) for k, v in dupFiles.items())

# Read in the list of files that were moved with good barcodes
goodFiles = pickleOpen(homeDir+'no_newPaths_Aug12.pkl')
goodDict = dict((k.upper(), v) for k, v in goodFiles.items())

badFiles = pickleOpen(homeDir+'no_badBarcode_Aug12.pkl')
badDict = dict((k.upper(), v) for k, v in badFiles.items())

len(goodDict)
len(goodFiles)

len(badDict)
len(badFiles)

allDict = {**goodDict, **badDict}

set(movedDict).difference(set(allDict))
set(allDict).difference(set(movedDict))

imageFiles = pickleOpen(homeDir+'no_imageFiles_Aug12_filename.pkl')
imageDict = dict((k.upper(), v) for k, v in imageFiles.items())

movedFiles = pickleOpen(homeDir+'no_movedFiles_Aug13_filename.pkl')
movedDict = dict((k.upper(), v) for k, v in movedFiles.items())
len(movedDict)
len(imageDict)
# All in A, that are not in B 
set(movedDict).difference(set(imageDict))
set(imageDict).difference(set(movedDict))


imageFiles = pickleOpen(homeDir+'no_imageFiles_Aug12_barcode.pkl')
imageDict = dict((k.upper(), v) for k, v in imageFiles.items())

movedFiles = pickleOpen(homeDir+'no_movedFiles_Aug13_barcode.pkl')
movedDict = dict((k.upper(), v) for k, v in movedFiles.items())

len(movedDict)
len(imageDict)
# All in A, that are not in B 
set(movedDict).difference(set(imageDict))
set(imageDict).difference(set(movedDict))





set(p29lsu).difference(set(p30lsu))
set(p30lsu).difference(set(p29lsu))



lsa = pickleOpen('/Users/ChatNoir/Projects/HerbariumRA/ggmountlsa303home/lsa303Jun06.pkl')
cbf29 = pickleOpen('/Users/ChatNoir/Projects/HerbariumRA/gmount1cyberflorahome/oldPathDictionary29.pkl')
cbf30 = pickleOpen('/Users/ChatNoir/Projects/HerbariumRA/gmount1cyberflorahome/oldPathDictionaryMay30.pkl')
cbf28 = pickleOpen('/Users/ChatNoir/Projects/HerbariumRA/gmount1cyberflorahome/barcodeImageDict.pkl')
csv30 = pickleOpen('/Users/ChatNoir/Projects/HerbariumRA/gmount1cyberflorahome/portalDictionaryMay30.pkl')

d1 = list(k.upper().split("-")[0] for k, v in lsa.items())
d2 = list(k.upper().split("-")[0] for k, v in cbf29.items())
d3 = list(k.upper().split("-")[0] for k, v in cbf30.items())
d4 = list(k.upper().split("-")[0] for k, v in cbf28.items())
p30 = list(k.upper().split("-")[0] for k, v in csv.items())

d2lsu,d2lsus = splitLSU(d2)
d3lsu,d3lsus = splitLSU(d3)
d4lsu,d4lsus = splitLSU(d4)
p30lsu,p30lsus = splitLSU(p30)


# All in A, that are not in B 
set(d4lsu).difference(set(d1))

len(set(d1).difference(set(d4lsu)))


set(d2lsu).difference(set(d1))
set(d1).difference(set(d2lsu))
LSU00051504

set(d2lsu).difference(set(d3lsu))
set(d3lsu).difference(set(d2lsu))


LSU00176590


# All in A, that are not in B 
len(set(p30lsu).difference(set(d1)))

len(set(d1).difference(set(p30lsu)))
