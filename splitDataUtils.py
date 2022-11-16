import os
import shutil

DIR_PATH = "/home/felipeserver/Documents/datasets/plant_types/dataset_type_of_plants_new/dataset_type_of_plants_new"
TARGET_DIR = "/home/felipeserver/Documents/development/ml/plant_types/data"

class Utils:
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.train_files = dict()
        self.test_files = dict()
        self.class_names = None

    def splitData(self):
        self.class_names = os.listdir(self.dirpath)

        #min_val = min([len(os.listdir(os.path.join(self.dirpath, c))) for c in self.class_names])

        for class_ in self.class_names:
            files =  os.listdir(os.path.join(self.dirpath, class_))
            self.train_files[class_] = files[:-int(len(files)*0.2)]
            self.test_files[class_] = files[-int(len(files)*0.2):]


    def makeDirStructure(self, target_dir):
        if not os.path.exists(os.path.join(target_dir,"train")):
            os.makedirs(os.path.join(target_dir, "train"))
        else:
            print("Folder structure already exists!")

        if not os.path.exists(os.path.join(target_dir,"test")):
            os.makedirs(os.path.join(target_dir, "test"))
        else:
            print("Folder structure already exists!")

        for name in self.class_names:
            os.mkdir(target_dir + "/train/" + name)
            os.mkdir(target_dir + "/test/" + name)
            for img in self.train_files[name]:
                shutil.copy2(self.dirpath + "/" + name + "/" + img, target_dir + "/train/" + name + "/" + img)

            for i in self.test_files[name]:
                shutil.copy2(self.dirpath + "/" + name + "/" + i, target_dir + "/test/" + name + "/" + i)

        print("Files copied!")

dir1 = Utils(DIR_PATH)
dir1.splitData()
dir1.makeDirStructure(TARGET_DIR)

