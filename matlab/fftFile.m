% fftFile(path) Generates a real FFT Image (center is DC) overwriting the file path 
function fftFile(path)
    f = imread(path);
    if(size(f,3) > 1)
        f = rgb2gray(f); 
    end
    % DC Shift %
    [M,N] = size(f);
    f_s = zeros(size(f));
    for x = 1:M
        for y = 1:N
        f_s(x,y) = f(x,y) * (-1)^(x+y);  
        end
    end
    % FFT %
    F = uint8(abs(fft2(f_s)));
    imwrite(F,path);
end