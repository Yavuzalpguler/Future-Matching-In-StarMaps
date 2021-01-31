import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt


def futureMatch(img1, img2):
    
    #We are using ORB since SIFT and SURF are beyond our reach for the moment, and we can make use of anyone of them.
    orb = cv2.ORB_create(20000)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # Since ORB is based on binary descriptors, HAMMING is the way to go.
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key = lambda x:x.distance)
    
     
    # Extracting location components from kp1 and kp2.
    src_pts = np.float32([ kp1[n.queryIdx].pt for m,n in enumerate(matches) ])
    dst_pts = np.float32([ kp2[n.trainIdx].pt for m,n in enumerate(matches) ])
    
    
    # Using homography to find the relation of points on the same plane.  
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    return dst



if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-futureimg', type=str, default="src/Small_area_rotated.png", help="Template image path")
    parser.add_argument('-map', type=str, default="src/StarMap.png", help="Main image path")
    args = parser.parse_args()
  
    
    starmap = cv2.imread(args.map)
    future = cv2.imread(args.futureimg)

    graymap = cv2.cvtColor(starmap, cv2.COLOR_BGR2GRAY)
    grayfuture = cv2.cvtColor(future, cv2.COLOR_BGR2GRAY)
    
    dst = futureMatch(grayfuture, graymap)
    dstx = np.zeros((len(dst), 2), dtype=np.int32)

    #Reorganizing the locations array by rounding the elements, eventhough this results in minimal resolution losts and the results do not shape a square sometimes, it is more convenient for the user to read the data.
    for i in range(len(dst)):
        for j in range(2):
             dstx[i][j]=round(dst[i][0][j])
            

    print(dstx)



   