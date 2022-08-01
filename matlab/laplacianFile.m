% shapren(path): Sharpens an Image 
function laplacianFile(path)
    im = imread(path);
    lap = [1 1 1; 1 -8 1; 1 1 1];
    imSharp =  imfilter(im,lap);
    imSharp = uint8(imSharp);
    imwrite(imSharp,path);
end