import time, os
# Hiệu ứng loading
from time import sleep

while True:
    ns = input("Nhập ngày tháng năm sinh của bạn: \n")
    # Nếu Nhập Đúng
    # thay cả trên này nữa nha cả 2 cái trên và dưới thay giống nhau
    if ns == "31/03/2007":
        print("Chính Xác !!!")
        time.sleep(1)
        # lệnh thoát vòng lặp khi nhập đúng
        break
    # Nếu Nhập Sai
    else:
        ns_2 = input("Bạn nhập sai rồi ! Nhập lại nào: \n")
        # các bạn chỉnh ngày sinh tùy ý nhé !
        if ns_2 == "31/03/2007":
            print("Chính Xác !!!")
        else:
            print("Bạn nhập sai rồi ! Thoát")
            exit()
        time.sleep(1)
        # lệnh tiếp tục vòng lặp khi nhập key sai
        break
time.sleep(3)
os.system("cls")
time.sleep(2)
print("          ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ ")
print("          ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ ")
print("          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗")
print("          ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║")
print("          ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝")
print("          ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
print("")


def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill="█"):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()


items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
print("\n")
time.sleep(2)
# 3 cái ngoặc kép nha rồi dán code ascii vừa copy, sau đó đóng 3 ngoặc kép lại
# bây giờ thêm hiệu ứng nha

string = """
XXXNNNNNNNWXd',okkOOx;.....xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMN0kkxxxxxxddddd
XXNNNNNNNWWXd',okkOOx;.....xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kkkxxxxxxdddd
NNNNNNNWWWWXd''okOOOk;.....xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kkkkxxxxxdddd
NNNNNWWWWWWNd''okOO0k;.....xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kkkkxxxxddddd
NNNNWWWWWWMNx''okOO0k:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOkOkkxxxxddddd
NNNWWWWWWWMNx''oOOO0k:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNNNXK00NWWWWMMMMMMNOkOOkkxxdddddd
NNWWWWWMMMMNx,'oOOO0k:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0OOOkkxxdddddooxkO0KNWWMMMNOOOOkkxxdxxxdx
WWWWWWMMMMMWk,'oOOO0k:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWKkdollllccclllllllc::ccldk0XWX0O0Okkxdodxxxx
WWWWWMMMMMMWk,'oOO00k:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNkoollcccc:ccccc:::;,;;;,,::ldkO00OOkxxdddxkx
WWWWMMMMMMMWk,'oOO00O:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNkoollcccccccc:::;:;,,;;,,;;;,,lO000OOkkkkkkk
WWWMMMMMMMMWk,'oOO00O:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWW0dlc:;;;::::::::;;:;;;;,,;;,,.;k000OOOkkkkkk
WWWMMMMMMMMWk,'oO000O:.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0l...........',,,;;;,,,,,;,'.;x0000OOkkkkkk
WWMMMMMMMMMWO,'oOO00Oc.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd'.';,,;,..     ............;d00000OOOkkkkk
WMMMMMMMMMMWO,'oOO00Oc.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk'..ll::ll;,.             .:x00K000000OOOOkk
WMMMMMMMMMMWO,'oOO00Oc.....dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNl. 'ddcldxdo:.            .oXX0KKKK000OOOOOk
MMMMMMMMMMMWO,'oOO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc..,oolccllll:. ...        .:k00KK0000OOOOkk
MMMMMMMMMMMWO,'oOO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl. ,lcclccooc::,''..         .lO00KKK00OOOOk
MMMMMMMMMMMW0,.oOO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c. .oxOKK0OxdkOxl:'.          .:kKKKK00OOOkk
MMMMMMMMMMMW0;.oOO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNO;  .oXNNXK0KXXXkc:;'.           'o000000OOkk
MMMMMMMMMMMW0;.oOO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk,   .dXX0Oxk0KKkc;::,...         .;dO0000OOk
MMMMMMMMMMMWO,.okO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNx'    .dOOddkkOOko:;,,,;;..         .;ok0OOOk
MMMMMMMMMMMWO,.lkO00Oc.....oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0l.    ':ldolcoxxdc;,;;;;;;,...        .ckOOOO
MMMMMMMMMMMWO,.lkO00O:.....oWMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMWWKd:'.   .,::ldxxxxl,.,;;;;::;''....',,,;:c:lxOOO
MMMMMMMMMMMWO,.lkO00O:.....oWMMMMMMMMMMMMMMMMMMMMMMMMMWNNWWWWWWWWWWWWWNXd;,...  .,::::clcc:,,;;,;:c:;,'....,;codolc;:oOO
MMMMMMMMMMMW0,.lkOOOO:.....oWMMMMMMMMMMMMMMMMMMMMMMMWWNXNNNNNNNNNNNNNNXKk:'.    .';:::;;:::::;,;;:;;;'',';:clll:,,,',:xO
MMMMMMMMMMMW0,.ckOOOO:.....oWMMMMMMMMMMMMMMMMMMMMMWNNXXXXXXXXXXXXNXXXXK0ocl,   .''.,::;:::;;::;;::::,';:cclcc:;,,;,,;;ok
MMMMMMMMMMMW0,.ckOOOO:. ...oWMMMMMMMMMMMMMMMMMMMWNNXXXXXXXNNNNXXXXXXXKko:lOk;..,::;,;::::;;;;;;;;;;,,;cll::ccc::c:,,,':x
MMMMMMMMMMMWO,.ckOOOO:. ...oWMMMMMMMMMMMMMMMMWWNNXXXXXXXXXNNNNXXXXNXOklck0O00kkOOOxll:,,,,,,,;;;::;;::c;;cclc:cc:'...';d
MMMMMMMMMMMWO,.ckOOOk:. . .oWMMMMMMMMMMMMMWWWNXXXXXXXXXXXXXNNNXXXXX0ko:xKkx0XKK0Okd:::;'',,,;::cc;;:;cl;::;c:::::'. .,,l
WMMMMMMMMMMWO,.cxkOOk:.   .lNMMMMMMMMMMMWWNNXXXXXXXXXXXXXXXNNNNNXNXOl':00ddOKXKOddooooc;',:::ccc:;;;;ldl;',:::ccc:,,'',;
WWMMMMMMMMMWO'.cxkOOk:.   .lNMMMMMMMMWWWNXXXXXXXXXXXXXXXXXXXNNNNNNXk,.'dOdk00Oxdoloxxl;,,,;::c:::,;;,lxdc.';cllcclc;,;,'
WWMMMMMMMMMWO'.cxkOOk:    .lNMMMMMMMWWNXXXXXXXXXXXXXXXXXXXXXXXNNXXKd;..'oddkOxlllllc:;;,cddc;:c:;,;;;lddd;.,;:clc:;;::,,
WWMMMMMMMMMWO'.:xkkOk:     lNMMMMWWWNXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOko,. .:xdolcccc:;;,:d0XX0dc:;,;;;;codl,.';:cc::;::;,,
WWWWWMMMMMMWO'.:xkkkk:     lNMMWWWNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX00Kk:..:ONKc,:::;;:cdOKXXXXX0d,';;;;:ll,.';:::;,,,,''''
WWWWWWMMMMMWO'.:xkkkx;     lNMWNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0Kk:,;l0WWWKl,,;cdOKKXXXXXXXk:,,;;,,;;'.',;,;;;;;;,,,;;
WWWWWWWMMMMWk'.:xxkkx;     lNWNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKxodoooOXNNKxclkXNNNNXXKKOo;';;:c,..''',;;:c:::;;;:;;;
NNWWWWWWWWMWk'.:dxxkx;     cXNXXXXXXXXXXXXXXXXXXXXXXXKKKKXXXXXXXXX0xxdlc:lox00Oko:o0XNNXKkc;;;,;;cl:',,,,;:::cc:::;;;,''
NNNNNWWWWWWNk'.:dxxxx;     cXNXXXXXXXXXXXXXXXXXXXXKKKKXKKXXXXXXXXKdodol::ll:cclc;;;:o0XOl,'';;,;:coc;::;,,,;;::::;,'....
NNNNNNNWNNNNk'.;dxxxd;.....lKXXXXXXXXXXXXXXXXXXXKKKKKXKKKKKXXXXXXKxoolc;,lo:,,'';:;,,;:,''',;:;;cclc::c:::;::;;;;,,'....
XXXXXXNNNNNXx..;dxddc'''.'';ok0XXXXXXXXXXXXXXXXKXKKKXKKKKKKXNXOxdo::llc;,cl;...;c:,,,'''''',,::::::cccc::c:;::;;;,''....
XXXXXXXXXNNXx'.;doc,'...   .':ONXXNXXXXXXXXXXXKKKKKKKKKK0Okkkxoc:'  .::,'''..';cc;',;;,'.''',,;:,',;;::;;::;;:;,,.......
KKKKKKXXXXXKx'.;lll:....... .;lOXNNNNXXXXKKKKKKKKKKKXX0dl:;'....     c:.... .clc;,',;;;;,''''',;,,,.'',,;,,,,;;'....... 
KKKKKKKKXXXKx..;l:,''..''......;xXWNNNXKKKKKKKKKKKKXKOocc;.         .dl .. .cll:,'';;;::;,',;,'',,,'''',,,,'','.......  
0KKKKKKKKKKKd'.:c;... ....     .,cxk0NXKKK0KKKKKKKKkollc,.    .     .Ox....colc,''';;;;;:;;;;;..,'....'''''',,........  
00000KKKKKK0d;col:.   ...      .....lXXXKK000KKKKKOl:dc. ..  .,.    '0O. .:doc;''.';;;;;;;;;;;'.,,. .......''...  ....  
"""
list_str = string.split()
for i in list_str:
    print(i)
    time.sleep(0.1)
