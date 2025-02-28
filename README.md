My workplace has a beautiful view through the window and a cozy desktop setup.

However, my iPhone 11 struggled to capture both bright and dark areas in a single shot. 
So, I decided to create an HDR image myself!

The challenge? 
I took six different pictures without a tripod, resulting a blurry result. 
But honestly, who uses a tripod for iPhone photos these days?

To fix this, I applied a feature matching method—and it worked perfectly!

📌 About the Code

This project code can be found at WindowViewCozyDesk.py

📷 About the Images

Numbers only → Original photos taken with an iPhone 11, labeled by EV values.
Aligned_n → Images aligned relative to image 0 for better HDR processing.

The exposure values (EV) converted into exposure time for HDR image processing.

🔹 Exposure Value to Exposure Time Conversion
EV List: [0.0, 0.3, 0.7, 1.0, 1.3, 1.7, 2.0]
Exposure Time (seconds): [0.0100, 0.0119, 0.0151, 0.0200, 0.0246, 0.0317, 0.0400]

1) Without alignment_fusion_mertens
2) Without alighnment_ldr_robertson
3) With Alignment (cv2.createTonemap(gamma=1.5))
![without alignment_fusion_mertens](https://github.com/user-attachments/assets/36d6b357-12a3-46da-a330-a9a9f40f4ed4)
![without alighnment_ldr_robertson](https://github.com/user-attachments/assets/ce3d0592-ba0d-4f62-bc36-8b0437d95bc9)
![With Alignment](https://github.com/user-attachments/assets/2ed017f9-a83d-4868-9a10-4033e09a8308)
