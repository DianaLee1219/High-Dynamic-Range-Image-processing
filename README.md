📌 High Dynamic Range (HDR) Image Processing

My workplace has a beautiful view through the window and a cozy desktop setup.

However, my iPhone 12 struggled to capture both bright and dark areas in a single shot. 
So, I decided to create an HDR image myself!

The challenge? 
I took six different pictures without a tripod, resulting a blurry result. 
But honestly, who uses a tripod for iPhone photos these days?

To fix this, I applied a feature matching method—and it worked perfectly!
Now you can see my workplace showing both bright and dark regions in one image below.
![image](https://github.com/user-attachments/assets/c4b898c9-d3dd-4167-9803-1fcdee48b775)


📌 About the Code

This project code can be found at WindowViewCozyDesk.py

1. Put your images with different exposure time. (you need to adjust the Exposure Value (EV) LIST and Exposure Time) 
2. The code will do feature matching for you. (no need a tripod)
3. Adjust a gamma vaule for tone mapping. (default gamma = 2.2)
4. Download your HDR image!

📷 About the Images

Numbers only (Input) → Original photos taken with an iPhone 11, labeled by EV values.

Aligned_n (Interim result) → Images aligned relative to image 0 for better HDR processing. 

The exposure values converted into exposure time for HDR image processing.

🔹 Exposure Value to Exposure Time Conversion

EV List: [0.0, 0.3, 0.7, 1.0, 1.3, 1.7, 2.0]

Exposure Time (seconds): [0.0100, 0.0119, 0.0151, 0.0200, 0.0246, 0.0317, 0.0400]

🔹 What is EV?

"EV" indicates the amount of light (exposure amount) obtained from the combination of "lens aperture value" and "shutter speed." 
As the EV value increases, the amount of light decreases (for bright objects), and as the value decreases, the amount of light increases (for dark objects).

![image](https://github.com/user-attachments/assets/929da32b-f5ad-4dc6-a9bc-6df221f52ad3)



