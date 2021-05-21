using System;
using System.Windows.Forms;

using System.IO;
using System.IO.Pipes;
using System.Diagnostics;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {

        int cch = 1;
        string delimiter = ",";
        bool sent = false;
        public Form1()
        {
            InitializeComponent();



        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            using (StreamWriter writer = new StreamWriter(@"test.txt"))
            {
                writer.Write(-0.054541539 + delimiter + -0.25991479 + delimiter + -0.157079633 + delimiter + -0.783930406 + delimiter + -0.450946312);
                sent = true;

            }


        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter(@"test.txt"))
            {
                writer.Write(textBox1.Text);
               

            }
        }


        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //Console.WriteLine("co phim dc nhan");
          //  Console.WriteLine(e.KeyChar);

            using (StreamWriter writer = new StreamWriter(@"test.txt"))
            {


               writer.Write(e.KeyChar);


            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "rrrrrrdfsdfsdf";
            KeyPreview = true;
           
            
         
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/c \"python C:\\Users\\ControlLab1\\Desktop\\project\\csharp-python-exchange-via-txt\\svn_shared_data\\bin\\x64\\Debug\\svn.py\"";
           // startInfo.Arguments = "/C C:\\gstreamer\\1.0\\x86_64\\bin\\gst-launch-1.0.exe -v tcpclientsrc host=192.168.0.139 port=5001 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false ";
            process.StartInfo = startInfo;
            process.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

            using (var fs = new FileStream(@"test2.txt", FileMode.Open, FileAccess.ReadWrite, FileShare.ReadWrite))
            using (var reader = new StreamReader(fs, System.Text.Encoding.Default))
            {
                double feedback = 0;
                string readered = reader.ReadToEnd();
                if (sent)
                {
                    while (String.IsNullOrEmpty(readered))
                    {
                        readered = reader.ReadToEnd();
                        Console.WriteLine("stuckkkkkkkkkkkkk");
                    }

                    label1.Text = readered;

                    feedback = Convert.ToDouble(readered);
                        Console.WriteLine("afdsfd is: " + feedback.ToString());
                    label1.Text = feedback.ToString();
                    fs.SetLength(0);
                    sent = false;
                }

                
            }
      
        }
    }
}

