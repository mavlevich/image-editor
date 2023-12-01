import cv2


def pastel_monochrome(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to pastel
    pastel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pastel = cv2.cvtColor(pastel, cv2.COLOR_GRAY2BGR)

    # Convert the image to monochrome
    image_filter_monochrome = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_filter_monochrome = cv2.cvtColor(image_filter_monochrome, cv2.COLOR_GRAY2BGR)

    # Combine the pastel and monochrome images using weighted addition
    output = cv2.addWeighted(pastel, 0.5, image_filter_monochrome, 0.5, 0)

    # Save the pixelated image
    cv2.imwrite('image_filter_monochrome.jpg', image_filter_monochrome)

    # Show the pixelated image
    cv2.imshow('mono', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pastel_monochrome('image.jpg')
