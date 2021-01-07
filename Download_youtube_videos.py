import pytube
#import cv2

print("Write the link to the video that you want to download")
link = input()
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('D:\Funny programs in Python')
a = stream.title
print("The video was downloaded succesfully, the name of the video is -> " + a)

#video = (a + ".mp4")

#print("D:\Funny programs in Python\{video}")


#while(True):
#    ret, frame=cap.read()
#
#    cv2.imshow('output',frame)
#    if (cv2.waitKey(1) & 0xFF == ord('q')):
#        break
#
#cap.release()
#cv2.destroyAllWindows()
