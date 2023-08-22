# SnapScuplt

## 🏺 Introduction
  Typically, to 3D scan a model into CAD, users have to process a video of their object for hours. This is perfect for getting the most accurate results possible, but engineers often only care about the general shape and ratios of a part in a larger assembly. ScanSculpt gives this type of rough 3D scanning its own process by relying on data from only 3 images, processed in seconds. 

## 🛠 Process

  1. The [removebg](https://www.remove.bg/) library highlights the foreground and the background of each of the 3 images
  2. Then, OpenCV masks out the background so only the outline of the object remains
  3. The dimensions of the 3 cutouts can be compared together to properly size and position the pictures 
  4. Some post-processing on top gives the parallax effect.  
ㅤ![Screenshot 2023-08-18 at 5 09 27 PM](https://github.com/NoahBSchwartz/SnapSculpt/assets/44248582/2553897f-9526-4345-aff8-dbf7a8632536)



## Weaknesses 

## 🎉 Result
In person, the effect is convincing enough to give the illusion of looking through the screen. In fact, it's more effective than 3D glasses in some cases because of the head tracking.

![ezgif com-video-to-gif](https://github.com/NoahBSchwartz/SnapSculpt/assets/44248582/3815bc02-becb-4487-a7df-b35581b79f77)



## 🚀 How to Use

Explain how others can use your project, including setup instructions, dependencies, and examples.



