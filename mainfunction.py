from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from welcome_screen import Ui_welcome_screen
from student import Ui_student
from faculity import Ui_Faculity 
from showbook import Ui_showbook
from issuebook import Ui_issuebook
from returnbook import Ui_returnbook
from addbook import Ui_addbook
import sys,os

books=['python','java','c++','oops','c programming','python automation','java advance','vue js']
rollno_list=[]
li=[]
issue=[]
allbooks=[]
#registration file
if'rollno.txt' in os.listdir():
    with open('rollno.txt')as f:
        rollno_list=f.read().split()
    f.close()
else:
    with open('rollno.txt','w')as f:
        f.write(rollno_list+ '\n')
    f.close()

#allbooks file
if'books.txt' in os.listdir():
    with open('books.txt')as f:
        allbooks=f.read().split()
    f.close()
else:
    with open('books.txt','w')as f:
        for i in books:
            f.write(i+'\n')
    f.close()



#MAIN WINDOW CLASS
class welcome_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_welcome_screen()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.studentfun)
        self.ui.pushButton_2.clicked.connect(self.faculityfun)
        
#student btn 
    def studentfun(self):
        self.st=studentclass()
        self.st.show()
        # print("student")
        self.hide()

#staff btn
    def faculityfun(self):
        self.f=faculityclass() #f obj. of faculityclass class
        self.f.show()
        # print("faculity")
        self.hide()
        

#STUDETN CLASS
class studentclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_student()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.submitrecord)
        self.ui.pushButton_2.clicked.connect(self.back)

    def submitrecord(self):
        # print("submit record")
        name=self.ui.lineEdit.text()
        roll =self.ui.lineEdit_2.text()
        branch=self.ui.lineEdit_3.text()
#        print(f"{name} {roll} {branch}")
        if roll in rollno_list:
            #for msg dialogbox
            msg= QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText(f"{name} You Are Already Registered!")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec_()
        else:
            with open('rollno.txt','a')as f:
                f.write(roll+'\n')
            f.close()
            rollno_list.append(roll)
            
            #for msg dialogbox
            msg= QMessageBox()
            msg.setWindowTitle("Done")
            msg.setText(f"{name} Your Registration is Successfull Done!")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec_()
        
    def back(self):
        # print("back")
        self.wc=welcome_screen()#obj of welcome-scren cls
        self.wc.show()#show welcome screen 
        self.hide()# hide 
        

print(allbooks)
print(rollno_list)
#FACULITY CLASS
class faculityclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_Faculity()  #  ui obj. of class Ui_faculity
        self.ui.setupUi(self)
        self.ui.showbtn.clicked.connect(self.showbook)
        self.ui.add.clicked.connect(self.addbook)
        self.ui.issue.clicked.connect(self.issuebook)
        self.ui.return_2.clicked.connect(self.returnbook)
        self.ui.back.clicked.connect(self.back)
      
    def showbook(self):
        self.sb=showbookclass()
        self.sb.show()
        # print("show book")
        self.hide()

    def addbook(self):
        self.ab=addbookclass()
        self.ab.show()
        self.hide()
    #    print("add book")
    
    def issuebook(self):
        self.ib=issuebookclass()
        self.ib.show()
        # print("issue book")
        self.hide()
    
    def returnbook(self):
        self.rb=returnbook()
        self.rb.show()
        self.hide()
        
        # print("return book")

    def back(self):
        # print("back")
        self.wc=welcome_screen()
        self.wc.show()
        self.hide()

class showbookclass(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui=Ui_showbook()
        self.ui.setupUi(self)
       
        self.ui.back.clicked.connect(self.backbtn)
        print(allbooks)
        li=""
        index=0
        for i in allbooks:
            # li=li+" "+i

            if index >=6 and index <=11:
                li=li+" "+i
                # self.ui.label.setText(li)
            elif index >=12 and index <=20:
                    li=li+"\n"+i
                    # self.ui.label.setText(li)
            else:
                li=li+" "+i

            self.ui.label.setText(li)
            index+=1    
        
    def backbtn(self):
        # print("back")
        self.f=faculityclass()
        self.f.show()
        self.hide()
#issue book
class issuebookclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_issuebook()
        self.ui.setupUi(self)
        self.ui.issuebtn.clicked.connect(self.issuebtnbook)
        self.ui.back.clicked.connect(self.backbtn)

    def issuebtnbook(self):
        # print("issue book is issue")
        bookname= self.ui.lineEdit.text()
        roll=self.ui.lineEdit_2.text()
        if roll in rollno_list:
            #for book name is exits in library
            if bookname in allbooks:
                #for already issue book or not
                if roll not in issue:
                    #add roll no in issue list
                    issue.append(roll)
                    # book remove from library
                    allbooks.remove(bookname)
                    with open('issue.txt','a')as f:
                        for i in li:
                            f.write(i+'\n')
                    f.close()
                    self.ui.label.setText(f"You have been issued {bookname} Book.")
                    msg=QMessageBox()
                    msg.setWindowTitle("Done")
                    msg.setText("Please keep it safe and return it within 30 days Otherwise you give Rs5 fine per day!")
                    msg.setIcon(QMessageBox.Information)
                    x=msg.exec_()

                    with open('issue.txt','w')as f:
                        # write issuenlist data in issue file
                        for i in issue:
                            f.write(i+'\n')
                        f.close()

                else:
                    self.ui.label.setText("We can't issue you more book!")
            else:
                self.ui.label.setText("This book is either not available or has already been issued to someone else.\n Please wait the book is available!")
        else:
            self.ui.label.setText("Your Roll Number Not Registered First go and Registered Yourself! ")


    def backbtn(self):
        # print("back")
        self.f=faculityclass()
        self.f.show()
        self.hide()

#return book
class returnbook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_returnbook()
        self.ui.setupUi(self)
        self.ui.returnbtn.clicked.connect(self.bookreturn)
        self.ui.back.clicked.connect(self.back)

    def bookreturn(self):
        # print(rollno_list)
        bookname=self.ui.lineEdit.text()
        roll=self.ui.lineEdit_2.text()

        if roll in rollno_list:
            if roll in issue:
                #rollno delete from issue list
                issue.remove(roll)
                allbooks.append(bookname)
                with open('issue.txt','w')as f:
                    for i in issue:
                        f.write(i+'\n')
                    f.close()

                with open('books.txt','w')as f:
                    for i in allbooks:
                        f.write(i+'\n')
                    f.close()

                
                self.ui.label.setText(f" {bookname} Book Return!")
            else:
                self.ui.label.setText("Sory No Book is issued to you! ")
        else:
             #self.ui.label.setText("You Are Not Registered !")
             msg=QMessageBox()
             msg.setWindowTitle("Information")
             msg.setText("You Are Not Registered!")
             msg.setIcon(QMessageBox.Information)
             x=msg.exec_()

     

    def back(self):
        self.f=faculityclass()
        self.f.show()
        self.hide()
    
#add book
class addbookclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_addbook()
        self.ui.setupUi(self)
        self.ui.addbtn.clicked.connect(self.bookadd)
        self.ui.back.clicked.connect(self.back)

    def bookadd(self):
        bookname=self.ui.lineEdit.text()
        if bookname not in allbooks:
                        
            self.ui.label.setText(f"New  {bookname} book Sucessfully Add in the Library ")
            
            allbooks.append(bookname)
            with open('books.txt','w')as f:
                for i in allbooks:
                    f.write(i+'\n')
                f.close()
        else:
            msg=QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("This Book is already Present in the library")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec_()
         
    def back(self):
        self.f=faculityclass()
        self.f.show()
        self.hide()
    

app=QApplication(sys.argv)
wc=welcome_screen() # crate obj of class welcome_screen
wc.show()
sys.exit(app.exec_())