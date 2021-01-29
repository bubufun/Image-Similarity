import pymongo
from gridfs import *

def loading_image():
    myclientdata = pymongo.MongoClient("mongodb+srv://uri")
    mydbdata = myclientdata['test']
    # mycoldata = mydbdata['trash']

    
    gridFS = GridFS(mydbdata, collection="fs")
    count=0
    for grid_out in gridFS.find():
        count+=1
        print(count)
        data = grid_out.read() # 獲取圖片資料
        outf = open('%s.jpg'% count,'wb')#建立檔案
        outf.write(data)  # 儲存圖片
        outf.close()
if __name__ == '__main__':
    loading_image()