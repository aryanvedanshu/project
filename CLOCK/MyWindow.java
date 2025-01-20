import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.lang.*;


public class MyWindow extends JFrame{

    private JLabel heading;

    private JLabel clockLabel;

    private Font font = new Font ("", Font.BOLD, 40 );

     
    MyWindow() 
    {
        super.setTitle("My Clock");
        super.setSize(500,500);
        super.setLocation(300,200);
        this.createGUI();
        this.startClock();
        super.setVisible(true);
    }

    public void createGUI()
    {
        heading = new JLabel("My clock");

        clockLabel = new JLabel("clock");

        heading.setFont(font);
        clockLabel.setFont(font);

        this.setLayout (new GridLayout(2,1));

        this.add (heading);

        this.add(clockLabel);
    }

    public void startClock()
    {
//         Timer timer = new Timer(1000, new ActionListener() {
//             public void actionPerformed(ActionEvent e){
// //                 Date d = new Date();
                
// //                 SimpleDateFormat sfd = new SimpleDateFormat("hh:mm:ss  aa");
// //                 String dateTime= sfd.format(d);

// // //                String dateTime=new Date().toString();

// //                 clockLabel.setText(dateTime);

//             }
//         } );
//         timer.start();

        Thread t = new Thread()
        {
        public void run(){
            try{
                while(true){
                Date d = new Date();
                
                SimpleDateFormat sfd = new SimpleDateFormat("hh:mm:ss:  aa");
                String dateTime= sfd.format(d);

//              String dateTime=new Date().toString();

                clockLabel.setText(dateTime);  

                Thread.sleep(1000);
                
                }
            }
            catch (InterruptedException e){
                e.printStackTrace();
            }
        }

    };
    t.start();

    }
}
