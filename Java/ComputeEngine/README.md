# Random Number Generator Compute Engine for Java™

## Create a virtual machine

I recommend making it an f1-micro (the cheapest one) running Ubuntu 18.0.4 LTS.

## Dependencies

Make sure you have installed Java 8 or newer.

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

You'll see the random number at <external ip>:8080/rng
