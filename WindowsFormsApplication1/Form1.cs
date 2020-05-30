using System;
using System.Windows.Forms;
using IronPython.Hosting;
using System.IO;
using System.IO.Pipes;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {

        int cch = 1;
        public Form1()
        {
            InitializeComponent();



        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {


           

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter(@"C:\Users\user\Desktop\rl_human\test.txt"))
            {
                writer.Write(textBox1.Text);

            }
        }

       
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            Console.WriteLine("co phim dc nhan");
            Console.WriteLine(e.KeyChar);
            
            using (StreamWriter writer = new StreamWriter(@"C:\Users\user\Desktop\rl_human\test.txt"))
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

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            using (var fs = new FileStream(@"C:\Users\user\Desktop\rl_human\test2.txt", FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
            using (var reader = new StreamReader(fs, System.Text.Encoding.Default))
            {

                Console.WriteLine(reader.ReadToEnd());
                //  label1.Text = text;
            }
        }
    }
}
