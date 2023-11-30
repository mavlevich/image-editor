import cv2


def pixelate_image(image, block_size):
    image = cv2.imread(image)

    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Resize the image to a smaller size
    small_image = cv2.resize(image, (block_size, block_size), interpolation=cv2.INTER_LINEAR)

    # Resize the small image back to the original size
    image_filter_pixel = cv2.resize(small_image, (width, height), interpolation=cv2.INTER_NEAREST)

    # Save the pixelated image
    cv2.imwrite('image_filter_pixel.jpg', image_filter_pixel)

    # Show the pixelated image
    cv2.imshow('image_filter_pixel', image_filter_pixel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pixelate_image('image.jpg', 32)

