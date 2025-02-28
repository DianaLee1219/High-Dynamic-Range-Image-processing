import cv2
import numpy as np
import glob

def align_images(images):
    """Align images using ORB feature matching and homography."""
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Use the first image as the reference
    ref_img = images[0]
    aligned_images = [ref_img]

    for i in range(1, len(images)):
        img = images[i]
        
        # Detect and compute ORB features
        kp1, des1 = orb.detectAndCompute(ref_img, None)
        kp2, des2 = orb.detectAndCompute(img, None)
        
        # Match features
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        # Extract matched points
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # Compute homography
        H, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

        # Warp image to align with reference
        aligned = cv2.warpPerspective(img, H, (ref_img.shape[1], ref_img.shape[0]))
        aligned_images.append(aligned)

    return aligned_images

def create_hdr(images, exposure_times):
    """Create HDR image from multiple exposures."""
    # Align images to avoid blur
    aligned_images = align_images(images)    

    # Convert exposure times to numpy float32 array
    exposure_times = np.array(exposure_times, dtype=np.float32)

    # Merge to HDR
    merge_debevec = cv2.createMergeDebevec()
    hdr = merge_debevec.process(aligned_images, times=exposure_times.copy())

    # Tone mapping
    tonemap = cv2.createTonemap(gamma=1.5)
    ldr = tonemap.process(hdr)
    ldr = np.clip(ldr * 255, 0, 255).astype(np.uint8)

    return ldr

if __name__ == "__main__":
    # List of image filenames
    filenames = ["0.0.jpg", "0.3.jpg", "0.7.jpg", "1.0.jpg", "1.3.jpg", "1.7.jpg", "2.0.jpg"]
    images = []
    for filename in filenames:
      im = cv2.imread(filename)
      images.append(im)
    
    # Exposure times corresponding to images
    exposure_times = [0.0100, 0.0119, 0.0151, 0.0200, 0.0246, 0.0317, 0.0400]

    # Generate HDR image
    hdr_image = create_hdr(images, exposure_times)

    # Save the result
    cv2.imwrite("hdr_result.jpg", hdr_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
