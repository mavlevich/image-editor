import cv2


def increase_resolution(image_path):
    # Load image from file
    img = cv2.imread(image_path)

    # Get the original image size
    height, width, _ = img.shape

    # Create a new image with twice the resolution
    new_width = width * 2
    new_height = height * 2
    filter_increased_resolution = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Save the result to a file
    cv2.imwrite('filter_increased_resolution.jpg', filter_increased_resolution)

    # Show the result
    cv2.imshow('Increased Resolution', filter_increased_resolution)
    cv2.waitKey(0)


increase_resolution('image.jpg')
