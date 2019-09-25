# Random Number Generator Compute Engine for Java™

## Demo

http://35.188.106.110:8080/rng/

## Create a virtual machine

I recommend making it an f1-micro (the cheapest one) running Ubuntu 18.0.4 LTS.

## Dependencies

After starting the virtual machine, make sure you install dependencies.

`sudo apt update && sudo apt full-upgrade`

You'll need git and at least Java 8.

`sudo apt install git openjdk-8-jdk`

Then you can clone this repository to the VM.

`git clone https://github.com/ColeChronowski/GCP-RNG.git`

## Firewall

Make sure you open up the firewall on your virtual machine to allow port 8080 TDP.

## Running

SSH into the virtual machine

Run the following command in the directory GCP-RNG/Java/ComputeEngine

`java -jar start.jar`

If you want to continue the service after closing the ssh window, you can run

`nohup java -jar start.jar`

instead.

## Observing

You'll see the random number at http://<external ip>:8080/rng
