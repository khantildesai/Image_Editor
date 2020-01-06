import utilities


def rotate_90_degrees(image_array, direction = 1):
    '''
    (list) -> (List)
    This function takes an input of an image in the form of a list, and returns
    the image rotated either clockwise or anticlock wise
    direction 1 = clockwise
    direction -1 = anticlockwise
    Examples:
    '''
    #print(image_array)
    if direction == 1:
        temp = []
        result = []
        for column in range(len(image_array[0])):
            #loops through columns
            for row in range(len(image_array)):
                temp.append(image_array[row][column])
                #reates temp vairbale of reach row in original
            temp.reverse()
            result.append(temp)
            temp = []
            #reverses list and adds it to result
        return result
    elif direction == -1:
        temp = []
        result = []
        r = 0
        for row in range(len(image_array)):
            result.append([])
            image_array[row].reverse()
        # reverses each row of original and formats result varuable to correct size 
        while r < len(image_array):
            image_array[r].reverse()
            temp = image_array[r]
            #loop through process till aplied to all rows of result variable
            for index in range(len(temp)):
                result[index].append(temp[index])
                #addes correct value for each variable in temp to result
            r += 1
        return result
                

def flip_image(image_array, axis = 0):
    '''
    (list) -> (List)
    This function takes an input of an image in the form of a list, and returns
    the image flipped along the x axis(1), y axis (0), x = y axis (-1) 
    Examples:
    '''
    #axis = -1 (along x = y), 0 along y, 1 along x
    if axis == 1:
        r = 0
        while r < (int(len(image_array)/2)) + 1:
            image_array[0 + r], image_array[0 - r] = image_array[0 - r], image_array[0 + r]
            r += 1
        return image_array
    elif axis == 0:
        for row in range(len(image_array)):
            image_array[row].reverse()
        return image_array
    elif axis == -1:
        return flip_image(rotate_90_degrees(image_array), 1)
    #return output_array

def invert_grayscale(image_array):
    '''
    (list) -> (list)
    This function takes an input of an image in the form of a list, and returns
    the inverted grayscale image as a list 
    Examples:
    ''' 
    for row in range(len(image_array)):
        for column in range(len(image_array[row])):
            n = 255 - image_array[row][column]
            image_array[row][column] = n
    return image_array

def crop(image_array, direction, n_pixels):
    '''
    (list, string, int) -> (list)
    This function takes an input of an image in the form of a list, and returns
    the cropped image in the up, down, left, right direction by n_pixels) 
    Examples:
    '''

    if direction == 'up':
        image_array = image_array[n_pixels:]
    elif direction == 'down':
        image_array = image_array[:len(image_array) - n_pixels]
    elif direction == 'left':
        for r in range(len(image_array)):
            image_array[r] = image_array[r][n_pixels:]
    elif direction == 'right':
        for r in range(len(image_array)):
            image_array[r] = image_array[r][:len(image_array) - n_pixels]
    return image_array
    #return output_array

def rgb_to_grayscale(rgb_image_array):
    '''
    (list) -> (list)
    This function takes inputs of images as lists and returns a list representing that image in grayscale
    '''
    for row in range(len(rgb_image_array)):
        for column in range(len(rgb_image_array[0])):
            rgb_image_array[row][column] = 0.2989 * rgb_image_array[row][column][0] + 0.5870 * rgb_image_array[row][column][1] + 0.1140 * rgb_image_array[row][column][2]
    return rgb_image_array
    #return output_array

def invert_rgb(image_array):
    '''
    (list) -> list
    This function takes input as a list and returns a list representing inverted invered\
    '''
    for row in range(len(image_array)):
        for column in range(len(image_array[0])):
            image_array[row][column][0] = 255 - image_array[row][column][0]
            image_array[row][column][1] = 255 - image_array[row][column][1]
            image_array[row][column][2] = 255 - image_array[row][column][2]
    return image_array
    #return output_array


if (__name__ == "__main__"):
    file = 'robot.png'
    utilities.write_image(flip_image(utilities.image_to_list(file), -1), 'gray.png')
    #print(invert_grayscale([[1,1, 1,0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0]]))
