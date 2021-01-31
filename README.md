# Future-Matching-In-StarMaps

This repository includes the solutions to 4D Sight job application tasks. \
Main mission to be accomplished is to locate the cropped images in the bigger image.

## Installation for dependencies



```bash
pip3 install -r requirements.txt
```

## Usage

By default, the paths to the StarMap files are not needed to be indicated. \
However, if you want to use the script for your own purposes, feel free to do so as below.

```bash
cd Future-Matching-In-StarMaps
python main.py [-h] [-futureimg FUTUREIMG] [-map MAP]
```



## References

[OpenCV ORB Documentation](https://docs.opencv.org/master/d1/d89/tutorial_py_orb.html)

[OpenCV Future Matching Documentation](https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html)

[OpenCV Future Matching + Homography Documentation](https://docs.opencv.org/master/d1/de0/tutorial_py_feature_homography.html)

