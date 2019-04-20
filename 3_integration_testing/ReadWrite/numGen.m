%fileID = fopen('numbers.txt','w');
for (i=1:100)
fileID = fopen('numbers.txt','w');     
fprintf(fileID,'%f\n',i);
pause(0.25);
fclose(fileID);
end
%fclose(fileID);