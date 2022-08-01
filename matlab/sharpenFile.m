% shapren(path): Sharpens an Image 
function sharpenFile(path)
    im = imread(path);
    sharp = [-1 -1 -1; -1 9 -1; -1 -1 -1];
    imSharp =  imfilter(im,sharp);
    imSharp = uint8(imSharp);
    imwrite(imSharp,path);
end