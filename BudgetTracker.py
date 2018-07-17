from graphics import*
# a function to creat an interface
class available:
    def __init__(self,itemsbght,itemsbght1,itemsbght2):
        self.item=itemsbght
        self.price=itemsbght1
        self.quantita=itemsbght2

        
def interface():
    try:
        global win
        win=GraphWin("JunctionMall" ,600,600)
        win.setBackground("khaki")
        win.setCoords(0,0,7,7)
        center = Point(3,6.8)
        centera=Point(3,5.6)
        label = Text(center, "Nakumatt Lifestyle")
        label.setSize(25)
        label.draw(win)
        label.setSize(20)
        labelae=Text(Point(3,6),"Pay less,get more,Everyday")
        labelae.setSize(24)
        labelae.setFace("courier")
        labelae.draw(win)
        labela=Text(centera,"Our Dear Customer")
        labela.setSize(24)
        labela.setFace("courier")
        labela.setTextColor("blue")
        labela.draw(win)
        center1=Point(3.3,4.5)
        label1=Text(center1,"Would you like to shop with us(y/n)?")
        label1.setSize(23)
        label1.draw(win)
        entra=Entry(Point(6.5,4.5),4)
        entra.setSize(16)
        entra.draw(win)
        center2=Point(3,2.8)
        label2=Text(center2,"Welcome!!!")
        label2.setSize(22)
        label2.draw(win)

        rect=Rectangle(Point(2,1.1),Point(4,1.3))
        rect.draw(win)
        center4=Point(3,1.2)
        button=Text(center4,"Submit")
        button.draw(win)
        button.setSize(12)         
        button.setFill("Blue")
        #an indefinite loop to allow the user to proceed to purchase if he/she enters "y" and vice versa
##        while True:
        calculate=win.getMouse()
        x=calculate.getX()
        y=calculate.getY()
        if 2<=x<=4 and 1.1<=y<=1.3:
            #if the user inputs "y" for yes, then he/she is able to view the shopping window and make purchases
            if (entra.getText())=="y" or (entra.getText())=="Y":
                    label.undraw()
                    labela.undraw()
                    labelae.undraw()
                    label1.undraw()
                    label2.undraw()
                    entra.undraw()
                    global text
                    text=Text(Point(1.5,6.4),"Items")
                    text.draw(win)
                    global text1
                    text1=Text(Point(2.8,6.4),"Prices")
                    text1.draw(win)
                    global text2
                    text2=Text(Point(4.1,6.4),"Quantity")
                    text2.draw(win)
                    button.setText("Print Receipt")
                    global quan
                    quan=Text(Point(2,6.8),"Enter the quantity you want to purchase")
                    quan.draw(win)
                    global amounta
                    amount1=Point(2,6.6)
                    amounta=Text(amount1,"Enter the amount you wish to spend:")
                    amounta.draw(win)
                    global entrya
                    entrya=Entry(Point(3.9,6.6),6)
                    entrya.draw(win)
                    draw()
            #if the user inputs "n" for no,then the program displays the quit window
            else:
                    (entra.getText()[0])=="n" or (entra.getText()[0])=="N"
                    label.undraw()
                    labela.undraw()
                    label1.undraw()
                    label2.undraw()
                    labelae.undraw()
                    entra.undraw()
                    text1=Text(Point(3,5.6),"Thank you for visiting our site!!!")
                    text1.draw(win)
                    text2=Text(Point(3,5.3),"Welcome again!!!")
                    text2.draw(win)
                    button.setText("Quit")
                    win.getMouse()
                    win.close()

    except SyntaxError:
            tex=Text(Point(3,1),"Enter a string (y/n)")
            tex.draw(win)

#a function to draw the shopping window
def draw():
    #creating empty lists in which you append the items, price, and quantity
    global items
    items=[]
    global prices
    prices=[]
    global quantity
    quantity=[]
    
    j,k,l=6.1,6.1,6.1
    fileopen=open("readfile.txt","r")
    #using a for loop to draw the entry boxes for items,prices and quantities on intervals of 0.5 on the y-coordinate
    for i in range(10):
        items.append(Entry(Point(1.5,j),6))
        items[i].draw(win)
        j=j-0.5

    for i in range(10):
        prices.append(Entry(Point(2.8,k),6))
        prices[i].draw(win)
        k=k-0.5

    for i in range(10):
        quantity.append(Entry(Point(4.1,l),6))
        quantity[i].draw(win)
        quantity[i].setText(0.0)
        l=l-0.5

    #reading from file to entry boxes
    for i in range(10):
        items[i].setText(fileopen.readline())
        prices[i].setText(fileopen.readline())
        
    rect=Rectangle(Point(2,1.1),Point(4,1.3))
    rect.draw(win)
    global button
    button=Text(Point(3,1.2),"Print Receipt")
    button.setSize(12)         
    button.setFill("Blue")
    button.draw(win)
    display=win.getMouse()
    x1=display.getX()
    y1=display.getY()
    if 2<=x1<=4 and 1.1<=y1<=1.3:
        bought()
def bought():
    #a function to enable the user make selection(shop)
    global total
    total=0
    text.undraw()
    text1.undraw()
    text2.undraw()
    amounta.undraw()
    quan.undraw()
    entrya.undraw()
    m,n,p,r,t,y=6.1,6.1,6.2,6.2,6.2,6.2
    #use of a for loop to calculate the price of the items bought
    global i
    for i in range(10):
        global currentQuantity
        currentQuantity=eval(quantity[i].getText()) * eval(prices[i].getText())
        
        total=total+currentQuantity
        global itemsbght
        itemsbght=Text(Point(3,m),items[i].getText())
        var=itemsbght.getText()
        global itemsbght1
        itemsbght1=Text(Point(3.6,n),prices[i].getText())
        var2=itemsbght1.getText()
        global itemsbght2
        global value
        value = quantity[i].getText()
        itemsbght2=Text(Point(4.2,p),value)
        var3=itemsbght2.getText()
        obj= available(var,var2,var3)
        current=Text(Point(4.8,r),currentQuantity)
        global tot
        tot=Text(Point(4.8,t),str(total))
        global totprice
        totprice=Text(Point(3.8,y),"Total Price")
        global price
        price=Text(Point(3.6,6.5),"Price")
        global qua
        qua=Text(Point(4.3,6.5),"Quantity")
        items[i].undraw()
        prices[i].undraw()
        quantity[i].undraw()
        #write into a text file(item,price, and quantity) bought 
        if currentQuantity>0:
            itemsbght.draw(win)
            outfile=open("write.txt","a")
            print(var,file=outfile)
            m=m-0.5
            itemsbght1.draw(win)
            outfile=open("write.txt","a")
            print(var2,file=outfile)
            n=n-0.5
            itemsbght2.draw(win)
            outfile=open("write.txt","a")
            print(var3,file=outfile)
            p=p-0.5
            current.draw(win)
            r=r-0.5
            t=t-0.7
            y=y-0.7
        
    tot.draw(win)
    totprice.draw(win)
    price.draw(win)
    qua.draw(win)
    moreitems()
##    win.getMouse()
##    win.close()

def moreitems():
    # a function to enable the user purchase more items if he/she has a balance
    global amount
    try:
        amount=eval(entrya.getText())
        if amount>total:
            #calculate the balance remaining after the purchase
            balance=amount-total
            text5=Text(Point(2.9,4.5),"Balance GHC:")
            text5.draw(win)
            bal=Entry(Point(3.8,4.5),5)
            bal.setText(balance)
            bal.draw(win)
            text6=Text(Point(3,4.1),"Would you like to shop more items?")
            text6.draw(win)
            more=Entry(Point(4.7,4.1),4)
            more.draw(win)
            mclick=win.getMouse()
            #decision structure to enable the user purchase more items if he/she has a balance total amount intended for shopping
            if (more.getText())=="yes" or (more.getText())=="YES":
                rect2=Rectangle(Point(2,1.1),Point(4,1.3))
                rect2.draw(win)    
                button2=Text(Point(3,1.2),"")
                button2.setSize(12)         
                button2.setFill("Blue")
                button2.draw(win)
                display3=win.getMouse()
                x3=display3.getX()
                y3=display3.getY()
                
                if 2<=x3<=4 and 1.1<=y3<=1.3:
                    text5.undraw()
                    text6.undraw()
                    more.undraw()
                    entrya.undraw()
                    bal.undraw()
                    
                    block=Rectangle(Point(0,0),Point(7,7))
                    block.setFill("khaki")
                    block.draw(win)
                    tot.undraw()
                    totprice.undraw()
                    price.undraw()
                    qua.undraw()
                   
                    entrya.draw(win)
                    entrya.setText(balance)
                    amounta2=Text(Point(2,6.6),"Remaining amount")
                    amounta2.draw(win)
                    quan.draw(win)
                    textti=Text(Point(5,6.8),"...Shop more items")
                    textti.draw(win)
                    draw()
                    bought()
                    #calculate the second balance after the second purchase
                    balance2=entrya.getText()-str(total)
                    bal.setText(balance2)
                    text6.undraw()
                    more.undraw()
                    textti.undraw()
                    rect5=Rectangle(Point(2,1.1),Point(4,1.3))
                    rect5.draw(win)    
                    button5=Text(Point(3,1.2),"Quit")
                    button5.setSize(12)         
                    button5.setFill("Blue")
                    button5.draw(win)
                    display5=win.getMouse()
                    x4=display5.getX()
                    y4=display5.getY()
                    if 2<=x5<=4 and 1.1<=y5<=1.3:
                        win.getMouse()
                        win.close()
            #enable the user get the receipt if he/she has a balance but not willing to purchase more items            
            elif (more.getText())=="no" or (more.getText())=="NO":
                display2=win.getMouse()
                x2=display2.getX()
                y2=display2.getY()
                if 2<=x2<=4 and 1.1<=y2<=1.3:
                    text5.undraw()
                    text6.undraw()
                    more.undraw()
                    entrya.undraw()
                    bal.undraw()
                    block=Rectangle(Point(0,0),Point(7,7))
                    block.setFill("khaki")
                    block.draw(win)
                    tot.undraw()
                    totprice.undraw()
                    price.undraw()
                    qua.undraw()

                    text4=Text(Point(3,5.6),"Thank you for shopping with us!!")
                    sms=Text(Point(3,5.0),"Nakumatt,Saves your money!!")
                    text4.draw(win)
                    text4.setSize(28)
                    sms.setSize(24)
                    sms.draw(win)
                    rect4=Rectangle(Point(2,1.1),Point(4,1.3))
                    rect4.draw(win)    
                    button4=Text(Point(3,1.2),"Quit")
                    button4.setSize(12)         
                    button4.setFill("Blue")
                    button4.draw(win)
                    display4=win.getMouse()
                    x4=display4.getX()
                    y4=display4.getY()
                
                    if 2<=x4<=4 and 1.1<=y4<=1.3:
                        win.getMouse()
                        win.close()
##            win.getMouse()
##            win.close()    
                
        #if the user has spent the whole amount intended for shopping, close the window
        elif amount==total:
            text6=Text(Point(3,2.0),"You have used up all your cash.")
            text6.draw(win)
            text7=Text(Point(3,1.6),"Thank you for shopping with us!!!")
            text7.draw(win)
            text6.setSize(16)
            text7.setSize(16)
            win.getMouse()
            win.close()
        
        #if the user has purchased more items than the amount intended for shopping, the program allows removal of some items
        else:
            text7=Text(Point(3,1.7),"Exceeded")
            text7.draw(win)
            text8=Text(Point(3,1.5),"Please remove some items")
            text8.draw(win)
            rect5=Rectangle(Point(2,1.1),Point(4,1.3))
            rect5.draw(win)    
            
            button5=Text(Point(3,1.2),"Back")
            button5.setSize(12)         
            button5.setFill("Blue")
            button5.draw(win)
            
            button.undraw()
            
            display5=win.getMouse()
            x5=display5.getX()
            y5=display5.getY()
            
            if 2<=x5<=4 and 1.1<=y5<=1.3:
                text7.undraw()
                text8.undraw()
                entrya.draw(win)
                block=Rectangle(Point(0,0),Point(7,7))
                block.setFill("khaki")
                block.draw(win)
                amounta1=Text(Point(2,6.6),"Enter the amount you wish to spend:")
                amounta1.draw(win)
                
                tot.undraw()
                totprice.undraw()
                price.undraw()
                qua.undraw()
                draw()
                qua.draw(win)
                
                

                amounta.undraw()

##                win.getMouse()
##                win.close()

    except SyntaxError:
        ext=Text(Point(3,1),"Enter the amount to spend")
        ext.draw(win)
##    win.getMouse()
##        win.close()
interface()    
