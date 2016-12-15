%produce the video by a series of images
%%
%read the files
imageNamesIn = dir(fullfile('*In*.png'));
imageNamesIn = {imageNamesIn.name}';

imageNamesOut = dir(fullfile('*Out*.png'));
imageNamesOut = {imageNamesOut.name}';

outputVideo = VideoWriter(fullfile('flux_IN_OUT.avi'));

%set the framereate
outputVideo.FrameRate = 4;
open(outputVideo)

%%write it to video
for ii = 1:length(imageNames)
	%read
   img = imread(fullfile(imageNamesIn{ii}));
   imgOut = imread(fullfile(imageNamesOut{ii}));
   
   %cut the edge
   img2 = [img(923:5555,900:4666,:) imgOut(923:5555,900:4666,:)];
   
   %too big, scaling 
   img2 =  imresize(img2, 0.3);
   
   %add the text 
   textStr = ['hour = ', num2str(ii-1)];
   img3 = insertText(img2,[10 10],textStr,'FontSize',72);
%    imshow(img3);

   
   writeVideo(outputVideo,img3)
end

close(outputVideo)