from PIL import Image

# ASCII characters used
ASCII_chars = ["@", "#", "$", "%", "&", "^", "*", "+", ";", ":", ",", "."]

# resizing according to a new width
def resize_image(image, new_width):
	width, height = image.size
	ratio = height/width
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height)) # makes a tuple
	return resized_image


# grayifying the image
def grayify(image):
	greyscaled_image = image.convert("L")
	return greyscaled_image


# convert pixels to string of ASCII characters
def pixels_to_ASCII(image):
	pixels = image.getdata()  # this returns a list of pixels
	characters = "".join(ASCII_chars[pixel // 25] for pixel in pixels)
	return characters


# main
def main():
	new_width = int(input("Enter required width: "))
	path = input("Enter pathname to an image: ")
	try:
		image = Image.open(path)
	except:
		print(path,"isn't a valid pathname of your image")
		return

	# converting image to ASCII
	new_image_data = pixels_to_ASCII(grayify(resize_image(image, new_width)))

	# format
	ASCII_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, len(new_image_data), new_width)])

	print(ASCII_image)

main()