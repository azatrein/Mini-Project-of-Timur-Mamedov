# Mini-Project-of-Timur-Mamedov

First we create AWS: EC2 and RDS instances. Keep in mind the security properties of those and IAM.  

Use MobaXterm as a terminal or any other terminal(you can even connect to ec2 terminal so you won't enter "ssh -i "C:\...key.pem" ubuntu@IPofYourEC2"

Further, you can download all necesary packages like basic "sudo apt install python3" and all the other ones you'll find out later(there will be clues from linux)
make sure to download them in a virtual environment 
"python3 -m venv venv"
"source venv/bin/activate" to activate and just "deactivate" to quit

create directory "mkdir name" and python file "touch app.py" 
also templates directory where app.py is for "index.html"

access your directory "cd ..."

edit python file "nano app.py" (double tap to paste from normal IDE) "ctrl o" to save then enter and close "ctrl x"

connect to postgreSQL "psql -h RDSendpoint -U postgres -d postgres" postgres is default names of RDS

inject templates that you find in net or your own

make sure to install apache2 package - its the server because httpd would'n work in my case and "sudo systemctl status apache2" to check its status

make sure youe ec2 subnet is activatet: find networking in ec2 console -> subnet -> network ALC for both in/out bound rules to allow traffic from all ports

run "sudo python3 app.py" and go to http:\\EC2_IP:8000




