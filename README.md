# SnapScuplt

## 🏺 Introduction
  Typically, a model has to go through around an hour of processing 500 frames of data to create a .  makes rough 3D scanning free and instantaneous 

## 🛠 Process

  1. [Mediapipe](https://google.github.io/mediapipe/solutions/face_mesh.html) is used to track the user's face in real-time
  2. These coordinates are fed into a Blender scene over a socket communication link
  3. The camera follows these coordinates to move in sync with the viewer's movements for a convincing effect
  4. Some post-processing on top gives the parallax effect.  
ㅤ![Screenshot 2023-08-18 at 5 09 27 PM](https://github.com/NoahBSchwartz/SnapSculpt/assets/44248582/2553897f-9526-4345-aff8-dbf7a8632536)



## Weaknesses 

## 🎉 Result
In person, the effect is convincing enough to give the illusion of looking through the screen. In fact, it's more effective than 3D glasses in some cases because of the head tracking.

![ezgif com-video-to-gif](https://github.com/NoahBSchwartz/SnapSculpt/assets/44248582/3815bc02-becb-4487-a7df-b35581b79f77)



## 🚀 How to Use

Explain how others can use your project, including setup instructions, dependencies, and examples.



