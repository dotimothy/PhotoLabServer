% fftFile(path) Generates a real FFT Image overwriting the file path 
function fftFile(path)
    f = imread(path);
    F = real(fft(f));
    imwrite(F,path);
end