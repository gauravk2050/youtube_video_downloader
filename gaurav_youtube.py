from pytube import YouTube
from time import sleep

def Main():
    ans='y'
    while ans=='y':
        yt = inp()
        ch = int(input("ENTER YOU CHOICE \n1.Show Details\n2.Stream\n3.Download\n4.exit"))
        if ch == 1:
            details(yt)
        elif ch ==2:
            stream(yt)
        elif ch==3:
            down(yt)
        else:
            exit(0)
        ans = input('Enter y to continue..')
        
def inp():
    st = input('Enter you Link')
    y = YouTube(st)
    return y

def details(yt):
    print('Details:\n')
    print('Title: ',yt.title)
    print('length: ',yt.length,'Sec')
    print('thumbnail: \n',yt.thumbnail_url)
    print('description:\n ',yt.description)
    print('Rating:\n',yt.rating)
    print('Views: ',yt.views)
    print('Age Restriction: ',yt.age_restricted)
    print('ID: ',yt.video_id)
    
def stream(t):
    s=t.streams
    a='y'
    while a=='y':
        c = int(input(' 1.DASH Stream\n 2.Progressive Stream\n  3.Stream all\n  4.Stream Audio\n    5.Stream Video'))
        if c == 1:
            print('Dash------\n')
            print(s.filter(adaptive=True).all())
        elif c == 2:
            print(s.filter(progressive=True).all())
        elif c == 3:
            print(s.all())
        elif c == 4:
            print('Audio---------\n')
            print(s.filter(only_audio=True).all())
        elif c == 5:
            print(s.filter(file_extension='mp4').all())
        else:
            print('Wrong Input')
        a=input('Enter y To Stream Again')
        
def down(yt):
    title = yt.title
    c=int(input("   1.Video\n   2.Audio"))
    if c==1:
        s = yt.streams.filter(progressive=True, file_extension='mp4')
        print("Available formats for >>>", title, "youtube video")
        a = 1
        for i in s:
            print(a, end=".")
            print(i.resolution)
            a += 1
        resol = input("Enter any Resolution Quality from above>>")
        if "p" in resol:
            userentry = resol
        else:
            userentry = str(resol) + "p"
        # x is the stream which user want to download
        x = yt.streams.get_by_resolution(userentry)
        if x == None:
            print("No resolution like this try again")
        else:
            print("Please wait your video is being downloading", end="")
            for i in range(10):
                print(".", end="")
                sleep(1)
            x.download('C:/Users/GAURAV/Music/')
            print("\nYour video is downloaded")
            sleep(1)
            print("Thanks for visiting us")
    elif c==2:
        yt.streams.last().download('C:/Users/GAURAV/Music/')
        print("\nYour Audio is downloaded")
        sleep(1)
        print("Thanks for visiting us")
    else:
        print("OOPS WRONG INPUT...")
if __name__=='__main__':
    Main()


